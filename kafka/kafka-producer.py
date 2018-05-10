from kafka import KafkaProducer
import boto
import msgpack
import time


settings = {
    'AWS_ACCESS_KEY_ID': 'AKIAJE2R7GYZOCFEGCMA',
    'AWS_SECRET_ACCESS_KEY': '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',
    'AWS_BUCKET_NAME': 'bitcoin-blockchain-de18b',
    'SEARCH_PREFIX': 'txns',
    'SEARCH_KEYS': ['.json'],
    'KAFKA_SERVERS': ['34.217.59.12:9092', '54.191.43.46:9092', '34.217.74.153:9092'],
    'KAFKA_TOPIC': 'txns'
}


def get_s3_paths():
    s3 = boto.connect_s3(
        settings.get('AWS_ACCESS_KEY_ID'),
        settings.get('AWS_SECRET_ACCESS_KEY')
    )
    bucket = s3.get_bucket(settings.get('AWS_BUCKET_NAME'))
    print(bucket)

    bucket_list = bucket.list(prefix=settings.get('SEARCH_PREFIX'))
    print(bucket_list)
    filtered_list = filter(
        lambda item: any(
            [key in item.name for key in settings.get('SEARCH_KEYS')]
        ), bucket_list
    )

    return filtered_list


def build_payloads(paths, count=None):
    payloads = []
    for path in paths:
        tokens = path.name.split('/')
        print(tokens)
        payload = {
            's3_path': path.name,
            'number': tokens[1],
            'file_name': tokens[-1]
        }
        print(payload)
        break
        payloads.append(payload)

        if count:
            count -= 1
            if count == 0:
                break

    return payloads


def send_to_kafka(payloads):
    producer = KafkaProducer(
        bootstrap_servers=settings.get('KAFKA_SERVERS'),
        value_serializer=msgpack.dumps
    )
    for payload in payloads:
        print(payload)
        time.sleep(1)
        producer.send(settings.get('KAFKA_TOPIC'), payload)


def run():
    paths = get_s3_paths()
    payloads = build_payloads(paths)
    #send_to_kafka(payloads)


if __name__ == '__main__':
    run()

