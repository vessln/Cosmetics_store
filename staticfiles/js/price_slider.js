const priceRange = document.getElementById("price-range");
const priceValue = document.getElementById("price-value");

// Update the price value when the slider value changes
priceRange.addEventListener("input", function() {
    priceValue.textContent = this.value;
});
