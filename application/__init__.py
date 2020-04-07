from flask import Flask
import os
static_folder = os.path.abspath("application/view/static")
templates_folder = os.path.abspath("application/view/templates")
app = Flask(__name__, template_folder=templates_folder, static_folder=static_folder)

from application.controller import todo_controller