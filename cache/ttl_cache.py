from lru_cache import LRUCache


def ttl_cache(ttl, limit):
    lru = LRUCache(limit)

    def decorator(func):
        def inner(path, method):
            key = str(path) + str(method)
            if key in lru.cache:
                return lru.get(key)
            res = func(path, method)
            return res
        return inner
    return decorator
