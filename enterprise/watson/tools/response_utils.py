from flask import jsonify


def _make_repo_response(data, status_code):
    """Returns HTTP response for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns:
        HTTP response
    """

    response = jsonify(data)
    response.status_code = status_code

    return response


def make_repo_response(data, status_code):
    """Returns HTTP response with default JSON for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns HTTP response:
        {
            answer = {
                'confidence': 1.0,
                'entities': [
                    {'confidence': 1.0, 'name': 'entity_value', 'value': 'entity_value'},
                    {'confidence': 1.0, 'name': 'entity_value', 'value': 'entity_value'},
                ], 
                'intent': 'intent_name',
                'response': [], 
                'session': '@accenture.com', 
                'status': HTTP_CODE
            }
        }
    """
    answer = {
        'confidence': -1,
        'entities': [],
        'intent': '',
        'response': [],
        'session': '',
        'status': None
    }
    try:
        if data is not None \
                and float(data['confidence']) \
                and data['session'] \
                and int(data['status']):
            return _make_repo_response(data, status_code)
    except:
        return make_repo_error_response(answer, status_code)


def make_repo_error_response(data, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns HTTP response:
        {
            answer = {
                'confidence': 1.0,
                'entities': [
                    {'confidence': 1.0, 'name': 'entity_value', 'value': 'entity_value'},
                    {'confidence': 1.0, 'name': 'entity_value', 'value': 'entity_value'},
                ], 
                'intent': 'intent_name',
                'response': [], 
                'session': '@accenture.com', 
                'status': HTTP_CODE
            }
        }
    """
    answer = {}
    answer["confidence"] = -1
    answer["entities"] = []
    answer["intent"] = ''
    answer["response"] = [data if data is not None else 'WA General Error']
    answer["session"] = ''
    answer["status"] = status_code

    return _make_repo_response(answer, status_code)


def make_repo_error_auth_response(data, session, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        session: user session
        status_code: status code for HTTP response

    Returns:
        HTTP response
    """

    return _make_repo_response(data, status_code)


def make_repo_error_logic_response(data, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns:
        HTTP response
    """

    return _make_repo_response("No hay opción disponible para " + data, status_code)
