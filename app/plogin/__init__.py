from flask import Blueprint

pdash = Blueprint('pdash',__name__, template_folder= 'templates', static_folder = 'static')
from app.plogin import routes