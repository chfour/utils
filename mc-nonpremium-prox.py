from twisted.internet import reactor
from quarry.net.proxy import DownstreamFactory, Bridge
from quarry.net.auth import OfflineProfile
from quarry.types.uuid import UUID
import logging
import argparse

class MyDownstreamFactory(DownstreamFactory):
    max_players = 2
    motd = f"-> {args.username}@{args.target}:{args.connect_port}"
    display_name = args.username

class MyProfile(OfflineProfile):
    pass

class ExampleBridge(Bridge):
    def make_profile(self):
        return MyProfile(args.username)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=str,
                    help="host to connect to")
    parser.add_argument("username", type=str,
                    help="username to connect as")
    parser.add_argument("-p", "--port", type=int, default=25565,
                    help="port to *listen* on")
    parser.add_argument("-c", "--connect-port", type=int, default=25565,
                    help="port to connect to")
    args = parser.parse_args()

    logging.basicConfig(
        format="[%(asctime)s] %(levelname)s / %(name)s: %(message)s",
        level=logging.DEBUG
    )

    factory = MyDownstreamFactory()
    factory.bridge_class = ExampleBridge
    factory.connect_host = args.target
    factory.connect_port = args.connect_port
    factory.listen("127.0.0.1", args.port)
    logging.info(f"listening on port {args.port}, will connect to {args.target}:{args.connect_port}")
    reactor.run()

if __name__ == "__main__":
    main()
