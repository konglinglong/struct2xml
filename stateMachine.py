""" StructContext """

class State(object):
    """Base state."""

    def dump(self):
        """打印状态"""
    def handle(context):
        pass


class IdleState(State):
    def __init__(self):
        self.state = ''
        self.name = "IdleState"
    def handle(self, context):
        print(self.name)


class HandStructMemberState(State):
    def __init__(self):
        self.state = ''
        self.name = "HandStructMemberState"
    def handle(self, context):
        print(self.name)

class StructContext(object):
    """A StructContext."""

    def __init__(self):
        """We have a StructContext"""

        self.stations = {'IdleState':IdleState(), 'HandStructMemberState':HandStructMemberState()}
        self.state = self.stations['IdleState']

    def setstate(self, newstate):
        if newstate in self.stations.keys():
            self.state = self.stations[newstate]
    def request(self, context):
        self.state.handle(context)


def main():
    '''  '''
    context = StructContext()
    context.request('')
    context.setstate('HandStructMemberState')
    context.request('')

if __name__ == '__main__':
    main()
