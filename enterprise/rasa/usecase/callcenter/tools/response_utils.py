import json

from flask import Response


def make_rasa_response(data, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns:
        HTTP response
    """

    return _make_rasa_response(data, status_code)


def _make_rasa_response(data, status_code):
    """Returns HTTP response for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns:
        HTTP response
    """

    json_data = json.dumps(data)

    return Response(response=json_data, status=status_code, mimetype='application/json')


def make_rasa_error_response(data, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns:
        HTTP response
    """

    return _make_rasa_response(data, status_code)


def make_rasa_error_logic_response(data, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns:
        HTTP response
    """

    return _make_rasa_response("No hay opción disponible para " + data, status_code)

