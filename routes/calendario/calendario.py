from flask import Blueprint, render_template, request
import calendar
from datetime import datetime

class CustomHTMLCalendar(calendar.HTMLCalendar):
    def __init__(self, firstweekday=6):
        super().__init__(calendar.SUNDAY)  # Define domingo como o primeiro dia da semana
    
    def formatmonth(self, theyear, themonth, withyear=True):
        # Gera o corpo do mês
        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="month">')
        a('\n')
        a(self.formatweekheader())
        a('\n')
        weeks = self.monthdays2calendar(theyear, themonth)
        
        # Itera pelas semanas e adiciona ao HTML
        for week in weeks:
            a(self.formatweek(week))
            a('\n')
        
        # Verifica se há menos de 6 semanas e preenche as linhas faltantes
        while len(weeks) < 6:
            a(self.formatweek([(0, 0)] * 7))  # Adiciona uma semana vazia
            weeks.append(None)  # Incrementa o contador de semanas para sair do loop
        
        a('</table>')
        a('\n')
        return ''.join(v)
    
    def formatweekheader(self):
        return '<tr class="week-header"><th class="day-name">Dom</th><th class="day-name">Seg</th><th class="day-name">Ter</th><th class="day-name">Qua</th><th class="day-name">Qui</th><th class="day-name">Sex</th><th class="day-name">Sáb</th></tr>'
    
    def formatweek(self, theweek):
        s = '<tr>'
        for d, wd in theweek:
            if d == 0:
                s += '<td class="noday">&nbsp;</td>'  # Celula vazia para dias que não fazem parte do mês
            else:
                s += '<td class="day">%d</td>' % d
        s += '</tr>'
        return s
    
MONTH_NAMES_PT = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]
    
calendario_blueprint = Blueprint('calendario', __name__, template_folder='templates', static_folder='static-calendario')

@calendario_blueprint.route('/calendario')
def calendario_menu():
    year = request.args.get('year', type=int, default=datetime.now().year)
    month = request.args.get('month', type=int, default=datetime.now().month)

    # Calcular o mês e ano anterior e próximo com ajuste automático de ano
    if request.args.get('action') == 'next_month':
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

    elif request.args.get('action') == 'prev_month':
        if month == 1:
            month = 12
            year -= 1
        else:
            month -= 1

    elif request.args.get('action') == 'next_year':
        year += 1

    elif request.args.get('action') == 'prev_year':
        year -= 1

    # Nome do mês em português
    month_name_pt = MONTH_NAMES_PT[month - 1]

    # Gerar o calendário após a lógica de navegação
    cal = CustomHTMLCalendar().formatmonth(year, month)

    return render_template('calendarioMenu.html', calendar=cal, year=year, month=month,
                           month_name_pt=month_name_pt, calendar_module=calendar)
