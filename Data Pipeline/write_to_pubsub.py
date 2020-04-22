import json

project_id = "PROJECT"
topic_name = "TOPIC"
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)



def write_to_pubsub(deviceId, temperature, location, time):
    try:
        data = json.dumps({
            'deviceId': deviceId,
            'temperature': temperature,
            'location': location,
            'time': time
        }, ensure_ascii=False)

        publisher.publish(topic_path,
                          data.encode("utf-8"))
        print(data)

    except Exception as e:
        print(e)
        raise