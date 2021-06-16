def load_file_content(name):
    try:
        file = open(name)
        try:
            return file.read()
        finally:
            file.close()
    except:
        raise RuntimeError('Nelze načíst obsah souboru ' + name)


"""
content = load_file_content('file.txt')
lines = content.split()
print(lines)
"""


def list_map(function, lst):
    result = []
    for element in lst:
        new_element = function(element)
        result += [new_element]
    return result


def parse_row(row_string):
    cells_string = row_string.split()
    return list_map(int, cells_string)

# print(parse_row('1 2 3')) # [1, 2, 3]


def parse_matrix(matrix_string):
    try:
        rows_string = matrix_string.split('\n')
        return list_map(parse_row, rows_string)
    except:
        raise RuntimeError('Matici nelze převézt: \n' + matrix_string)

# print(parse_matrix('1 2 3\n6 8 2\n9 5 2')) # [[1, 2, 3], [6, 8, 2], [9, 5, 2]]


def load_matrix(name):
    return parse_matrix(load_file_content(name))


print(load_matrix('matrix.txt'))  # [[1, 2, 3], [6, 8, 2], [9, 5, 2]]
