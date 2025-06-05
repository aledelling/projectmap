document.addEventListener('DOMContentLoaded', function() {
    // Seleccionar elementos del DOM
    const navLinks = document.querySelectorAll('.nav-link');
    const contentSections = document.querySelectorAll('.content-section');
    
    // Función para cambiar de sección
    function changeSection(e) {
        e.preventDefault();
        
        // Obtener la sección a mostrar
        const sectionToShow = this.getAttribute('data-section');
        
        // Remover clase active de todos los enlaces
        navLinks.forEach(link => link.classList.remove('active'));
        
        // Agregar clase active al enlace clickeado
        this.classList.add('active');
        
        // Ocultar todas las secciones
        contentSections.forEach(section => section.classList.add('hidden'));
        
        // Mostrar la sección correspondiente
        document.getElementById(`${sectionToShow}-section`).classList.remove('hidden');
    }
    
    // Agregar evento click a cada enlace de navegación
    navLinks.forEach(link => {
        link.addEventListener('click', changeSection);
    });
    
    // Aquí puedes agregar más funcionalidades específicas para cada sección
    // como manejo de formularios, interacciones con tablas, etc.
    
    // Ejemplo: Inicializar tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});