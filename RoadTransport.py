from abc import ABC

from ITransport import ITransport


class RoadTransport(ITransport, ABC):

    def __init__(self):
        self.deliver = "Delivery made by truck"

    def transport_method(self):
        print(self.deliver)
