from Network import NetworkMgr

__author__ = 'Administrator'


def main():
    global network
    if not network:
        network = NetworkMgr.NetworkMgr()
    network.start_listen()
    while True:
        if not network.is_run:
            break
        network.loop()


if __name__ == "__main__":
    network = None
    main()
