def store_file_content(filename, content):
    """Uloží řetězec content do souboru filename."""
    file = open(filename, 'w')
    try:
        file.write(content)
    finally:
        file.close()

store_file_content('file.txt', '12\n3')
store_file_content('file2.txt', '56\n32\n11')
