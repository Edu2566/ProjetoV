// Função para habilitar arrastar com o dedo
const notebookNames = document.querySelectorAll('.notebook-name');

notebookNames.forEach((notebookName) => {
    let isDown = false;
    let startX;
    let scrollLeft;

    notebookName.addEventListener('touchstart', (e) => {
        isDown = true;
        startX = e.touches[0].pageX - notebookName.offsetLeft;
        scrollLeft = notebookName.scrollLeft;
    });

    notebookName.addEventListener('touchmove', (e) => {
        if (!isDown) return;
        e.preventDefault(); // Previne o comportamento padrão do toque
        const x = e.touches[0].pageX - notebookName.offsetLeft;
        const walk = (x - startX) * 2; // Aumenta a velocidade de rolagem
        notebookName.scrollLeft = scrollLeft - walk;
    });

    notebookName.addEventListener('touchend', () => {
        isDown = false;
    });

    notebookName.addEventListener('touchcancel', () => {
        isDown = false;
    });
});
