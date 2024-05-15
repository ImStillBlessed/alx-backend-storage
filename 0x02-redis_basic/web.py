#!/usr/bin/env python3
"""
This is a simple exercise to implement a basic cache system.
"""
import requests
import redis
from functools import wraps
from typing import Callable


redis_client = redis.Redis()

def count_requests(method: Callable) -> Callable:
    """
    Decorator to count how many times a URL is accessed.
    """
    @wraps(method)
    def wrapper(url: str, *args, **kwargs):
        count_key = f"count:{url}"
        redis_client.incr(count_key)
        return method(url, *args, **kwargs)
    return wrapper

def cache_response(method: Callable) -> Callable:
    """
    Decorator to cache the response for a URL with an expiration time.
    """
    @wraps(method)
    def wrapper(url: str, *args, **kwargs):
        cache_key = f"cache:{url}"
        cached_response = redis_client.get(cache_key)
        if cached_response:
            return cached_response.decode('utf-8')

        response = method(url, *args, **kwargs)
        redis_client.setex(cache_key, 10, response)
        return response
    return wrapper

@count_requests
@cache_response
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a particular URL.

    Args:
        url (str): The URL to fetch the HTML content from.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
