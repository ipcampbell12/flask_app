from flask import Blueprint, jsonify, abort, request
from ..models import Teacher, Student, db
bp = Blueprint('teachers', __name__, url_prefix='/teachers')


@bp.route('', methods=['GET'])
def index_teachers():
    teachers = Teacher.query.all()
    result = []
    for t in teachers:
        result.append(t.serialize())
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    t = Teacher.query.get_or_404(id)
    return jsonify(t.serialize())
