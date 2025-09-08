class Steck:
    def __init__(self):
        self.__obj = []

    def __str__(self):
        if len(self.__obj) > 0:
            return '; '.join(self.__obj)
        return ''

    def delite(self):
        self.__obj.pop()

    def new(self, name):
        self.__obj.append(name)


class TaskManager:
    def __init__(self):
        self.tasks = dict()

    def __str__(self):
        answer = ''
        for i_pry in sorted(self.tasks.keys()):
            answer += f'{i_pry} {self.tasks[i_pry]}\n'
        return answer

    def new_task(self, name, pry):
        if pry not in self.tasks:
            self.tasks[pry] = Steck()
        self.tasks[pry].new(name)

    def delite(self, pry=0):
        if pry in self.tasks:
            self.tasks[pry].delite()
            if str(self.tasks[pry]) == '':
                self.tasks.pop(pry)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
manager.delite(2)
manager.delite(2)
manager.delite(1111)
manager.delite()
print(manager)
