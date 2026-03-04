#!/usr/bin/env python3

import time
import socket

from zeroconf import Zeroconf, ServiceBrowser, ServiceStateChange


found_self = False


def on_service_change(zeroconf, service_type, name, state_change):
    global found_self
    if state_change is ServiceStateChange.Added:
        info = zeroconf.get_service_info(service_type, name)
        print(f"Found service: {name}")
        if info:
            print(f"  Addresses: {[socket.inet_ntoa(addr) for addr in info.addresses]}")
            print(f"  Port: {info.port}")
            print(f"  Properties: {info.properties}")
            found_self = True
        print()


def main():
    print("=== Verifying Bpod Server Advertisement ===\n")

    global found_self
    found_self = False

    zc = Zeroconf()
    browser = ServiceBrowser(zc, '_bpod._tcp.local.', handlers=[on_service_change])

    print("Listening for 5 seconds...\n")
    time.sleep(5)

    browser.cancel()
    zc.close()

    if found_self:
        print("✓ Server is advertising correctly!")
    else:
        print("✗ Server NOT advertising!")


if __name__ == '__main__':
    main()
