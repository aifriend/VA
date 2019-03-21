from flask.json import jsonify


def make_config_response(data, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns:
        HTTP response
    """

    return _make_config_response(data, status_code)


def _make_config_response(data, status_code):
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


def make_config_error_response(data, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns:
        HTTP response
    """

    return _make_config_response(data, status_code)


def make_config_error_logic_response(data, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns:
        HTTP response
    """

    return _make_config_response("No hay opción disponible para " + data, status_code)

