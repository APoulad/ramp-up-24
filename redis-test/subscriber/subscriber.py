import redis

r = redis.Redis(host='redis', port=6379)

pubsub = r.pubsub()
pubsub.subscribe('my_channel')

print("Subscribed to the channel...")

while True:
    message = pubsub.get_message()
    if message and message['type'] == 'message':
        print(message['data'].decode('utf-8'))