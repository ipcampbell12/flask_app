from flask import Blueprint, jsonify, abort, request
from ..models import Teacher, Student, db
bp = Blueprint('students', __name__, url_prefix='/students')


@bp.route('', methods=['GET'])
def index_students():
    students = Student.query.all()
    result = []
    for s in students:
        result.append(s.serialize())
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show_students(id: int):
    s = Student.query.get_or_404(id)
    return jsonify(s.serialize())
