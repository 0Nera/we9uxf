import time


class block:
    def __init__(self) -> None:
        self.last_hash = ""
        self.data = []
        self.timestamp = time.time()
        self.owner = "server"
        self.reward = None