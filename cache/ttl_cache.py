from lru_cache import LRUCache

# not working
def ttl_cache(ttl, limit):
    lru = LRUCache(limit)

    def decorator(func):
        def inner(*args, **kwargs):
            if [args, kwargs] in lru.cache:
                return lru.get([args, kwargs])
            res = func(*args, **kwargs)
            return res
        return inner
    return decorator
