###########################################################
# Motor
###########################################################
#
# Version: 0.1
# Datum: 2021-11-09 21:11

from logger import Logger
from machine import Pin
import time

class Motor():
    
    FORWAERTS: int = 1
    RUECKWAERTS: int = -1

    __log: Logger = Logger('Motor')

    def __init__(self, id: str, bezeichnung: str, forwaertsPin: int, rueckwaertsPin: int):
        if id is None:
            raise ValueError("id not set")
        
        if bezeichnung is None:
            raise ValueError("bezeichnung not set")

        if forwaertsPin is None:
            raise ValueError("forwaertsPin not set")

        if rueckwaertsPin is None:
            raise ValueError("rueckwaertsPin not set")

        self.id = id
        self.bezeichnung = bezeichnung
        self.forwaertsPin = Pin(forwaertsPin, mode=Pin.OUT, pull=Pin.PULL_DOWN)
        self.rueckwaertsPin = Pin(rueckwaertsPin, mode=Pin.OUT, pull=Pin.PULL_DOWN)
        
        self.forwaertsPin.off()
        self.rueckwaertsPin.off()

        self.__log.info("Motor[{}] erstellt. bezeichnung={}, forwaertsPin={}, rueckwaertsPin={}".format(
            self.id,
            self.bezeichnung,
            forwaertsPin,
            rueckwaertsPin
        ))

    def halt(self):
        self.__log.trace("Motor[{}] stoppen".format(
            self.id
        ))

        self.forwaertsPin.off()
        self.rueckwaertsPin.off()

    def drehen(self, richtung: int, dauer: int):
        if richtung is None:
            raise ValueError("richtung not set")

        if dauer is None:
            raise ValueError("dauer not set")

        self.__log.trace("Motor[{}] drehen. richtung={}, dauer={}ms".format(
            self.id,
            richtung,
            dauer
        ))
        
        if richtung == -1:
            self.forwaertsPin.off()
            self.rueckwaertsPin.on()
            time.sleep_ms(dauer)
            self.rueckwaertsPin.off()
        elif richtung == 0:
            self.forwaertsPin.off()
            self.rueckwaertsPin.off()
            time.sleep_ms(dauer)
        elif richtung == 1:
            self.rueckwaertsPin.off()
            self.forwaertsPin.on()
            time.sleep_ms(dauer)
            self.forwaertsPin.off()
        else:
            raise ValueError("richtung not valid. valid values: -1,0,1")

motoren: Dict = {};

def motoren_laden(motoren_file: str):
    for line in open(motoren_file, 'r').readlines():
        if not line.strip().startswith('#'):
            temp: array = line.strip().split(",")
            
            motorId: str = temp[0].strip()
            motor: Motor = Motor(
                id=temp[0].strip(),
                bezeichnung=temp[1].strip(),
                forwaertsPin=int(temp[2].strip()),
                rueckwaertsPin=int(temp[3].strip()))
            motoren[motorId] = motor

def script_ausfuehren(script_file: str):
    for line in open('scripts/{}'.format(script_file), 'r').readlines():
        if not line.strip().startswith('#'):
            temp: array = line.strip().split(",");
            
            motorId: str = temp[0].strip()
            motor: Motor = motoren[motorId]
            motor.drehen(richtung=int(temp[1].strip()), dauer=int(temp[2].strip()))
