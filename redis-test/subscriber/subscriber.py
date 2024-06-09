import redis

r = redis.Redis(host='localhost', port=6379)

pubsub = r.pubsub()
pubsub.subscribe('my_channel')

print("Subscribed to the channel...")

while True:
    message = pubsub.get_message()
    if message:
        print(message['data'])
