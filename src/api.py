import json

from flask import request, Response, Blueprint

from api_handler import APIHAndler


api = Blueprint('apiv1', __name__, url_prefix='/api')


@api.route('/data')
def get_data():
    member_id = request.args.get('member_id')
    if not member_id:
        return Response('Missing parameter `member_id`.', status=400)
    api_handler = APIHAndler(member_id)
    data = api_handler.get_data()
    return Response(json.dumps(data), status=200, mimetype='application/json')