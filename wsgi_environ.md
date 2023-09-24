REMOTE_ADDR: IP-адрес удаленного клиента (клиентского компьютера).

REMOTE_HOST: Имя хоста удаленного клиента (обычно совпадает с IP-адресом).

REMOTE_PORT: Порт удаленного клиента.

REQUEST_METHOD: Метод HTTP-запроса, например, "GET".

SERVER_PORT: Порт сервера, на котором выполняется ваше приложение.

SERVER_NAME: Имя сервера.

SERVER_SOFTWARE: Информация о программном обеспечении сервера (в данном случае, "waitress").

SERVER_PROTOCOL: Версия протокола HTTP (например, "HTTP/1.1").

SCRIPT_NAME: Путь к текущему скрипту (обычно пустая строка).

PATH_INFO: Путь запрошенного ресурса.

REQUEST_URI: Полный URI (Uniform Resource Identifier) запроса.

QUERY_STRING: Строка запроса (если она есть).

wsgi.url_scheme: Схема URL (обычно "http" или "https").

wsgi.version: Версия WSGI (1.0).

wsgi.errors: Поток ошибок для записи ошибок приложения.

wsgi.multithread: Указывает, поддерживает ли сервер многопоточность.

wsgi.multiprocess: Указывает, поддерживает ли сервер многопроцессов.

wsgi.run_once: Указывает, будет ли приложение запущено только один раз.

wsgi.input: Поток ввода, из которого можно читать данные запроса.

wsgi.file_wrapper: Обертка для файлового ввода.

wsgi.input_terminated: Указывает, завершен ли поток ввода.

HTTP_HOST: Заголовок "Host" из HTTP-запроса.

HTTP_CONNECTION: Заголовок "Connection" из HTTP-запроса.

HTTP_CACHE_CONTROL: Заголовок "Cache-Control" из HTTP-запроса.

HTTP_USER_AGENT: Заголовок "User-Agent" из HTTP-запроса, который содержит информацию о браузере клиента.

HTTP_ACCEPT: Заголовок "Accept" из HTTP-запроса, который указывает, какие типы контента клиент готов принять.

Другие заголовки HTTP, такие как HTTP_ACCEPT_LANGUAGE, HTTP_ACCEPT_ENCODING, HTTP_SEC_CH_UA, и другие, содержат различную информацию о запросе.

waitress.client_disconnected: Метод, который можно вызвать, чтобы проверить, был ли клиент отключен.