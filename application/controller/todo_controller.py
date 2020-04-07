from application import app
from flask import render_template, request
from application.model.dao.todo_dao import ToDoDAO
from application.model.entity.todo import ToDo

todo_dao = ToDoDAO()

@app.route("/", methods=['GET'])
def home():
    todo_list = todo_dao.listar()
    return render_template("index.html", todo_list=todo_list), 200, {'Content-Type': 'text/html'}


@app.route("/inserir", methods=['POST'])
def inserir_todo():
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    todo = ToDo(titulo, descricao)
    todo_dao.inserir(todo)
    todo_list = todo_dao.listar()
    return render_template("index.html", todo_list=todo_list), 201, {'Content-Type': 'text/html'}
