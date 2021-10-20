import time
import redis
import pickle
import config
from collections import deque
import threading

class RedisClientConnection:

    def __init__(self,subPattern):
        self.messageQueue = {}
        self.Lock = threading.Lock()
        self.cache = redis.Redis(host= config.CacheHost , port= config.CachePort)
        self.subListener = self.cache.pubsub(ignore_subscribe_messages=True)
        self.psub(subPattern)
        self.listenerThread = self.subListener.run_in_thread(sleep_time=0.3)


    def messageHandler(self,message):
        print("handeling")
        try:
            if message['type'] == 'pmessage':
                data = pickle.loads(message["data"])
                pcname = message["channel"].decode('utf-8')[3:]
                data["pcname"] = message["channel"].decode('utf-8')[3:]
                print("from handler")
                print(data)
                with self.Lock:
                    if pcname not in self.messageQueue:
                        self.messageQueue[pcname]=deque([data])
                    else:
                        self.messageQueue[pcname].append(data)
        except Exception as e:
            print(e)
            self.listenerThread.stop()
            self.listenerThread.join(timeout = 1.0)
            self.subListener.close()


    def psub(self,pattern):
        self.subListener.psubscribe(**{pattern : self.messageHandler})