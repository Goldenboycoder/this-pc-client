import redis
import pickle
import config
from collections import deque

class RedisClientConnection:

    def __init__(self,subPattern):
        self.messageQueue = deque([])
        self.cache = redis.Redis(host= config.CacheHost , port= config.CachePort)
        self.subListener = self.cache.pubsub(ignore_subscribe_messages=True)
        self.sub(subPattern)
        self.listenerThread = self.subListener.run_in_thread(sleep_time=0.3)


    def messageHandler(self,message):
        try:
            data = pickle.loads(message["data"])
            print("from handler")
            print(data)
            self.messageQueue.append(data)
        except Exception as e:
            print(e)
            self.listenerThread.stop()
            self.listenerThread.join(timeout = 1.0)
            self.subListener.close()


    def sub(self,pattern):
        self.subListener.subscribe(**{pattern : self.messageHandler})  