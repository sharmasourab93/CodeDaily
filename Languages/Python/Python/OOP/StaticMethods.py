class Foo(object):
    lol=10
    def __init__(self):
        self.bar = 'barry'

    def too(self):
        return self.bar

    @staticmethod
    def foo(bar):
        print("Static prints "+bar)

Foo.foo(Foo().too()) # doesn't work

"""
Static methods act as separate utility functions without internal reference to self in a class
But they can be invoked using the Class name only
"""