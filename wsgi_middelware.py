class RequestCounterMiddleware:
    def __init__(self, app):
        self.app = app
        self.request_count = 0

    def __call__(self, environ, start_response):
        self.request_count += 1
        print(self.request_count)
        response = self.app(environ, start_response)
        return response


class PathValidationMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        path = environ.get("PATH_INFO", "")

        if not path.startswith("/document"):
            status = "404 Not Found"
            headers = [("Content-type", "text/plain")]
            start_response(status, headers)
            return [b"404 Not Found"]

        return self.app(environ, start_response)


def simple_app(environ, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/plain")]
    start_response(status, headers)
    return [b"Hello, World!"]


# Создаем экземпляры middleware и применяем их к WSGI-приложению
app = simple_app
app = PathValidationMiddleware(app)
app = RequestCounterMiddleware(app)
