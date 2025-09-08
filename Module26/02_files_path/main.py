from os import sep, walk, path


def gen_files_path(user_path: str, dir_name: str) -> iter:
    for path_w, directories, files in walk(user_path):
        if path_w.split(sep)[-1] == dir_name:
            yield '\nПолные адреса папок в каталоге:'
            for direct in directories:
                yield path.abspath(path.join(path_w, direct))
            yield '\nПолные адреса файлов в каталоге:'
            for file in files:
                yield path.abspath(path.join(path_w, file))
            break


print('Будем производить поиск в корневой директории данного проекта')
dir_user_name = input('Введите название каталога (например "Module26"): ')
for abs_path in gen_files_path(path.abspath(path.join('..', '..')), dir_user_name):
    print(abs_path)
