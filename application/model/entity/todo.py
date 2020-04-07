class ToDo():

    def __init__(self, titulo, descricao):
        self._id = None
        self._titulo = titulo
        self._descricao = descricao
        self._data = None
    
    def get_id(self):
        return self._id

    def get_titulo(self):
        return self._titulo

    def get_descricao(self):
        return self._descricao

    def get_id(self):
        return self._id

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def set_id(self, id):
        self._id = id

