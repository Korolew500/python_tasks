class File:
    def __init__(self, name_file: str, mode: str, *args, **kwargs) -> None:
        self.name_file = name_file
        self.mode = mode
        self.args = args
        self.kwargs = kwargs

    def __enter__(self) -> str:
        try:
            self.file_name = open(self.name_file, self.mode, *self.args, *self.kwargs)
            return self.file_name.read()
        except FileNotFoundError:
            with open(self.name_file, 'w', *self.args, *self.kwargs) as self.write_file:
                print(f'Файл {self.name_file} был создан')
            self.file_name = open(self.name_file, self.mode, *self.args, *self.kwargs)
            return self.file_name.read()

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file_name.close()
        return True


with File('xyz.txt', 'r') as file_name:
    print(file_name)
