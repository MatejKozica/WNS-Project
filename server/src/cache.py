import pickle

from redis import Redis

class Cache:

    def __init__(self, namespace, ttl=None) -> None:
        self.redis = Redis("wns_redis", 6379)
        self.namespace = namespace
        self.ttl = ttl

    def _key(self, name, namespace=None):
        return f"{namespace or self.namespace}:{name}"

    def set(self, name, data, namespace=None, ttl=None):
        self.redis.set(self._key(name, namespace), pickle.dumps(data))

    def get(self, name, namespace=None):
        data = self.redis.get(self._key(name, namespace))
        data = pickle.loads(data)
        return data

    def keys(self, namespace=None):
        glob_key = self._key("*", namespace)
        return self.redis.keys(glob_key)


cache = Cache("airplanes")