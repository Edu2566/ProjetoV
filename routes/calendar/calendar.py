# main_calendar.py
from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from routes.calendar.event_calendar import EventCalendar

# Instância da classe EventCalendar
event_calendar = EventCalendar()

calendar_blueprint = Blueprint('calendar', __name__, template_folder='templates', static_folder='static-calendar')

@calendar_blueprint.route('/calendar')
def calendar_menu():
    year = request.args.get('year', type=int, default=datetime.now().year)
    month = request.args.get('month', type=int, default=datetime.now().month)

    # Controle de navegação entre meses e anos
    if request.args.get('action') == 'next_month':
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    elif request.args.get('action') == 'prev_month':
        if month == 1 and year > 2024:
            month = 12
            year -= 1
        elif month == 1 and year == 2024:
            pass
        else:
            month -= 1
    elif request.args.get('action') == 'next_year':
        year += 1
    elif request.args.get('action') == 'prev_year' and year > 2024:
        year -= 1

    month_name_pt = event_calendar.get_month_name(month)
    cal = event_calendar.CustomHTMLCalendar(event_calendar).formatmonth(year, month)
    
    return render_template('calendar-menu.html', calendar=cal, year=year, month=month, month_name_pt=month_name_pt, events=event_calendar.events)

@calendar_blueprint.route('/add_event', methods=['POST'])
def add_event():
    date = request.form.get('date')
    event = request.form.get('event')
    
    if date and event:
        event_calendar.save_event(date, event)
    
    return redirect(url_for('calendar.calendar_menu', year=datetime.now().year, month=datetime.now().month))

@calendar_blueprint.route('/update_event', methods=['POST'])
def update_event():
    date = request.form.get('date')
    old_event_name = request.form.get('old_event_name')
    new_event_name = request.form.get('new_event_name')

    if date and old_event_name and new_event_name:
        if date in event_calendar.events:
            try:
                # Atualiza o evento
                event_index = event_calendar.events[date].index(old_event_name)
                event_calendar.events[date][event_index] = new_event_name
            except ValueError:
                pass  # Se o evento antigo não for encontrado, ignore

    return redirect(url_for('calendar.calendar_menu', year=datetime.now().year, month=datetime.now().month))

@calendar_blueprint.route('/delete_event', methods=['POST'])
def delete_event():
    date = request.form.get('date')
    event = request.form.get('event')

    if date and event:
        if date in event_calendar.events:
            try:
                event_calendar.events[date].remove(event)
                if not event_calendar.events[date]:  # Se não houver mais eventos na data, remove a chave
                    del event_calendar.events[date]
            except ValueError:
                pass  # Se o evento não for encontrado, ignore

    return {'success': True}
