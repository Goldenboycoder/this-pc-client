import time
import redis
import pickle
import config
from collections import deque

class RedisClientConnection:

    def __init__(self,subPattern):
        self.messageQueue = deque()
        self.cache = redis.Redis(host= config.CacheHost , port= config.CachePort)
        self.subListener = self.cache.pubsub(ignore_subscribe_messages=True)
        self.sub(subPattern)
        self.listenerThread = self.subListener.run_in_thread(sleep_time=0.3)


    def messageHandler(self,message):
        print("handeling")
        try:
            if type(message) !=int:
                data = pickle.loads(message["data"])
                print("from handler")
                print(data)
                self.messageQueue.append(data)
        except Exception as e:
            print(e)
            self.listenerThread.stop()
            self.listenerThread.join(timeout = 1.0)
            self.subListener.close()

    def lopp(self):
        for msg in self.subListener.listen():
            if type(msg["data"]) != int:
                data = pickle.loads(msg["data"])
                print(data)
            #self.messageQueue.append(data)
            time.sleep(1)

    def sub(self,pattern):
        print("ggggggggggg")
        #self.subListener.subscribe(**{"PC-DESKTOP-8G6O9EB" : self.messageHandler})
        self.subListener.psubscribe(**{pattern : self.messageHandler})