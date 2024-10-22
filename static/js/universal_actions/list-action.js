document.addEventListener("DOMContentLoaded", function() {
    var expandButtons = document.querySelectorAll(".expand-button");

    expandButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            var nestedList = this.nextElementSibling;

            if (nestedList.classList.contains("active")) {
                nestedList.style.maxHeight = null;
                nestedList.style.opacity = 0;
                nestedList.classList.remove("active");
            } else {
                nestedList.style.maxHeight = nestedList.scrollHeight + "px";
                nestedList.style.opacity = 1;
                nestedList.classList.add("active");
            }
        });
    });
});
