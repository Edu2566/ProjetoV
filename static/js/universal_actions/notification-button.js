document.querySelectorAll('.fa-bell').forEach(function(icon) {
    if (icon.id === 'side-bell') {
        return;
    }
    icon.addEventListener('click', function(event) {
        // Alterna as classes entre solid e regular
        if (this.classList.contains('fa-solid')) {
            this.classList.remove('fa-solid');
            this.classList.add('fa-regular');
        } else {
            this.classList.remove('fa-regular');
            this.classList.add('fa-solid');
        }
    });
});
