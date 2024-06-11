// static/js/events.js

document.addEventListener('DOMContentLoaded', (event) => {
    // Events page specific functionality

    // Example: Event filtering by date or category
    const eventFilters = document.querySelectorAll('.event-filter');
    const eventsList = document.querySelector('.events-list');

    if (eventFilters && eventsList) {
        eventFilters.forEach((filter) => {
            filter.addEventListener('change', (e) => {
                const filterType = e.target.name;
                const filterValue = e.target.value;

                const events = eventsList.querySelectorAll('.event-item');
                events.forEach((eventItem) => {
                    const eventDate = eventItem.dataset.date;
                    const eventCategory = eventItem.dataset.category;

                    let shouldDisplay = true;

                    if (filterType === 'date' && filterValue) {
                        shouldDisplay = eventDate === filterValue;
                    }

                    if (filterType === 'category' && filterValue) {
                        shouldDisplay = eventCategory === filterValue;
                    }

                    eventItem.style.display = shouldDisplay ? 'block' : 'none';
                });
            });
        });
    }

    // Example: Expand and collapse event details
    const eventDetailsToggles = document.querySelectorAll('.event-details-toggle');
    eventDetailsToggles.forEach((toggle) => {
        toggle.addEventListener('click', (e) => {
            const eventDetails = e.target.nextElementSibling;
            if (eventDetails) {
                eventDetails.classList.toggle('is-hidden');
            }
        });
    });
});
