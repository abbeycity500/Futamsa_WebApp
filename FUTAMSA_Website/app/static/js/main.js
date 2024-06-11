// static/js/main.js

document.addEventListener('DOMContentLoaded', (event) => {
    // Common functionality to run when the document is fully loaded

    // Example: Navbar toggle for mobile view
    const navbarToggle = document.querySelector('.navbar-toggle');
    const navbarMenu = document.querySelector('.navbar-menu');

    if (navbarToggle && navbarMenu) {
        navbarToggle.addEventListener('click', () => {
            navbarMenu.classList.toggle('is-active');
        });
    }

    // Example: Flash message auto-dismiss
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach((message) => {
        setTimeout(() => {
            message.style.display = 'none';
        }, 5000);
    });
});
