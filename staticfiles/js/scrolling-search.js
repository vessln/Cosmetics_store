document.addEventListener("DOMContentLoaded", function() {
    const searchButton = document.getElementById("search-button");

    if (searchButton) {
        searchButton.addEventListener("click", function(event) {
            event.preventDefault();

            window.scroll({
                top: 700,
                left: 0,
                behavior: "smooth"
            });
        });
    }
});