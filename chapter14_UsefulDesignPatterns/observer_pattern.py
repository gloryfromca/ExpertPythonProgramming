class Event(object):
    _observers = []

    def __init__(self, subject):
        self.subject = subject

    @classmethod
    def register(cls, observer):
        if observer not in cls._observers:
            cls._observers.append(observer)

    @classmethod
    def notify(cls, event):
        for observer in cls._observers:
            observer(event)

class PrintEvent(Event):
    def __repr__(self):
        return "PrintEvent"

def log(event):
    print("I'm processing the event, I will log it:")
    print(" ", event)

class AnotherObserver(object):
    def __call__(self, event):
        print("I'm processing the event, I will print it:")
        print(" ", event)

PrintEvent.register(log)
PrintEvent.register(AnotherObserver())

PrintEvent.notify("Hi, I'm the event!")


















