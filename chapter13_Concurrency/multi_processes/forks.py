import os
pid_list = []
def main():
    pid_list.append(os.getpid())
    child_pid = os.fork()

    # call os.fork() will return 0 in child process.
    if child_pid == 0:
        pid_list.append(os.getpid())
        print("I'm child!")
        print("all the pids i know %s" % pid_list)

    else:
        pid_list.append(os.getpid())
        print("I'm parent!")
        print("the child is pid %s" % child_pid)
        print("all the pids i know %s" % pid_list)
if __name__ == "__main__":
    main()
