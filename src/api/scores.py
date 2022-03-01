from flask import Blueprint, jsonify, abort, request
from ..models import Student, Score, db
bp = Blueprint('scores', __name__, url_prefix='/scores')


@bp.route('', methods=['GET'])
def index_score():
    scores = Score.query.all()
    result = []
    for s in scores:
        result.append(s.serialize())
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show_score(id: int):
    s = Score.query.get_or_404(id)
    return jsonify(s.serialize())


@bp.route('', methods=['POST'])
def create_score():
    if 'student_id' not in request.json or 'score' not in request.json or 'standard_id' not in request.json:
        return abort(400)
    Student.query.get_or_404(request.json['student_id'])
    s = Score(
        student_id=request.json['student_id'],
        standard_id=request.json['standard_id'],
        score=request.json['score']
    )

    db.session.add(s)
    db.session.commit()
    return jsonify(s.seralize())
