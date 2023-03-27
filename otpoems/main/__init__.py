from flask import Blueprint

bp = Blueprint('main', __name__)

from otpoems.main import routes