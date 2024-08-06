def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w') as file:
        for i, string in enumerate(strings):
            file.write(string + '\n')
            strings_positions[i, file.tell()] = string
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
