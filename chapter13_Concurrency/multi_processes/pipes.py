from multiprocessing import Process, Pipe

class CustomClass(object):
    pass
def work(connection):
    while True:
        instance = connection.recv()
        if instance:
            print("CHLD: {}".format(instance))
        else:
            return
def main():
    parent_conn, child_conn = Pipe()
    child = Process(target=work, args=(child_conn, ))
    for item in (42, "as", {"sa": "jiang"}, CustomClass(), None):
        parent_conn.send(item)
    child.start()
    child.join()
if __name__ == '__main__':
    main()