import http.client


# Peticion HTTPS generica
def https_request(server, url, method, body, headers):
    conn = http.client.HTTPSConnection(server)
    conn.request(method, url, body, headers)
    response = conn.getresponse()
    data = response.read()
    return response.status, response.reason, data
