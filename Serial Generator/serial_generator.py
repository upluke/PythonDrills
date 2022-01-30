"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    """ initialize serial number """

    def __init__(self, start=100):
        self.start = start

    """ print and increment serial number """

    def generate(self):
        print(self.start)
        self.start += 1

    """ reset serial number """

    def reset(self):
        self.start = 100


serial = SerialGenerator()
serial.generate()
serial.generate()
serial.generate()
serial.reset()
serial.generate()
serial.generate()
