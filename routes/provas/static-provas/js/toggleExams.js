function toggleExams(event) {
    const examsList = event.currentTarget.querySelector('.exams-list');
    examsList.classList.toggle('show');
}

function ItemClick(event) {
    event.stopPropagation();
}