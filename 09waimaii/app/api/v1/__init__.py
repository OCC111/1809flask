
from flask import Blueprint
from . import member,food

def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    member.api.register(bp_v1)
    food.api.register(bp_v1)

    return bp_v1