from app import app
from flask import jsonify, make_response, request
from werkzeug.exceptions import Unauthorized, InternalServerError
from networkx import dijkstra_path, from_numpy_matrix, shortest_path_length
from networkx.exception import NetworkXNoPath
import numpy as np
from functools import wraps


def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        try:
            if request.headers.get('x-api-key') and request.headers.get('x-api-key') == app.config['X-API-KEY']:
                return view_function(*args, **kwargs)
            else:
                return make_response(jsonify({"body": f'{Unauthorized.code}: '
                                                      f'{Unauthorized.description}'}), 401)
        except OSError:
            return make_response(jsonify({"body": f'{InternalServerError.code}: '
                                                  f'{InternalServerError.description}'}), 500)
    return decorated_function


@app.route('/', methods=['GET'])
@require_appkey
def get_route():
    try:
        city_start = int(request.values.get('city_start'))
        city_finish = int(request.values.get('city_finish'))
        distances = np.load(open(r"matrix_distance", "rb"))
        graph = from_numpy_matrix(distances)
        path = dijkstra_path(graph, city_start, city_finish, weight='weight')
        length = shortest_path_length(graph, city_start, city_finish, weight='weight')
        if length == 0:
            raise NetworkXNoPath
    except NetworkXNoPath:
        return make_response(jsonify({"body": 'No road'}), 404)
    except BaseException:
        return make_response(jsonify({"body": f'{InternalServerError.code} - {InternalServerError.description}'}), 500)
    return make_response(jsonify(body={'path': path, 'distance': length}))
