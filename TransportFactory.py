from RoadTransport import RoadTransport
from SeaTransport import SeaTransport


class TransportFactory:

    @staticmethod
    def build_transport(transport_type):
        if transport_type == "Road":
            return RoadTransport()
        elif transport_type == "Sea":
            return SeaTransport()
        else:
            print("Please input correct transport type")
            exit()
