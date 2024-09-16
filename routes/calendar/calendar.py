from flask import Blueprint, render_template, request
import calendar
from datetime import datetime

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
            a(self.formatweek(week))
        while len(weeks) < 6:
            a(self.formatweek([(0, 0)] * 7))
            weeks.append(None)
        a('</table>')
        return ''.join(v)
    
    def formatweekheader(self):
        return '<tr class="week-header"><th class="day-name">Dom</th><th class="day-name">Seg</th><th class="day-name">Ter</th><th class="day-name">Qua</th><th class="day-name">Qui</th><th class="day-name">Sex</th><th class="day-name">Sáb</th></tr>'
    
    def formatweek(self, theweek):
        s = '<tr>'
        for d, wd in theweek:
            if d == 0:
                s += '<td class="noday">&nbsp;</td>'
            else:
                s += '<td class="day">%d</td>' % d
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

    if request.args.get('action') == 'next_month' and month < 13:
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

    elif request.args.get('action') == 'prev_month' and month > 1:
        if month == 1 and year > 2024:
            month = 12
            year -= 1
        elif year >= 2024:
            month -= 1

    elif request.args.get('action') == 'next_year':
        year += 1

    elif request.args.get('action') == 'prev_year' and year > 2024:
        year -= 1

    month_name_pt = MONTH_NAMES_PT[month - 1]
    cal = CustomHTMLCalendar().formatmonth(year, month)

    return render_template('calendar-menu.html', calendar=cal, year=year, month=month, month_name_pt=month_name_pt, calendar_module=calendar)
