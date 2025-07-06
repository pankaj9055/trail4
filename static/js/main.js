// FurniLux Website JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Ensure critical elements are always visible first
    ensureElementsVisible();
    
    // Initialize all components
    initMobileMenu();
    initCarousel();
    initScrollReveal();
    initSmoothScroll();
    
    // Flash message auto-hide - reduced frequency
    setTimeout(() => {
        const flashMessages = document.querySelectorAll('.flash-messages .alert');
        flashMessages.forEach(msg => {
            msg.style.transition = 'opacity 0.5s ease';
            msg.style.opacity = '0';
            setTimeout(() => {
                if (msg.parentNode) msg.remove();
            }, 500);
        });
    }, 3000); // Reduced from 5000 to 3000
    
    // Re-ensure visibility after animations
    setTimeout(ensureElementsVisible, 500);
    setTimeout(ensureElementsVisible, 1500);
});

// Function to ensure navigation and products are always visible
function ensureElementsVisible() {
    // Force navigation lines to be visible
    const navLines = document.querySelectorAll('.nav-line-container, .nav-line');
    navLines.forEach(line => {
        line.style.display = 'block';
        line.style.visibility = 'visible';
        line.style.opacity = '1';
        line.style.transform = 'translateX(0)';
    });
    
    // Force products to be visible
    const products = document.querySelectorAll('.product-card');
    products.forEach(product => {
        product.style.display = 'block';
        product.style.visibility = 'visible';
        product.style.opacity = '1';
        product.style.transform = 'scale(1)';
        product.style.position = 'static';
        
        // Ensure buttons are properly positioned
        const buttons = product.querySelectorAll('button');
        buttons.forEach(button => {
            button.style.position = 'relative';
            button.style.zIndex = '10';
            button.style.display = 'inline-block';
            button.style.visibility = 'visible';
            button.style.opacity = '1';
        });
    });
    
    // Force about page content to be visible
    const aboutSections = document.querySelectorAll('section, .bg-white, .prose');
    aboutSections.forEach(section => {
        section.style.display = 'block';
        section.style.visibility = 'visible';
        section.style.opacity = '1';
    });
    
    // Force all text content to be visible
    const textElements = document.querySelectorAll('p, h1, h2, h3, h4, h5, h6, div');
    textElements.forEach(element => {
        element.style.visibility = 'visible';
        element.style.opacity = '1';
    });
}

// Mobile menu functionality
function initMobileMenu() {
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
    }
}

// Enhanced Carousel functionality with manual controls
function initCarousel() {
    const carouselTrack = document.querySelector('.carousel-track');
    const slides = document.querySelectorAll('.carousel-slide');
    const indicators = document.querySelectorAll('.indicator');
    const prevButton = document.querySelector('.carousel-prev');
    const nextButton = document.querySelector('.carousel-next');
    const autoScrollToggle = document.getElementById('autoScrollToggle');
    const autoScrollText = document.getElementById('autoScrollText');
    
    if (!carouselTrack || slides.length === 0) return;
    
    let currentSlide = 0;
    const totalSlides = slides.length;
    let isAutoScrolling = true;
    let autoScrollInterval;
    
    // Initialize auto-scroll
    function startAutoScroll() {
        if (isAutoScrolling) {
            autoScrollInterval = setInterval(() => {
                nextSlide();
            }, 5000); // Increased to 5 seconds for better UX
        }
    }
    
    function stopAutoScroll() {
        clearInterval(autoScrollInterval);
    }
    
    // Navigation functions
    function nextSlide() {
        currentSlide = (currentSlide + 1) % totalSlides;
        updateCarousel();
    }
    
    function prevSlide() {
        currentSlide = currentSlide === 0 ? totalSlides - 1 : currentSlide - 1;
        updateCarousel();
    }
    
    function goToSlide(index) {
        currentSlide = index;
        updateCarousel();
    }
    
    function updateCarousel() {
        const translateX = -currentSlide * 100;
        carouselTrack.style.transform = `translateX(${translateX}%)`;
        
        // Update indicators
        indicators.forEach((indicator, index) => {
            indicator.classList.toggle('active', index === currentSlide);
        });
    }
    
    // Event listeners
    if (prevButton) {
        prevButton.addEventListener('click', () => {
            prevSlide();
            stopAutoScroll();
            if (isAutoScrolling) startAutoScroll(); // Restart auto-scroll
        });
    }
    
    if (nextButton) {
        nextButton.addEventListener('click', () => {
            nextSlide();
            stopAutoScroll();
            if (isAutoScrolling) startAutoScroll(); // Restart auto-scroll
        });
    }
    
    // Indicator click handlers
    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => {
            goToSlide(index);
            stopAutoScroll();
            if (isAutoScrolling) startAutoScroll(); // Restart auto-scroll
        });
    });
    
    // Auto-scroll toggle
    if (autoScrollToggle) {
        autoScrollToggle.addEventListener('click', () => {
            isAutoScrolling = !isAutoScrolling;
            if (isAutoScrolling) {
                startAutoScroll();
                autoScrollToggle.innerHTML = '<i class="fas fa-pause mr-1"></i><span>Auto</span>';
            } else {
                stopAutoScroll();
                autoScrollToggle.innerHTML = '<i class="fas fa-play mr-1"></i><span>Manual</span>';
            }
        });
    }
    
    // Pause auto-scroll on hover (less intrusive)
    carouselTrack.addEventListener('mouseenter', () => {
        if (isAutoScrolling) stopAutoScroll();
    });
    
    carouselTrack.addEventListener('mouseleave', () => {
        if (isAutoScrolling) startAutoScroll();
    });
    
    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (document.activeElement.closest('.carousel-container')) {
            if (e.key === 'ArrowLeft') {
                e.preventDefault();
                prevSlide();
                stopAutoScroll();
                if (isAutoScrolling) startAutoScroll();
            } else if (e.key === 'ArrowRight') {
                e.preventDefault();
                nextSlide();
                stopAutoScroll();
                if (isAutoScrolling) startAutoScroll();
            }
        }
    });
    
    // Touch/swipe support for mobile
    let startX = 0;
    let endX = 0;
    
    carouselTrack.addEventListener('touchstart', (e) => {
        startX = e.touches[0].clientX;
    });
    
    carouselTrack.addEventListener('touchend', (e) => {
        endX = e.changedTouches[0].clientX;
        const diffX = startX - endX;
        
        if (Math.abs(diffX) > 50) { // Minimum swipe distance
            if (diffX > 0) {
                nextSlide();
            } else {
                prevSlide();
            }
            stopAutoScroll();
            if (isAutoScrolling) startAutoScroll();
        }
    });
    
    // Initialize
    updateCarousel();
    startAutoScroll();
}

