from contextlib import contextmanager
@contextmanager
def list_transaction(alist):
    print("enter context")
    origin_list = list(alist)
    try:
        yield alist
    except Exception as e:
        print("leaving context")
        print("with a error %s" % e)
        alist[:] = origin_list
    finally:
        print("leaving context")
        print("without error")
names = ["zhanghui", ]

with list_transaction(names) as names:
    names.append("hyl")
    names.append("jsy")
    #raising error will make code after yield clause is unexecutable.
    raise RuntimeError("error in with clause")
print(names)

with list_transaction(names) as names:
    names.append("hyl")
    names.append("jsy")
print(names)



