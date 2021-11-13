from abc import ABCMeta, abstractstaticmethod


class ITransport(metaclass=ABCMeta):

    @abstractstaticmethod
    def transport_method():
        """Inheritance method"""
