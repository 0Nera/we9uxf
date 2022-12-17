import time
import hashlib
import numpy as np

from structures.block import block


class blockchain:
    def __init__(self) -> None:
        self.first = block()
        self.last = block()
        self.pow = 0
        self.difficult = 0
        pass