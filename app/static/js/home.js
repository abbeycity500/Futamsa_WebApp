// static/js/home.js

document.addEventListener('DOMContentLoaded', (event) => {
    // Home page specific functionality

    // Example: Initialize a slider
    const slider = document.querySelector('.slider');
    if (slider) {
        let currentIndex = 0;
        const slides = slider.querySelectorAll('.slide');
        const totalSlides = slides.length;

        const showSlide = (index) => {
            slides.forEach((slide, i) => {
                slide.style.display = (i === index) ? 'block' : 'none';
            });
        };

        document.querySelector('.slider-next').addEventListener('click', () => {
            currentIndex = (currentIndex + 1) % totalSlides;
            showSlide(currentIndex);
        });

        document.querySelector('.slider-prev').addEventListener('click', () => {
            currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
            showSlide(currentIndex);
        });

        showSlide(currentIndex);
    }
});
