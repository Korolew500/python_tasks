import os


def info_dir(path_dir):
    all_files, all_dir, all_size = 0, 0, 0
    for i_file in os.listdir(path_dir):
        if os.path.isdir(os.path.join(path_dir, i_file)):
            count_files, count_dir, count_size = info_dir(os.path.join(path_dir, i_file))
            all_files += count_files
            all_dir += count_dir + 1
            all_size += count_size
        elif os.path.isfile(os.path.join(path_dir, i_file)):
            all_files += 1
            all_size += os.path.getsize(os.path.join(path_dir, i_file))
    return all_files, all_dir, all_size


user_path = input('Введите полный путь до каталога: ')
user_files, user_dir, user_size = info_dir(user_path)
print('Размер каталога (в Кб):', round(user_size/1024, 2))
print('Количество подкаталогов:', user_dir)
print('Количество файлов:', user_files)
