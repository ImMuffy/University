# Vytvořit soubor numbers.txt, který bude obsahovat postupně čísla od nuly po zadané číslo, kde na každém řádku bude jedno číslo.
# Není možné si nejdříve vytvořit řetězec s obsahem a poté jej uložit. Musíte čísla zapisovat postupně.

def generate_numbers_to_file(filename, num):
	try:
		file = open(filename, 'w')
		for i in range(num):
			file.write(str(i) + '\n')
	finally:
		file.close()


generate_numbers_to_file('numbers.txt', 5)
