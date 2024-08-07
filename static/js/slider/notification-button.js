document.querySelectorAll('.swiper-slide .fa-bell').forEach(function(icon) {
    icon.addEventListener('click', function(event) {
        event.stopPropagation(); // Impede a propagação do evento para o elemento pai e o link

        if (this.classList.contains('fa-solid')) {
            this.classList.remove('fa-solid');
            this.classList.add('fa-regular');
        } else {
            this.classList.remove('fa-regular');
            this.classList.add('fa-solid');
        }
    });
});