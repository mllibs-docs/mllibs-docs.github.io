from PIL import Image

# Load the JPEG image
IMAGE_INPUT_PATH = "logo.jpeg"
FAVICON_OUTPUT_PATH = "docs/en/static/favicon.png"
LOGO_OUTPUT_PATH = "docs/en/static/logo.png"
image = Image.open(IMAGE_INPUT_PATH)

# Resize the image
favicon_size = (32, 32)
logo_size = (64, 64)
favicon_image = image.resize(favicon_size, Image.Resampling.LANCZOS)
logo_image = image.resize(logo_size, Image.Resampling.LANCZOS)

favicon_image = favicon_image.convert("RGBA")
logo_image = logo_image.convert("RGBA")

# Save
favicon_image.save(FAVICON_OUTPUT_PATH)
logo_image.save(LOGO_OUTPUT_PATH)
