//
// // Select the price slider element
// var priceSlider = document.getElementById('price-range');
//
// // Check if the slider position is stored in localStorage
// if (localStorage.getItem('max_price')) {
//     // If yes, set the slider position to the stored value
//     priceSlider.value = localStorage.getItem('max_price');
//     // Update the displayed value
//     document.getElementById('price-value').textContent = priceSlider.value;
// }
//
// // Add an event listener to update the displayed value and store the slider position when the slider is moved
// priceSlider.addEventListener('input', function() {
//     // Update the displayed value
//     document.getElementById('price-value').textContent = this.value;
//     // Store the slider position in localStorage
//     localStorage.setItem('max_price', this.value);
// });
//
// // Select the spinner element
// var spinner = document.getElementById('spinner');
//
// // Check if the spinner position is stored in localStorage
// if (localStorage.getItem('spinner_position')) {
//     // If yes, set the spinner position to the stored value
//     spinner.value = localStorage.getItem('spinner_position');
// }
//
// // Add an event listener to store the spinner position when it is changed
// spinner.addEventListener('change', function() {
//     // Store the spinner position in localStorage
//     localStorage.setItem('spinner_position', this.value);
// });
//

document.addEventListener('DOMContentLoaded', function() {
    // Check if the page is refreshed
    if (performance.navigation.type === 1) {
        // Clear stored price and spinner position when the page is refreshed
        localStorage.removeItem('max_price');
        localStorage.removeItem('spinner_position');
    }

    // Select the price slider element
    var priceSlider = document.getElementById('price-range');

    // Check if the slider position is stored in localStorage
    if (localStorage.getItem('max_price')) {
        // If yes, set the slider position to the stored value
        priceSlider.value = localStorage.getItem('max_price');
        // Update the displayed value
        document.getElementById('price-value').textContent = priceSlider.value;
    }

    // Add an event listener to update the displayed value and store the slider position when the slider is moved
    priceSlider.addEventListener('input', function() {
        // Update the displayed value
        document.getElementById('price-value').textContent = this.value;
        // Store the slider position in localStorage
        localStorage.setItem('max_price', this.value);
    });

    // Select the form element
    var form = document.querySelector('form');

    // Add an event listener to the form submit event to store the spinner position when filters are applied
    form.addEventListener('submit', function(event) {
        // Prevent the form from submitting normally
        event.preventDefault();

        // Select the spinner element
        var spinner = document.getElementById('spinner');
        // Store the spinner position in localStorage
        localStorage.setItem('spinner_position', spinner.value);

        // Submit the form
        form.submit();
    });

    // Add an event listener to detect clicks anywhere on the page
    document.addEventListener('click', function(event) {
        // Check if the click occurred outside the form or the "Apply Filters" button
        if (!event.target.closest('form') && event.target.tagName !== 'BUTTON') {
            // Clear stored price and spinner position
            localStorage.removeItem('max_price');
            localStorage.removeItem('spinner_position');
        }
    });
});


