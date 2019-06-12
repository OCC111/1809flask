
from flask import Blueprint
from . import user,food

def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    user.api.register(bp_v1)
    food.api.register(bp_v1)

    return bp_v1