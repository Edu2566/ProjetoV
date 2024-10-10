document.addEventListener("DOMContentLoaded", function() {
    var expandButtons = document.querySelectorAll(".expand-button");

    expandButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            var nestedList = this.nextElementSibling;

            // Alterna a exibição da lista suspensa
            if (nestedList.style.display === "block") {
                nestedList.style.display = "none";
            } else {
                nestedList.style.display = "block";
            }
        });
    });
});
