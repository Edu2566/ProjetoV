from flask import Blueprint, render_template, request
import calendar
from datetime import datetime

class CustomHTMLCalendar(calendar.HTMLCalendar):
    def formatmonthname(self, theyear, themonth, withyear=True):
        # Substituir o cabeçalho padrão por uma string vazia
        return ''
    
    def formatweekheader(self):
    # Adicionar uma classe aos nomes dos dias da semana
        return '<tr class="week-header"><th class="day-name">Seg</th><th class="day-name">Ter</th><th class="day-name">Qua</th><th class="day-name">Qui</th><th class="day-name">Sex</th><th class="day-name">Sáb</th><th class="day-name">Dom</th></tr>'

MONTH_NAMES_PT = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]
    
calendario_blueprint = Blueprint('calendario', __name__, template_folder='templates', static_folder='static-calendario')

@calendario_blueprint.route('/calendario')
def calendario_menu():
    year = request.args.get('year', type=int, default=datetime.now().year)
    month = request.args.get('month', type=int, default=datetime.now().month)

    # Gerar o calendário para o mês e ano especificados
    cal = CustomHTMLCalendar().formatmonth(year, month)

    # Calcular o mês e ano anterior e próximo
    prev_month = month - 1 if month > 1 else 12
    prev_year = year - 1 if month == 1 else year
    next_month = month + 1 if month < 12 else 1
    next_year = year + 1 if month == 12 else year

    # Calcular o ano anterior e próximo
    prev_year_only = year - 1
    next_year_only = year + 1

    month_name_pt = MONTH_NAMES_PT[month - 1]

    return render_template('calendarioMenu.html', calendar=cal, year=year, month=month,
                           prev_month=prev_month, prev_year=prev_year,
                           next_month=next_month, next_year=next_year,
                           prev_year_only=prev_year_only, next_year_only=next_year_only,
                           month_name_pt=month_name_pt, calendar_module=calendar)