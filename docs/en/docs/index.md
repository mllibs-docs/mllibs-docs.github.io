---
title: 👨🏻‍💻 Whoami
description: Hi there 👋! My name is Luis Correa, and I'm a Computer Scientist & Software Developer. Welcome to my blog where I share insights into the fascinating world of Computer Science and Software Engineering.
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
    <h1>👨🏻‍💻 Whoami</h1>
    <p>
      Hi there 👋! My name is Luis Correa, and I'm a Computer Scientist &amp; Software Developer. Welcome to my blog where I share insights into the fascinating world of Computer Science and Software Engineering.
    </p>
    <p>
      This space is dedicated to exploring the depths of technology, going beyond surface-level explanations. Here, you'll find:
    </p>
    <ul>
      <li>In-depth technical articles on AI and ML technologies</li>
      <li>Discussions on software development best practices</li>
      <li>Explorations of emerging trends in computer science</li>
      <li>Case studies and project showcases</li>
    </ul>
    <p>
      My goal is to provide insights that not only explain the 'how' but also delve into the 'why' behind technological innovations.
    </p>
    <p>
      Through this blog, I aim to contribute to the advancement of knowledge in AI, complex algorithms, and the future of software engineering. I invite you to explore these topics with me and engage in constructive discussions about computer science and technological development.
    </p>
  </div>
</div>