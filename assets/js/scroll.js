// Save the scroll position of the sidebar
document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.querySelector('.bd-sidebar');

    // Check if there's a saved scroll position and apply it
    const savedScrollPosition = localStorage.getItem('sidebarScrollPosition');
    if (savedScrollPosition) {
        sidebar.scrollTop = savedScrollPosition;
    }

    // Save scroll position before navigating
    document.querySelectorAll('.bd-links-link').forEach(link => {
        link.addEventListener('click', function () {
            localStorage.setItem('sidebarScrollPosition', sidebar.scrollTop);
        });
    });
});