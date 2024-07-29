def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding = 'utf-8')
    for num_str, str_ in enumerate(strings, 1):
        byte_ = file.tell()
        file.write(str_ + '\n')
        strings_positions[(num_str, byte_)] = str_
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)


