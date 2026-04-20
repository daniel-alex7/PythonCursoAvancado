# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz 
# from datetime import datetime  

# part 1

# data_str = '2026-04-20 07:49:54' 
# data_str_fmt = '%Y-%m-%d %H:%M:%S' 

# # data = datetime(2026, 4, 20, 7, 49, 54)
# data = datetime.strptime(data_str, data_str_fmt)
# print(data)


#  part 2

# data = datetime.now()
# print(data.timestamp())  # Isso está na base de dados
# print(datetime.fromtimestamp(1776726108.490952))

# part 3

# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime

from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
# delta = timedelta(days=10, hours=2)
delta = relativedelta(data_fim, data_inicio)
print(delta.days, delta.years)
# print(data_fim - delta)
# print(data_fim)
# print(data_fim + relativedelta(seconds=60, minutes=10))

# delta = data_fim - data_inicio
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)