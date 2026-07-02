let currentSlide = 0;
const slides = document.querySelectorAll('.carousel-slide');
const dots = document.querySelectorAll('.dot');

function goToSlide(i) {
  slides[currentSlide].classList.remove('active');
  dots[currentSlide].classList.remove('active');
  currentSlide = (i + slides.length) % slides.length;
  slides[currentSlide].classList.add('active');
  dots[currentSlide].classList.add('active');
}

function moveSlide(delta) {
  goToSlide(currentSlide + delta);
}

setInterval(() => moveSlide(1), 6000);

let cartCount = 0;
const cartBadge = document.querySelector('.cart-badge');
document.querySelectorAll('.add-to-bag').forEach(btn => {
  btn.addEventListener('click', () => {
    cartCount++;
    cartBadge.textContent = cartCount;
    const original = btn.textContent;
    btn.textContent = 'Added ✓';
    setTimeout(() => { btn.textContent = original; }, 900);
  });
});
