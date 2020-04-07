from datetime import date

class ToDoDAO():

    def __init__(self):
        self._todo_list = []
    
    def inserir(self, todo):
        todo.set_id(len(self._todo_list) + 1)
        todo.set_data(date.today())
        self._todo_list.append(todo)

    def listar(self):
        return self._todo_list