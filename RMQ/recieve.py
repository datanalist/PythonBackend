import pika

# Подключение к RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Создание очереди с именем 'hello'
channel.queue_declare(queue='hello')

# Функция обработки сообщений из очереди
def callback(ch, method, properties, body):
    print(f'Получено: {body}')

# Установка функции обработки сообщений
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

# Начало прослушивания очереди
print('Ожидание сообщений. Для выхода нажмите CTRL+C')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print('Завершение прослушивания очереди.')
    connection.close()