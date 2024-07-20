document.getElementById('tipo-busca').addEventListener('change', function() {
    var selectedValue = this.value;
    var lists = document.querySelectorAll('.faculdades-column');

    lists.forEach(function(list) {
        if (list.getAttribute('data-type') === selectedValue) {
            list.style.display = 'block';
        } else {
            list.style.display = 'none';
        }
    });
});