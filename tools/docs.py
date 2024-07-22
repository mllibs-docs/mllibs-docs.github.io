import logging
import os
import shutil
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
from multiprocessing import Pool
from pathlib import Path

import mkdocs
import mkdocs.commands
import mkdocs.commands.serve
import typer

logging.basicConfig(level=logging.INFO)

app = typer.Typer()

mkdocs_name = "mkdocs.yaml"

missing_translation_snippet = """
{!../../../docs/missing-translation.md!}
"""

docs_path = Path("docs")
en_docs_path = Path("docs/en")
en_config_path: Path = en_docs_path / mkdocs_name
site_path = Path("site").absolute()
build_site_path = Path("site_build").absolute()


def get_lang_paths() -> list[Path]:
    return sorted(docs_path.iterdir())


def complete_existing_lang(incomplete: str):
    lang_path: Path
    for lang_path in get_lang_paths():
        if lang_path.is_dir() and lang_path.name.startswith(incomplete):
            yield lang_path.name


def lang_callback(lang: str | None) -> str | None:
    if lang is None:
        return None
    lang = lang.lower()
    return lang


@app.command()
def build_lang(
    lang: str = typer.Argument(
        ..., callback=lang_callback, autocompletion=complete_existing_lang
    )
) -> None:
    lang_path: Path = docs_path / lang

    if not lang_path.is_dir():
        typer.echo(
            f"The language translation doesn't seem to exist yet: {lang}"
        )
        raise typer.Abort()
    build_site_dist_path = build_site_path / lang
    if lang == "en":
        dist_path = site_path
    else:
        dist_path = site_path / lang
        shutil.rmtree(dist_path, ignore_errors=True)

    current_dir = os.getcwd()
    os.chdir(lang_path)
    shutil.rmtree(build_site_dist_path, ignore_errors=True)
    print(build_site_dist_path)
    subprocess.run([
        "poetry", "run", "mkdocs", "build", "--site-dir", build_site_dist_path],
        check=True
    )
    shutil.copytree(build_site_dist_path, dist_path, dirs_exist_ok=True)
    os.chdir(current_dir)
    typer.secho(
        f"Successfully built docs for: {lang}", color=typer.colors.GREEN
    )


@app.command()
def build_all() -> None:
    shutil.rmtree(site_path, ignore_errors=True)
    langs = [lang.name for lang in get_lang_paths() if lang.is_dir()]
    cpu_count = os.cpu_count() or 1
    process_pool_size = cpu_count * 4
    typer.echo(f"Using process pool size: {process_pool_size}")
    with Pool(process_pool_size) as p:
        p.map(build_lang, langs)


@app.command()
def serve(
    lang: str = typer.Argument(
        None, callback=lang_callback, autocompletion=complete_existing_lang
    ),
) -> None:
    os.environ["LINENUMS"] = "true"

    if lang is None:
        lang = "en"

    lang_path: Path = docs_path / lang
    os.chdir(lang_path)
    mkdocs.commands.serve.serve()


@app.command()
def static_server() -> None:
    typer.echo("Warning: this is a very simple server.")
    typer.echo("For development, use the command live instead.")
    typer.echo(
        "This is here only to preview a site with translations already built.")
    typer.echo("Make sure you run the build-all command first.")
    os.chdir("site")
    server_address = ("", 8000)
    server = HTTPServer(server_address, SimpleHTTPRequestHandler)
    typer.echo("Serving at: http://127.0.0.1:8000")
    server.serve_forever()


if __name__ == "__main__":
    app()
