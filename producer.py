import pulsar

import json
import time
import random

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('iot-gw')

def generate_durian_sensor_data():
    return {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "humidity": round(random.uniform(50, 90), 2),  # %RH
        "temperature": round(random.uniform(20, 35), 2),  # °C
        "weight": round(random.uniform(1.5, 5.0), 2),  # kg
        "ethylene_ppm": round(random.uniform(0.1, 5.0), 2),  # Ethylene gas level (ppm)
        "ripeness_level": random.choice(["unripe", "mature", "ripe", "overripe"]),
    }

while True:
    json_data = json.dumps(generate_durian_sensor_data())
    producer.send((json_data).encode('utf-8'))
    time.sleep(1)

client.close()