from os import path, walk


def py_files(user_path: str) -> iter:
    all_count = 0
    files_count = 0

    for path_w, directories, files in walk(user_path):
        for file in files:
            if file[-3:] == '.py':
                abs_path = path.abspath(path.join(path_w, file))

                with open(abs_path, 'r', encoding='utf-8') as python_file:
                    sum_line = 0
                    for line in python_file:
                        if line != '\n':
                            for symbol in line:
                                if symbol == '#':
                                    break
                                elif symbol == ' ':
                                    pass
                                else:
                                    sum_line += 1
                                    all_count += 1
                                    break
                    yield f'{sum_line} непустых строк содержит файл {abs_path}'
                    files_count += 1

    yield f'\nВсего {all_count} непустых строк содержат {files_count} файлов .py директории {user_path}'


print('Будем производить подсчет непустых строк в корневой директории данного проекта')
for file_lines in py_files(path.abspath(path.join('..', '..'))):
    print(file_lines)
