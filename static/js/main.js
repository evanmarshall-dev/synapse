// Mobile menu toggle functionality
document.addEventListener('DOMContentLoaded', () => {
  const navbarToggle = document.querySelector('.navbar-toggle');
  const navbarMenuMobile = document.querySelector('.navbar-menu-mobile');

  if (navbarToggle && navbarMenuMobile) {
    navbarToggle.addEventListener('click', () => {
      navbarToggle.classList.toggle('active');
      navbarMenuMobile.classList.toggle('active');
      navbarToggle.setAttribute(
        'aria-expanded',
        navbarToggle.classList.contains('active'),
      );
    });

    // Close menu when a link is clicked
    navbarMenuMobile.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        navbarToggle.classList.remove('active');
        navbarMenuMobile.classList.remove('active');
        navbarToggle.setAttribute('aria-expanded', 'false');
      });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.navbar')) {
        navbarToggle.classList.remove('active');
        navbarMenuMobile.classList.remove('active');
        navbarToggle.setAttribute('aria-expanded', 'false');
      }
    });
  }
});
