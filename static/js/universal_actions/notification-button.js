document.querySelectorAll('.fa-bell').forEach(function(icon) {
    icon.addEventListener('click', function(event) {

        if (this.classList.contains('fa-solid')) {
            this.classList.remove('fa-solid');
            this.classList.add('fa-regular');
        } else {
            this.classList.remove('fa-regular');
            this.classList.add('fa-solid');
        }
    });
});

