import pika

# Подключение к RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Создание очереди с именем 'hello'
channel.queue_declare(queue='hello')

# Отправка сообщений в очередь
for i in range(1, 11):
    message = f'Сообщение {i}'
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(f'Отправлено: {message}')

# Закрытие соединения
connection.close()