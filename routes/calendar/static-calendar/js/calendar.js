function openModal(date) {
    console.log('Abrindo modal para a data:', date); // Para depuração
    document.getElementById('eventDate').value = date;
    const calendarEvents = JSON.parse(document.getElementById('calendar-events').textContent);
    const eventList = document.getElementById('eventList');
    eventList.innerHTML = ''; // Limpa a lista anterior

    const dateEvents = calendarEvents[date] || [];
    dateEvents.forEach(event => {
        const li = document.createElement('li');
        li.textContent = event;

        const completedButton = document.createElement('button');
        completedButton.textContent = 'Concluído';
        completedButton.onclick = (e) => {
            e.stopPropagation();
            toggleCompletion(li);
        };

        li.onclick = () => openUpdateModal(date, event);
        li.appendChild(completedButton);
        eventList.appendChild(li);
    });

    document.getElementById('eventModal').style.display = 'grid'; // Exibe o modal
}

function closeModal() {
    console.log('Fechando modal'); // Para depuração
    document.getElementById('eventModal').style.display = 'none';
}

// (Resto do código permanece igual)


function closeModal() {
    document.getElementById('eventModal').style.display = 'none';
}

function toggleCompletion(li) {
    if (li.style.textDecoration === 'line-through') {
        li.style.textDecoration = 'none'; // Remove o risco
        li.style.color = 'black'; // Restaura a cor original do texto
    } else {
        li.style.textDecoration = 'line-through'; // Risca o texto
        li.style.color = 'gray'; // Muda a cor do texto para cinza
    }
}

function toggleCompletionAll(event) {
    event.stopPropagation(); // Impede que o clique no botão afete o evento do <li>
    
    const li = event.target.parentElement; // Obtém o <li> pai do botão
    li.classList.toggle('completed'); // Alterna a classe para o <li>
    
    // Impede que o texto do botão seja riscado
    const button = event.target; // Obtém o botão clicado
    if (li.classList.contains('completed')) {
        button.textContent = 'Não Concluído'; // Altera o texto do botão
    } else {
        button.textContent = 'Concluído'; // Altera o texto do botão de volta
    }
}

// Abre o segundo modal para editar ou excluir o evento
function openUpdateModal(date, event) {
    document.getElementById('updateEventDate').value = date;
    document.getElementById('oldEventName').value = event;
    document.getElementById('newEventName').value = event;
    document.getElementById('updateEventModal').style.display = 'grid';
}

// Fecha o modal de atualização
function closeUpdateModal() {
    document.getElementById('updateEventModal').style.display = 'none';
}

// Função para excluir o evento
function deleteEvent() {
    const date = document.getElementById('updateEventDate').value;
    const event = document.getElementById('oldEventName').value;
    const formData = new FormData();
    formData.append('date', date);
    formData.append('event', event);

    fetch("{{ url_for('calendar.delete_event') }}", {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Evento excluído com sucesso!');
            window.location.reload(); // Atualiza a página para refletir as mudanças
        } else {
            alert('Erro ao excluir o evento.');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

// Adiciona um listener de eventos para fechar os modais quando clicar fora deles
window.onclick = function(event) {
    const eventModal = document.getElementById('eventModal');
    const updateEventModal = document.getElementById('updateEventModal');
    if (event.target === eventModal) {
        closeModal();
    }
    if (event.target === updateEventModal) {
        closeUpdateModal();
    }
};
