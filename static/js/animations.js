// Navbar scroll effect
document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.querySelector('.navbar');
    const scrollToTopBtn = document.querySelector('.scroll-to-top');

    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
            scrollToTopBtn.classList.add('visible');
        } else {
            navbar.classList.remove('scrolled');
            scrollToTopBtn.classList.remove('visible');
        }
    });

    // Scroll to top functionality
    scrollToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Animate elements on scroll
    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.animate-on-scroll');
        
        elements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementTop < windowHeight - 100) {
                element.classList.add('animated');
            }
        });
    };

    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll(); // Initial check

    // Service cards hover effect
    const serviceCards = document.querySelectorAll('.service-card');
    serviceCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.querySelector('.service-icon').style.transform = 'scale(1.1) translateY(-5px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.querySelector('.service-icon').style.transform = 'none';
        });
    });

    // Counter animation for statistics
    const stats = document.querySelectorAll('.stat-number');
    let animated = false;

    const animateStats = function() {
        if (animated) return;
        
        stats.forEach(stat => {
            const target = parseInt(stat.getAttribute('data-target'));
            let current = 0;
            const increment = target / 60; // Animate over 60 frames
            
            const updateCounter = function() {
                if (current < target) {
                    current += increment;
                    stat.textContent = Math.round(current);
                    requestAnimationFrame(updateCounter);
                } else {
                    stat.textContent = target;
                }
            };
            
            updateCounter();
        });
        
        animated = true;
    };

    // Trigger stats animation when in view
    const statsSection = document.querySelector('.stats-section');
    if (statsSection) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateStats();
                }
            });
        }, { threshold: 0.5 });

        observer.observe(statsSection);
    }
});
