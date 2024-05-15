#!/usr/bin/env python3
"""
This is a simple exercise to implement a basic cache system.
"""
import uuid
import redis
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of calls to a method.
    Args:
        method (Callable): The method to be decorated.
    Returns:
        Callable: The wrapped method with counting functionality.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function.
    Args:
        method (Callable): The method to be decorated.
    Returns:
        Callable: The wrapped method with history tracking functionality.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs" 
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        
        return result
    return wrapper

def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function.
    Args:
        method (Callable): The method whose call history is to be displayed.
    """
    redis_client = method.__self__._redis
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"
    inputs = redis_client.lrange(input_key, 0, -1)
    outputs = redis_client.lrange(output_key, 0, -1)
    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for input_data, output_data in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{input_data.decode('utf-8')}) -> {output_data.decode('utf-8')}")



class Cache:
    """
    Cache class to handle storing data in a Redis database.
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the Redis cache and return the key.
        Args:
            data (str): The data to be stored in the cache.
        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, bytes, int, float]]:
        """
       Retrieve data from the Redis cache and optionally convert it using a callable.
        Args:
            key (str): The key under which the data is stored.
            fn (Optional[Callable]): A callable to convert the data.
        Returns:
            Optional[Union[str, bytes, int, float]]: The retrieved data, optionally converted, or None if key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from the Redis cache using the key.
        Args:
            key (str): The key under which the data is stored.
        Returns:
            str: The string stored in the cache.
        """
        return self.get(key, fn=lambda x: x.decode("utf-8"))
    
    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from the Redis cache using the key.
        Args:
            key (str): The key under which the data is stored.
        Returns:
            int: The integer stored in the cache.
        """
        return self.get(key, fn=lambda x: int(x))
    
    