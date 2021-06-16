# Uložit do zadaného souboru pouze sudá čísla nacházející se v jiném zadaném souboru.
# Můžete předpokládat, že se vám obsah souboru vejde do paměti.

def load_file_content(filename):
    """Vrátí obsah souboru ve formě řetězce."""
    file = open(filename)
    try:
        return file.read()
    finally:
        file.close()

def store_file_content(filename, content):
    """Uloží řetězec do souboru."""
    file = open(filename, 'w')
    try:
        file.write(content)
    finally:
        file.close()

def list_map(function, lst):
    """Vrátí seznam výsledků aplikací funkce na prvky seznamu."""
    result = []
    for element in lst:
        new_element = function(element)
        result += [new_element]
    return result

def list_filter(predicate, lst):
    """Vrátí seznam, který bude obsahovat pouze prvky seznamu lst, které splňují predikát."""
    result = []
    for element in lst:
        if predicate(element):
            result += [element]
    return result

def is_even(num):
	"""Rozhodne, zda je číslo sudé"""
	if num % 2 == 0:
		return True
	else:
		return False

def filter_predicate_from_file(filename, predicate):
	"""Vrátí seznam čísel podle predikátu"""
	content = load_file_content(filename)
	nums = list_map(int, content.split())
	even_nums = list_filter(predicate, nums)
	return even_nums

def store_numbers_to_file(filename, numbers):
	"""Zapíše seznam čísel do souboru"""
	even_nums_str = ''
	for i in range(len(numbers)):
		even_nums_str += (str(numbers[i]) + '\n')
	store_file_content(filename, even_nums_str)

def store_predicate_numbers(source_file, target_file, predicate):
	"""Vezme čísla z prvního souboru a zapíše z nich jen čísla vyhocující predikátu do druhého souboru"""
	even_nums = filter_predicate_from_file(source_file, predicate)
	store_numbers_to_file(target_file, even_nums)


store_predicate_numbers('file.txt', 'numbers.txt', lambda n: n < 10)
