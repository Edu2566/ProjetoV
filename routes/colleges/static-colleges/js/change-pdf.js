document.addEventListener('DOMContentLoaded', function() {
    // Seleciona o botão e os iframes
    const button = document.querySelector('.button-header');
    const pdfViewer = document.querySelector('#pdfViewer');
    const templateViewer = document.querySelector('#templateViewer');
    
    // Estado inicial: exibe o PDF e oculta o template
    let showingPdf = true;
    
    button.addEventListener('click', function() {
        if (showingPdf) {
            // Oculta o PDF e exibe o template
            pdfViewer.style.display = 'none';
            templateViewer.style.display = 'block';
        } else {
            // Exibe o PDF e oculta o template
            pdfViewer.style.display = 'block';
            templateViewer.style.display = 'none';
        }
        
        // Alterna o estado
        showingPdf = !showingPdf;
    });
});
