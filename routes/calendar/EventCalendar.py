# calendar_utils.py
import calendar
from datetime import datetime

class EventCalendar:
    def __init__(self):
        self.events = {}

    def save_event(self, date, event):
        if date not in self.events:
            self.events[date] = []
        self.events[date].append(event)

    def get_events(self, date):
        return self.events.get(date, [])

    class CustomHTMLCalendar(calendar.HTMLCalendar):
        def __init__(self, parent_calendar, firstweekday=6):
            super().__init__(calendar.SUNDAY)
            self.parent_calendar = parent_calendar

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
                day_str = f'{day:02d}/{month:02d}/{year}'
                day_events = '<br>'.join(self.parent_calendar.get_events(day_str))

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

    def get_month_name(self, month):
        return self.MONTH_NAMES_PT[month - 1]
