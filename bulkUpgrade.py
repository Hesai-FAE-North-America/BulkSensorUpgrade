#! /usr/bin/python3

import logging
import threading
import time


class UpgradeSensor:

    def __init__(self):
        self.value = 0
        
    def StartUpgrade(self):
        # Use cgi commands to send fw/sw to sensor
    
    def CheckUpgrade(self):
        # use cgi to check upgrade status



class ChangeIP:
    # Change IP address from default to new address specified

class ResetIP:
     # change IP address back to defaule    
     
     
     
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    SensorIP = changeIP()
    UpgradeProcess = UpgradeSensor()
    resetIP = ResetIP()
    sensors = ["201","202","203","204","205","206"]
    logging.info("IP update.)
    SensorIP(sensors)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for index in range(2):
            executor.submit(UpgradeProcess(sensors[index], index)
    resetIP(sensors)