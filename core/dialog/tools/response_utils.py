from flask import jsonify


def _make_dialog_response(data, status_code):
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


def make_faq_dialog_response(data, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns HTTP response:
        {
            "answer": {
                "next": ""
                "question": [
                    {
                        "id": 0
                        "transcript": request,
                        "type": type,
                    }
                ],
                "session": "",
            }
        }
    """

    answer = {"answer": {}}
    answer["answer"]["next"] = ""
    answer["answer"]["question"] = []
    try:
        if data is not None:
            answer["answer"]["session"] = data.session
            item = {
                "id": 0,
                "transcript": data.answer,
                "type": ""
            }
            answer["answer"]["question"].append(item)
    except:
        pass

    return _make_dialog_response(answer, status_code)


def make_dialog_response(data, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns HTTP response:
        {
            "answer": {
                "next": ""
                "question": [
                    {
                        "id": 0
                        "transcript": request,
                        "type": type,
                    }
                ],
                "session": "",
            }
        }
    """

    answer = {"answer": {}}
    answer["answer"]["next"] = ""
    answer["answer"]["question"] = []
    try:
        if len(data) > 0:
            answer["answer"]["session"] = data[0]["recipient_id"]
            for i in range(0, len(data)):
                item = {
                    "id": 0,
                    "transcript": data[i]["text"],
                    "type": ""
                }
                answer["answer"]["question"].append(item)
    except:
        pass

    return _make_dialog_response(answer, status_code)


def make_dialog_error_response(data, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns HTTP response:
        {
            "answer": {
                "next": ""
                "question": [
                    {
                        "id": -1
                        "transcript": request,
                        "type": type,
                    }
                ],
                "session": "",
            }
        }
    """

    answer = {"answer": {}}
    answer["answer"]["next"] = ""
    answer["answer"]["question"] = []
    try:
        if len(data) > 0:
            answer["answer"]["session"] = data[0]["recipient_id"]
            for i in range(0, len(data)):
                item = {
                    "id": -1,
                    "transcript": data[i]["text"],
                    "type": ""
                }
                answer["answer"]["question"].append(item)
    except:
        pass

    return _make_dialog_response(answer, status_code)


def make_dialog_error_response(data):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information

    Returns HTTP response:
        {
            "answer": {
                "next": ""
                "question": [
                    {
                        "id": -1
                        "transcript": request,
                        "type": type,
                    }
                ],
                "session": "",
            }
        }
    """

    answer = {"answer": {}}
    answer["answer"]["next"] = ""
    answer["answer"]["question"] = []
    answer["answer"]["session"] = ""
    try:
        if data:
            item = {
                "id": -1,
                "transcript": data,
                "type": ""
            }
            answer["answer"]["question"].append(item)
    except:
        pass

    return _make_dialog_response(answer, 200)


def make_dialog_error_logic_response(data, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns HTTP response:
        {
            "answer": {
                "next": ""
                "question": [
                    {
                        "id": -2
                        "transcript": request,
                        "type": type,
                    }
                ],
                "session": "",
            }
        }
    """

    answer = {"answer": {}}
    answer["answer"]["next"] = ""
    answer["answer"]["question"] = []
    try:
        if len(data) > 0:
            answer["answer"]["session"] = data[0]["recipient_id"]
            for i in range(0, len(data)):
                item = {
                    "id": -2,
                    "transcript": data[i]["text"],
                    "type": ""
                }
                answer["answer"]["question"].append(item)
    except:
        pass

    return _make_dialog_response(answer, status_code)


def make_dialog_error_auth_response(data, session, status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        data: JSON with response information
        session: user session
        status_code: status code for HTTP response

    Returns HTTP response:
        {
            "answer": {
                "next": ""
                "question": [
                    {
                        "id": -3
                        "transcript": request,
                        "type": type,
                    }
                ],
                "session": "",
            }
        }
    """

    answer = {"answer": {}}
    answer["answer"]["next"] = ""
    answer["answer"]["question"] = []
    try:
        if len(data) > 0:
            answer["answer"]["session"] = data[0]["recipient_id"]
            for i in range(0, len(data)):
                item = {
                    "id": -3,
                    "transcript": data[i]["text"],
                    "type": ""
                }
                answer["answer"]["question"].append(item)
    except:
        pass

    return _make_dialog_response(answer, status_code)