// Scroll reveal animation
function initScrollReveal() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
            }
        });
    }, observerOptions);
    
    // Observe elements with scroll reveal animation
    document.querySelectorAll('.scroll-reveal').forEach(el => {
        observer.observe(el);
    });
    
    // Add scroll reveal class to elements that should animate
    document.querySelectorAll('.animate-fade-in, .animate-fade-in-delay, .animate-fade-in-delay-2, .animate-fade-in-delay-3').forEach(el => {
        el.classList.add('scroll-reveal');
    });
}

// Smooth scrolling for anchor links
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Image loading optimization
function initImageLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// Form validation
function validateForm(formElement) {
    const inputs = formElement.querySelectorAll('input[required], textarea[required], select[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.classList.add('error');
        } else {
            input.classList.remove('error');
        }
    });
    
    return isValid;
}

// Loading spinner
function showLoading() {
    const loadingSpinner = document.createElement('div');
    loadingSpinner.className = 'fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50';
    loadingSpinner.innerHTML = `
        <div class="bg-white rounded-lg p-4 flex items-center space-x-3">
            <div class="animate-spin rounded-full h-6 w-6 border-b-2 border-blue-600"></div>
            <span>Loading...</span>
        </div>
    `;
    document.body.appendChild(loadingSpinner);
    return loadingSpinner;
}

function hideLoading(spinner) {
    if (spinner && spinner.parentNode) {
        spinner.parentNode.removeChild(spinner);
    }
}

// Error handling
function showError(message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'fixed top-4 right-4 bg-red-500 text-white px-4 py-2 rounded-lg shadow-lg z-50';
    errorDiv.textContent = message;
    document.body.appendChild(errorDiv);
    
    setTimeout(() => {
        errorDiv.remove();
    }, 5000);
}

function showSuccess(message) {
    const successDiv = document.createElement('div');
    successDiv.className = 'fixed top-4 right-4 bg-green-500 text-white px-4 py-2 rounded-lg shadow-lg z-50';
    successDiv.textContent = message;
    document.body.appendChild(successDiv);
    
    setTimeout(() => {
        successDiv.remove();
    }, 5000);
}

// Performance optimization
function optimizePerformance() {
    // Lazy loading for images
    if ('IntersectionObserver' in window) {
        initImageLoading();
    }
    
    // Debounce scroll events
    window.addEventListener('scroll', debounce(() => {
        // Handle scroll events here
    }, 100));
    
    // Preload critical resources
    const preloadLinks = document.querySelectorAll('link[rel="preload"]');
    preloadLinks.forEach(link => {
        if (link.href) {
            fetch(link.href);
        }
    });
}

// Initialize performance optimizations
document.addEventListener('DOMContentLoaded', optimizePerformance);

// WhatsApp integration
function openWhatsApp(number, message = '') {
    // Prevent multiple clicks
    if (window.whatsappOpening) {
        return;
    }
    
    window.whatsappOpening = true;
    
    try {
        const cleanNumber = number.replace(/\D/g, '');
        const encodedMessage = encodeURIComponent(message);
        const url = `https://wa.me/${cleanNumber}?text=${encodedMessage}`;
        
        // Show feedback to user
        showSuccess('Opening WhatsApp...');
        
        // Open in new tab/window
        const whatsappWindow = window.open(url, '_blank', 'noopener,noreferrer');
        
        // Check if popup was blocked
        if (!whatsappWindow) {
            // Fallback: direct link if popup blocked
            window.location.href = url;
        }
        
    } catch (error) {
        console.error('Error opening WhatsApp:', error);
        showError('Failed to open WhatsApp. Please try again.');
    } finally {
        // Reset flag after 2 seconds
        setTimeout(() => {
            window.whatsappOpening = false;
        }, 2000);
    }
}

// Analytics tracking (placeholder)
function trackEvent(eventName, eventData = {}) {
    // Implementation for analytics tracking
    console.log('Event tracked:', eventName, eventData);
}

// Accessibility improvements
function initAccessibility() {
    // Add focus indicators
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Tab') {
            document.body.classList.add('using-keyboard');
        }
    });
    
    document.addEventListener('mousedown', () => {
        document.body.classList.remove('using-keyboard');
    });
    
    // Add skip link functionality
    const skipLink = document.querySelector('.skip-link');
    if (skipLink) {
        skipLink.addEventListener('click', (e) => {
            e.preventDefault();
            const target = document.querySelector(skipLink.getAttribute('href'));
            if (target) {
                target.focus();
            }
        });
    }
}

// Initialize accessibility features
document.addEventListener('DOMContentLoaded', initAccessibility);

// Export functions for use in other scripts
window.FurniLux = {
    showLoading,
    hideLoading,
    showError,
    showSuccess,
    openWhatsApp,
    trackEvent,
    validateForm
};
