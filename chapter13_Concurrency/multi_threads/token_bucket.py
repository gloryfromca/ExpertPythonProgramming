from threading import Lock
import time
class Throttle(object):
    def __init__(self, rate):
        self._consume_lock = Lock()
        self.rate = rate
        self.tokens = 0
        self.last = 0
    def consume(self, amount=1):
        with self._consume_lock:
            now = time.time()

            if self.last == 0:
                self.last = now
            elapsed = now - self.last
            incr = int(elapsed * self.rate)

            if incr:
                self.tokens += incr
            self.tokens = self.rate if self.rate < self.tokens else self.tokens

            if self.tokens >= amount:
                self.tokens -= amount
            else:
                amount = 0
            return amount





