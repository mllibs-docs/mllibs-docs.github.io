---
hide_comments: true
hide:
  - navigation
---

<style>
  .whoami-container * {
    margin: 0 !important;
  }

  .whoami-container {
    display: flex;
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
    background-color: var(--md-default-bg-color);
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .content {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    flex: 1 1 auto;
  }

  .avatar-container {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    flex: 0 0 auto;
  }

  .avatar {
    border-radius: 50%;
    width: 300px;
    height: 300px;
    object-fit: cover;
    border: 4px solid var(--md-primary-fg-color);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .vcard-name {
    font-size: 1.5rem;
    font-weight: bold;
    color: var(--md-default-fg-color);
    margin-bottom: 0.25rem;
  }

  .vcard-username {
    font-size: 1.1rem;
    font-style: normal;
    color: var(--md-default-fg-color--light);
  }

  .content p {
    line-height: 1.6;
    color: var(--md-default-fg-color);
  }

  .content ul {
    list-style-type: none;
    padding-left: 1rem;
  }

  .content li {
    margin-bottom: 0.5rem;
    position: relative;
  }

  .content li::before {
    content: '•';
    color: var(--md-primary-fg-color);
    font-weight: bold;
    position: absolute;
    left: -1rem;
  }

  @media (max-width: 768px) {
    .whoami-container {
      flex-direction: column;
      padding: 1.5rem;
    }

    .avatar-container {
      margin-bottom: 1.5rem;
    }

    .avatar {
      width: 150px;
      height: 150px;
    }
  }
</style>

<div class="whoami-container">
  <div class="avatar-container">
    <img src="/static/avatar.jpeg" alt="luiscib3r" class="avatar" />
    <div class="vcard-info">
      <h2 class="vcard-name">Luis Ciber</h2>
      <span class="vcard-username">luiscib3r</span>
    </div>
  </div>
  <div class="content">
    <h1>Whoami</h1>
    <p>
      ¡Hola! 👋 Mi nombre es Luis Correa, y soy Científico de la Computación y Desarrollador de Software. Bienvenido a mi blog donde comparto ideas sobre el fascinante mundo de la Ciencia de la Computación y la Ingeniería de Software.
    </p>
    <p>
      Este espacio está dedicado a explorar las profundidades de la tecnología, yendo más allá de las explicaciones superficiales. Aquí encontrarás:
    </p>
    <ul>
      <li>Artículos técnicos detallados sobre tecnologías de IA y ML</li>
      <li>Discusiones sobre las mejores prácticas en desarrollo de software</li>
      <li>Exploraciones de tendencias emergentes en ciencias de la computación</li>
      <li>Estudios de casos y presentaciones de proyectos</li>
    </ul>
    <p>
      Mi objetivo es proporcionar perspectivas que no solo expliquen el 'cómo', sino que también profundicen en el 'por qué' detrás de las innovaciones tecnológicas.
    </p>
    <p>
      A través de este blog, aspiro a contribuir al avance del conocimiento en IA, algoritmos complejos y el futuro de la ingeniería de software. Te invito a explorar estos temas conmigo y a participar en discusiones constructivas sobre el desarrollo tecnológico.
    </p>
  </div>
</div>