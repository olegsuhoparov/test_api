from .core import Core
from .checkers import Checkers
from .methods import Methods


class App:

    def __init__(self):
        self.core = Core()
        self.checkers = Checkers()
        self.methods = Methods()
