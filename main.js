let currentIndex =0;
        
function changeSlide(direction) {
    const slidesContainer = document.querySelector('.slider');
    const slideWidth = document.querySelector('.slider').offsetWidth;
    currentIndex += direction;

    if (currentIndex < 0) {
        currentIndex = 0; // Prevent sliding to the left when at the first slide
    }
    const transformValue = -currentIndex * slideWidth + 'px';
    slidesContainer.style.transform = 'translateX(' + transformValue + ')';
}