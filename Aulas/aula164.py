#formatando datas do datetime


from datetime import datetime


data = datetime.strptime('2026-04-13 07:58:03', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:%M'))