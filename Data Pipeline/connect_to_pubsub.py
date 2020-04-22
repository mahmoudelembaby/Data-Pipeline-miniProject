from google.cloud import pubsub_v1

project_id = "YOUR_PROJECT"
topic_name = "YOUR_TOPIC"
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)