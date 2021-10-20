from RedisConnector import RedisClientConnection
import time

redis = RedisClientConnection("PC-*")
#redis.lopp()

while(True):
    try:
        with redis.Lock:
            data = redis.messageQueue.popleft()
        print("from main")
        print(data)
    except Exception as e:
        print(e)
    time.sleep(2)