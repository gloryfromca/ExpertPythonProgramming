import time
from threading import Thread
if __name__ == "__main__":
    from synchronous import PLACES
    from synchronous import fetch_place
else:
    from .synchronous import PLACES
    from .synchronous import fetch_place

def main():
    threads = []
    for place in PLACES:
        thread = Thread(target=fetch_place, args=[place])
        thread.start()
        threads.append(thread)
    while threads:
        threads.pop().join()
    print("until every thread is over!")

if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started
    print(elapsed)



