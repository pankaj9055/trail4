// Auto-scroll carousel - 3 seconds timing, opacity-based transitions
function initMinimalCarousel() {
    const carouselContainer = document.querySelector('.carousel-container');
    const slides = document.querySelectorAll('.carousel-slide');
    
    if (!carouselContainer || slides.length === 0) {
        console.log('Carousel not found or no slides');
        return;
    }
    
    console.log(`Found ${slides.length} slides`);
    
    let currentSlide = 0;
    let autoScrollInterval;
    
    function nextSlide() {
        // Hide current slide
        console.log(`Hiding slide ${currentSlide}`);
        slides[currentSlide].style.opacity = '0';
        
        // Move to next slide
        currentSlide = (currentSlide + 1) % slides.length;
        
        // Show new slide
        console.log(`Showing slide ${currentSlide}`);
        slides[currentSlide].style.opacity = '1';
        
        console.log(`Moved to slide ${currentSlide + 1} - Total slides: ${slides.length}`);
    }
    
    function startAutoScroll() {
        console.log('Starting auto-scroll with 3 second intervals');
        if (slides.length > 1) {
            autoScrollInterval = setInterval(nextSlide, 3000); // 3 seconds auto-scroll
        }
    }
    
    function stopAutoScroll() {
        if (autoScrollInterval) {
            clearInterval(autoScrollInterval);
            console.log('Auto-scroll stopped');
        }
    }
    
    // Initialize carousel
    startAutoScroll();
    
    // Pause on hover, resume on leave
    carouselContainer.addEventListener('mouseenter', () => {
        stopAutoScroll();
    });
    
    carouselContainer.addEventListener('mouseleave', () => {
        startAutoScroll();
    });
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    initMinimalCarousel();
});