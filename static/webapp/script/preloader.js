var loader = document.getElementById("preloader");

// Set the desired preloader duration (in milliseconds)
var preloaderDuration = 1; // 1 seconds

// Hide the preloader after the specified duration
setTimeout(function() {
    loader.style.display = "none";
}, preloaderDuration);
