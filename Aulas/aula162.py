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

