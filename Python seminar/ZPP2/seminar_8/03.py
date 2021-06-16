# Napište funkci file_sum, která vrátí součet celých čísel v souboru, kde každé číslo je na jednom řádku.

def file_sum(filename):
	result_sum = 0
	file = open(filename)

	try:
		line = file.readline()
		while line != '':
			result_sum += int(line)
			line = file.readline()
	finally:
		file.close()

	return result_sum


print(file_sum('file.txt'))  # 23
