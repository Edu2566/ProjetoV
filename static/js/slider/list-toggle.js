document.addEventListener("DOMContentLoaded", function() {
    const selectElement = document.getElementById("search-type");
    const collegesColumn = document.querySelector('[data-type="colleges"]');
    const coursesColumn = document.querySelector('[data-type="courses"]');

    function toggleColumns() {
        if (selectElement.value === "colleges") {
            collegesColumn.style.display = "grid";
            coursesColumn.style.display = "none";
        } else if (selectElement.value === "courses") {
            collegesColumn.style.display = "none";
            coursesColumn.style.display = "grid";
        }
    }

    toggleColumns();

    selectElement.addEventListener("change", toggleColumns);
});
