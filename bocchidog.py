from threading import Event, Thread


class BocchidogBark(Exception):
    pass


class Bocchidog(Thread):
    def __init__(self, interval):
        super().__init__()
        self.interval = interval
        self.bocching = True
        self.event = Event()
        self.bark = False

    def run(self):
        while self.bocching:
            self.event.wait(self.interval)
            if not self.event.is_set():
                self.bark = True
                break
            self.event.clear()

    def stop(self):
        self.bocching = False

    def check(self):
        if self.bark:
            self.bark = False
            raise BocchidogBark()
        self.event.set()
