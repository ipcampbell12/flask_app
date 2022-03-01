from flask import Blueprint, jsonify, abort, request
from ..models import Standard, db
bp = Blueprint('standards', __name__, url_prefix='/standards')


@bp.route('', methods=['GET'])
def index_standards():
    standards = Standard.query.all()
    result = []
    for s in standards:
        result.append(s.serialize())
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show_standards(id: int):
    s = Standard.query.get_or_404(id)
    return jsonify(s.serialize())
