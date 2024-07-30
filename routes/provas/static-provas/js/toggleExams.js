function toggleExams(event) {
    const examsList = event.currentTarget.querySelector('.exams-list');
    if (examsList.style.display === 'none' || examsList.style.display === '') {
        examsList.style.display = 'block';
    } else {
        examsList.style.display = 'none';
    }
}

function ItemClick(event) {
    event.stopPropagation();
}