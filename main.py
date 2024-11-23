from src.kafka_consumer import consume_from_kafka
from src.kafka_producer import produce_to_kafka
from src.mongodb_consumer import consume_to_mongodb
import threading
import sys
from pathlib import Path


def kafka_pipeline():
    for data in consume_from_kafka():
        produce_to_kafka(data=data)

if __name__ == "__main__":
    # Thêm thư mục gốc của project vào sys.path
    sys.path.append(str(Path(__file__).resolve().parent / "src"))
    threading.Thread(target=kafka_pipeline).start()
    threading.Thread(target=consume_to_mongodb).start()