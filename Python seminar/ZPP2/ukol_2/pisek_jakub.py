# Soubor čísel je soubor, který má na každém řádku jedno celé číslo.
#
# Napište funkci, která pro soubor čísel vytvoří soubor jejich druhých
#  mocnin.
#
# Není možné načíst celý soubor do paměti provést výpočet a výsledek
#  uložit do souboru. Je nutné zpracovávat soubor řádek po řádku.
#
# Vaši funkci využijte v programu, který se nejprve zeptá uživatele na
#  zdrojový a poté na cílový soubor. Program dále zavolá vaši funkci,
#  úspěch oznámí uživateli a ukončí se. V případě neúspěchu
#  program uživatele co nejlépe informuje o vzniklé chybě a ukončí se.
#
# Program si musí poradit i se situací, kdy je vstupní soubor ve špatném formátu.
#
# Program nesmí skončit chybou - výpisem chyby interpretu.
#
# Bonusový požadavek: Napište vaší funkci pomocí funkce file_map (obdoby funkce file_filter).

# Odevzdání první verze do 20. dubna 8:45.
# Možnost uznání úkolu do 4. května 8:45.
# Jako předmět e-mailu uveďte ZPP2_1_2.

def write_down_powers(source, target):
	"""Práce se soubory pro následné zapsání"""
	source_file = open_file(source)
	try:
		target_file = open_file(target, 'w')
		try:
			write_powers_to_file(source_file, target_file)
		finally:
			target_file.close()
	finally:
		source_file.close()


def open_file(file, mode='r'):
	"""Otevření souboru s daným parametrem"""
	try:
		return open(file, mode)
	except:
		raise RuntimeError(f'Nepodařilo se otevřít soubor {file}')


def write_powers_to_file(source_file, target_file):
	"""Zápis druhé mocniny ze zdrojového do cílového souboru"""
	line = source_file.readline()

	if line == '':
		raise ValueError('Prázdný zdrojový soubor')

	while line != '':
		#Prázdný řádek
		if line == '\n':
			line = source_file.readline()
			continue

		try:
			pow_num = pow(int(line), 2)
		except:
			raise ValueError('Nepovolené znaky (všechno kromě celých čísel)')

		target_file.write((str(pow_num) + '\n'))
		line = source_file.readline()

	return 0


def get_input_files():
	"""Získání souboru ze vstupu pro následné zapsání mocnění"""
	try:
		source_file = input('Zadejte prosím zdrojový soubor i s příponou: ')
		target_file = input('Zadejte prosím cílový soubor i s příponou: ')
		print('')
		write_down_powers(source_file, target_file)
	except RuntimeError as e:
		print(e)
	except FileNotFoundError as not_found:
		print(f'Soubor {not_found.filename} nenalezen')
	except ValueError as e:
		print(f'Soubor {source_file} obsahuje neplatná data')
		print(f'Důvod: {e}')
	else:
		print('Data byla úspěšně zapsána')


get_input_files()
