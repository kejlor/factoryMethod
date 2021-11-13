from abc import ABC

from ITransport import ITransport


class SeaTransport(ITransport, ABC):

    def __init__(self):
        self.deliver = "Delivery made by ferry"

    def transport_method(self):
        print(self.deliver)
