def main(table):
    unique_rows = []
    non_empty_rows = []
    for row in table:
        if row not in unique_rows:
            unique_rows.append(row)
            if any(cell is not None for cell in row):
                non_empty_rows.append(row)
    transformed_table = []
    for row in non_empty_rows:
        transformed_row = []
        for cell in row:
            if '/' in cell:
                date_parts = cell.split('/')
                transformed_cell = '-'.join(
                    [part.zfill(2) for part in reversed(date_parts)]
                )
            elif '@' in cell:
                transformed_cell = cell.replace('@', '[at]')
            else:
                transformed_cell = cell
                index = transformed_cell.index('.')
                transformed_cell = transformed_cell[:index] + transformed_cell[
                                                              index + 2:
                                                              ]
            transformed_row.append(transformed_cell)
        transformed_table.append(transformed_row)
    transposed_table = list(map(list, zip(*transformed_table)))
    return transposed_table


table1 = [
    ['1', '2', '3'],
    ['14/12/02', 'П.Г. Риготман', 'rigotman49@mail.ru'],
    ['11/07/03', 'М.Ф. Вагобман', 'vagobman67@yahoo.com'],
    ['23/03/01', 'Я.М. Чесиди', 'cesidi41@mail.ru'],
    ['23/03/01', 'Я.М. Чесиди', 'cesidi41@mail.ru'],
    ['23/03/01', 'Я.М. Чесиди', 'cesidi41@mail.ru'],
    ['22/11/99', 'Я.Ш. Фурагин', 'furagin18@gmail.com']
]

table2 = [['14/12/02', 'П.Г. Риготман', 'rigotman49@mail.ru'], [None, None, None],
          ['11/07/03', 'М.Ф. Вагобман', 'vagobman67@yahoo.com'], ['23/03/01', 'Я.М. Чесиди', 'cesidi41@mail.ru'],
          ['23/03/01', 'Я.М. Чесиди', 'cesidi41@mail.ru'], [None, None, None],
          ['23/03/01', 'Я.М. Чесиди', 'cesidi41@mail.ru'], ['22/11/99', 'Я.Ш. Фурагин', 'furagin18@gmail.com']]

# result = main(table1)
result2 = main(table2)
# for row1 in result:
#     print('\t'.join(str(cell) for cell in row1))
print('\n')
for row1 in result2:
    print('\t'.join(str(cell) for cell in row1))
