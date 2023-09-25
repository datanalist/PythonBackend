# waitress-serve --listen=*:8000 wsgi_example:simple_app
def simple_app(environ, start_response):
    """Самый простой пример Веб приложения на WSGI"""
    print(environ)
    status = "200 OK"
    headers = [("Content-type", "text/plain")]
    start_response(status, headers)
    return [b"We are here!"]

