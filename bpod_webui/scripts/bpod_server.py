#!/usr/bin/env python3

import signal
import time

from bpod_core.bpod import Bpod


def main():
    print("Connecting to Bpod...")
    bpod = Bpod(remote=True)
    print(f"\nBpod '{bpod.name}' online")
    print(f"  Serial: {bpod._serial_number}")
    print(f"  Port: {bpod.port}")
    print(f"  ZMQ REP: {bpod._zmq_service.rep_tcp_addr}")
    print(f"  ZMQ PUB: {bpod._zmq_service.pub_tcp_addr}")
    print("\nPress Ctrl+C to stop.\n")

    running = True

    def signal_handler(sig, frame):
        nonlocal running
        running = False

    signal.signal(signal.SIGINT, signal_handler)

    try:
        while running:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        print("\nShutting down...")
        bpod.close()


if __name__ == '__main__':
    main()
