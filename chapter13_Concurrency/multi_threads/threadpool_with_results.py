import time
from geopy.geocoders import Nominatim
geolocator = Nominatim()
if __name__ == "__main__":
    from synchronous import PLACES
else:
    from .synchronous import PLACES
from queue import Queue, Empty
from threading import Thread

THREAD_POOL_SIZE = 4
def fetch_place(place):
    return geolocator.geocode(place)

def worker(work_queue, result_queue):
    while not work_queue.empty():
        try:
            item = work_queue.get(block=False)
        except Empty:
            break
        else:
            result_queue.put(fetch_place(item))
            work_queue.task_done()
def main():
    work_queue = Queue()
    result_queue = Queue()
    for place in PLACES:
        work_queue.put(place)
    threads = [
        Thread(target=worker, args=(work_queue, result_queue)) for _ in range(THREAD_POOL_SIZE)
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
