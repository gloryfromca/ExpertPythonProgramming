import time
from geopy.geocoders import Nominatim
if __name__ == "__main__":
    from synchronous import PLACES
    from token_bucket import Throttle
else:
    from .synchronous import PLACES
    from .token_bucket import Throttle

from queue import Queue, Empty
from threading import Thread

geolocator = Nominatim()
THREAD_POOL_SIZE = 4

def fetch_place(place):
    return geolocator.geocode(place)

def worker(work_queue, result_queue, throttle):
    while not work_queue.empty():
        try:
            item = work_queue.get(block=False)
        except Empty:
            break
        else:
            while not throttle.consume():
                pass
            try:
                result = fetch_place(item)
            except Exception as e:
                result = e
            finally:
                result_queue.put(result)
                work_queue.task_done()
def main():
    work_queue = Queue()
    result_queue = Queue()
    throttle = Throttle(10)

    for place in PLACES:
        work_queue.put(place)
    threads = [
        Thread(target=worker, args=(work_queue, result_queue, throttle)) for _ in range(THREAD_POOL_SIZE)
    ]
    for thread in threads:
        thread.start()

    work_queue.join()

    print("until work_queue.join()")
    while not result_queue.empty():
        print(result_queue.get().address)

if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started
    print("main() time consumed:", elapsed)