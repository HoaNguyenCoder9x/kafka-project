from confluent_kafka import Consumer
from pymongo import MongoClient
from src.utils import load_config, load_env
# import sys
# from pathlib import Path


def consume_to_mongodb():
    config = load_config()['KAFKA_DEV_SERVER']
    env = load_env()
    topic = env['KAFKA_LOCAL_TOPIC']

    consumer = Consumer(dict(config))
    consumer.subscribe([topic])

    # Define MongoDB Setting 
    mongo_client = MongoClient(env['MONGODB_URI'])
    db = mongo_client[env['MONGODB_NAME']]
    collection = db[env['COLLECTION_NAME']]

    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        collection.insert_one({'data': msg.value().decode('utf-8')})
        print("Data inserted into MongoDB.")
    consumer.close()


# consume_to_mongodb(topic='dev_topic',config='KAFKA_DEV_SERVER')