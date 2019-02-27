from flask import jsonify


def make_business_response(data, status_code):
    """Returns HTTP response for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns:
        HTTP response
    """

    return _make_business_response(data, status_code)


def _make_business_response(data, status_code):
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


def make_business_error_response(data, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns:
        HTTP response
    """

    return _make_business_response(data, status_code)


def make_business_error_auth_response(data, session, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        session: user session
        status_code: status code for HTTP response

    Returns:
        HTTP response
    """

    return _make_business_response(data, status_code)


def make_business_error_logic_response(data, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns:
        HTTP response
    """

    return _make_business_response(data, status_code)

