from confluent_kafka import Producer
from src.utils import load_env, load_config

def produce_to_kafka(data):
    kafka_config = load_config()['KAFKA_DEV_SERVER']
    env = load_env()
    topic = env['KAFKA_LOCAL_TOPIC']
    producer = Producer(dict(kafka_config))

    def delivery_report(err, msg):
        if err:
            print(f"Delivery failed: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    producer.produce(topic, data.encode('utf-8'), callback=delivery_report)
    producer.flush()


# produce_to_kafka(topic='dev_topic',config='KAFKA_DEV_SERVER',data={'key':'value'})