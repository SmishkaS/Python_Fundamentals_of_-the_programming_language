# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

str_file = 'file_for_DZ5_2.txt'

with open(str_file, 'r', encoding='utf-8') as f:
    count = 0
    for line in f.readlines():
        count += 1
        print(f"line number {count} contains {[len(line.split())]} words")
    print(f"all lines = {count}")
