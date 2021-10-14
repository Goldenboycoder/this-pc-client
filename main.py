from RedisConnector import RedisClientConnection
import time
redis = RedisClientConnection("PC-*")

while(True):
    time.sleep(0.6)
    data = redis.messageQueue.popleft()
    print("from main")
    print(data)