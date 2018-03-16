

class State:

    def next_actions(self):
        raise NotImplementedError("'next_actions' is not implemented in State")

    def apply(self, action):
        raise NotImplementedError("'apply' is not implemented in State")

    def solved(self):
        raise NotImplementedError("'solved' is not implemented in State")

    def consistent(self):
        raise NotImplementedError("'consistent' is not implemented in State")
