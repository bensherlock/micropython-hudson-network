#! /usr/bin/env python
#
# MicroPython Network Manager for HUDSON Sensor Application.
#
# This file is part of micropython-hudson-network
# https://github.com/bensherlock/micropython-hudson-network

class HudsonSensorNodeNetwork:
    """HUDSON Sensor Node Network"""

    def __init__(self):
        self._nm3_modem = None
        self._wdt = None


    def init_interfaces(self, nm3_modem, wdt):
        """Initialise with the NM3 Modem and WDT"""
        self._nm3_modem = nm3_modem
        self._wdt = wdt



    def handle_packet(self, message_packet):
        """Handle the incoming NM3 packet. """

        # Be sure to call the wdt during longer operations.
        # Feed the watchdog
        # wdt.feed()

        # In here you have full use of the nm3_modem


