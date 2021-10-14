from RedisConnector import RedisClientConnection
import time

redis = RedisClientConnection("PC-*")
#redis.lopp()

while(True):
    time.sleep(2)
    try:
        data = redis.messageQueue.popleft()
        print("from main")
        print(data)
    except Exception as e:
        print(e)