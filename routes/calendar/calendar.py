from flask import Blueprint, render_template, request, redirect, url_for
import calendar
from datetime import datetime

# Estrutura para armazenar eventos
events = {}

def save_event(date, event):
    if date not in events:
        events[date] = []
    events[date].append(event)

def get_events(date):
    return events.get(date, [])

class CustomHTMLCalendar(calendar.HTMLCalendar):
    def __init__(self, firstweekday=6):
        super().__init__(calendar.SUNDAY)

    def formatmonth(self, theyear, themonth, withyear=True):
        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="month">')
        a(self.formatweekheader())
        weeks = self.monthdays2calendar(theyear, themonth)
        for week in weeks:
            a(self.formatweek(week, theyear, themonth))  # Passa year e month
        while len(weeks) < 6:
            a(self.formatweek([(0, 0)] * 7, theyear, themonth))
            weeks.append(None)
        a('</table>')
        return ''.join(v)

    def formatweekheader(self):
        return '<tr class="week-header"><th class="day-name">Dom</th><th class="day-name">Seg</th><th class="day-name">Ter</th><th class="day-name">Qua</th><th class="day-name">Qui</th><th class="day-name">Sex</th><th class="day-name">Sáb</th></tr>'

    def formatday(self, day, weekday, year, month):
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # dia vazio
        else:
            day_str = f'{year}-{month:02d}-{day:02d}'
            day_events = '<br>'.join(get_events(day_str))

            # Verifica se a data pertence ao mês atual
            cell_class = 'day'
            if day_events:
                cell_class += ' has-event'
            
            return f'<td class="{cell_class}" onclick="openModal(\'{day_str}\')">{day}</td>'

    def formatweek(self, theweek, year, month):
        s = '<tr>'
        for d, wd in theweek:
            s += self.formatday(d, wd, year, month)  # Passa o year e month
        s += '</tr>'
        return s

MONTH_NAMES_PT = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]
    
calendar_blueprint = Blueprint('calendar', __name__, template_folder='templates', static_folder='static-calendar')

@calendar_blueprint.route('/calendar')
def calendar_menu():
    year = request.args.get('year', type=int, default=datetime.now().year)
    month = request.args.get('month', type=int, default=datetime.now().month)

    if request.args.get('action') == 'next_month' and month < 12:
        month += 1
    elif request.args.get('action') == 'prev_month' and month > 1:
        month -= 1
    elif request.args.get('action') == 'next_year':
        year += 1
    elif request.args.get('action') == 'prev_year' and year > 2024:
        year -= 1

    month_name_pt = MONTH_NAMES_PT[month - 1]
    cal = CustomHTMLCalendar().formatmonth(year, month)
    
    return render_template('calendar-menu.html', calendar=cal, year=year, month=month, month_name_pt=month_name_pt, events=events)

@calendar_blueprint.route('/add_event', methods=['POST'])
def add_event():
    date = request.form.get('date')
    event = request.form.get('event')
    
    if date and event:
        save_event(date, event)
    
    return redirect(url_for('calendar.calendar_menu', year=datetime.now().year, month=datetime.now().month))
