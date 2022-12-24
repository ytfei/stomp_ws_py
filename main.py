import json
import time

from stomp_ws.client import Client
import logging


def print_frame(frame):
    print(json.loads(frame.body))


if __name__ == '__main__':
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

    # open transport
    client = Client("ws://dev-option-websocket.mboxonline.com/optionWebsocket")

    # connect to the endpoint
    client.connect(timeout=0)

    # subscribe channel
    client.subscribe("/topic/mbp/btc", callback=print_frame)

    # send msg to channel
    # client.send("/topic/1", body=json.dumps({'name': 'tom'}))

    time.sleep(30)

    client.disconnect()
