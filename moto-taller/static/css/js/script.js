const btnMenu = document.getElementById('btn-menu');
const navLinks = document.getElementById('nav-links');

btnMenu.addEventListener('click', () => {
  navLinks.classList.toggle('activo');
});