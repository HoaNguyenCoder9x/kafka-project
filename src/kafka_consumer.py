from confluent_kafka import Consumer
from src.utils import load_config, load_env

def consume_from_kafka():
    
    kafka_config = load_config()['KAFKA_PROD_SERVER']
    env = load_env()
    topic = env['KAFKA_PROD_TOPIC']
    

    consumer = Consumer(dict(kafka_config))
    consumer.subscribe([topic])

    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        yield msg.value().decode('utf-8')
    consumer.close()


# c = consume_from_kafka(config='KAFKA_PROD_SERVER',topic='product_view')
# for i in c:
#     print(i)
