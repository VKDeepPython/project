from lru_cache import LRUCache


def lru_cache(limit):
    lru = LRUCache(limit)

    def decorator(func):
        def inner(*args, **kwargs):
            key = str(args, kwargs)
            if key in lru.cache:
                return lru.get(key)
            res = func(*args, **kwargs)
            lru.set(key, res)
            return res
        return inner
    return decorator
