'''#1. Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать генератор списков.'''

a = ['gvsa','egseerg','sfbbf']

tm = [len(i) for i in a]
print(f'{tm[0]} - {a[0]} {tm[1]} - {a[1]} {tm[2]} - {a[2]}')

