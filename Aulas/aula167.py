import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')

print(locale.getlocale())

print(calendar.calendar(2026))