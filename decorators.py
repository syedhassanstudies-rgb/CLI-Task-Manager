import time
import functools


def log_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n⚙  {func.__name__} called...")
        start = time.time()

        result = func(*args, **kwargs)

        duration = time.time() - start
        print(f"✓  {func.__name__} completed in {duration:.4f}s")

        return result
    return wrapper