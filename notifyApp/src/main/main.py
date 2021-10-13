import pika


def notify_to_console(text):
    print(text)


def on_notify(ch, method, properties, body):
    notify_to_console(body.decode())


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='event')

    channel.basic_consume(queue='event', on_message_callback=on_notify, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    main()
