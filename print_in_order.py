import threading

class Foo:
    def __init__(self):
        self.can_run_second = threading.Semaphore(0) 
        self.can_run_third = threading.Semaphore(0)   

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.can_run_second.release()  

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.can_run_second.acquire() 
        printSecond()
        self.can_run_third.release()   

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.can_run_third.acquire()  
        printThird()
