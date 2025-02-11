import pulsar
import clickhouse_connect
import json
import datetime

# Constants
CLICKHOUSE_CLOUD_HOSTNAME = 'localhost'
CLICKHOUSE_CLOUD_USER = 'mozox2'
CLICKHOUSE_CLOUD_PASSWORD = 'password'

PULSAR_HOST = 'localhost:6650'

# Pulsar connection
pulsar_client = pulsar.Client('pulsar://' + PULSAR_HOST)
consumer = pulsar_client.subscribe('iot-gw', subscription_name='my-sub')

# ClickHouse connection
clickhouse_client = clickhouse_connect.get_client(
    host=CLICKHOUSE_CLOUD_HOSTNAME, port=8123, username=CLICKHOUSE_CLOUD_USER, password=CLICKHOUSE_CLOUD_PASSWORD)

# Create table if exists

clickhouse_client.command('''
    CREATE TABLE IF NOT EXISTS durian_sensor (
        timestamp DateTime,
        humidity Float32,
        temperature Float32,
        weight Float32,
        ethylene_ppm Float32,
        ripeness_level String
    ) ENGINE = MergeTree()
    ORDER BY timestamp
''')

print("Table durian_sensor is ready")

while True:
    msg = consumer.receive()
    try:
        # Parse JSON data
        data = json.loads(msg.data().decode('utf-8'))
        print("Received: ", data)

        # Convert timestamp from string to datetime
        data['timestamp'] = datetime.datetime.strptime(data['timestamp'], "%Y-%m-%d %H:%M:%S")

        # Ensure correct data types
        formatted_data = [
            (
                data['timestamp'],               # DateTime format
                float(data['humidity']),         # Float32
                float(data['temperature']),      # Float32
                float(data['weight']),           # Float32
                float(data['ethylene_ppm']),     # Float32
                str(data['ripeness_level'])      # String
            )
        ]

        # Insert into ClickHouse
        clickhouse_client.insert('durian_sensor', formatted_data, 
                         column_names=['timestamp', 'humidity', 'temperature', 'weight', 'ethylene_ppm', 'ripeness_level'])

        consumer.acknowledge(msg)

    except Exception as e:
        print("Error processing message:", e)
        consumer.negative_acknowledge(msg)

pulsar_client.close()
clickhouse_client.close()