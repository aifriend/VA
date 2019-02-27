import http.client


def https_request(server, url, method, params, headers):
    conn = http.client.HTTPSConnection(server)
    conn.request(method, url, params, headers)
    response = conn.getresponse()
    data = response.read()
    return response.status, response.reason, data
