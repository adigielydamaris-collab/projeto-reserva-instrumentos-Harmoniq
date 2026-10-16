function initNavigation() {
  document.querySelectorAll('.side nav').forEach((menu) => {
    const links = menu.querySelectorAll('.nav');

    function setActiveLink(activeLink) {
      links.forEach((link) => {
        link.classList.toggle('nav-on', link === activeLink);
      });
    }

    // Restore the active item after navigating to another page.
    const currentLink = Array.from(links).find((link) => {
      return link.hasAttribute('href') &&
        new URL(link.href).pathname === window.location.pathname;
    });

    if (currentLink) setActiveLink(currentLink);

    links.forEach((link) => {
      link.addEventListener('click', () => setActiveLink(link));
    });
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initNavigation);
} else {
  initNavigation();
}
