import time
import heapq

class TimeBasedCache:
    def __init__(self):
        self.cache = {}  # Stores {key: (value, expiryTime)}
        self.expiry_heap = []  # Min-heap to track expiry times (expiryTime, key)

    def _clean_expired_keys(self):
        """Removes expired keys from the cache."""
        current_time = time.time()
        while self.expiry_heap and self.expiry_heap[0][0] <= current_time:
            _, key = heapq.heappop(self.expiry_heap)
            if key in self.cache and self.cache[key][1] <= current_time:
                del self.cache[key]  # Remove expired key

    def set(self, key, value, expiryTime):
        """Stores key-value pair with expiration."""
        expiry_timestamp = time.time() + expiryTime
        self.cache[key] = (value, expiry_timestamp)
        heapq.heappush(self.expiry_heap, (expiry_timestamp, key))
        self._clean_expired_keys()  # Clean expired keys on each set()

    def get(self, key):
        """Retrieves value if key exists and hasn't expired."""
        self._clean_expired_keys()  # Clean before fetching
        if key in self.cache:
            value, expiry_timestamp = self.cache[key]
            if expiry_timestamp > time.time():
                return value
            else:
                del self.cache[key]  # Remove expired key
        return None

# Example Usage
cache = TimeBasedCache()
cache.set("A", 100, 5)  # Key "A" expires in 5 seconds
print(cache.get("A"))  # Output: 100
time.sleep(6)  # Wait for expiry
print(cache.get("A"))  # Output: None (expired)
