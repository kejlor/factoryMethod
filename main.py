from TransportFactory import TransportFactory

if __name__ == "__main__":
    choice = input("Which type of transport do you require?\n")
    transport = TransportFactory.build_transport(choice)
    transport.transport_method()
