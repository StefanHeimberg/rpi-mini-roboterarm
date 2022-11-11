# rpi-zero-roboterarm
Software zur Steuerung eines KOSMOS Roboterarm mit einem RP2040-Zero

## Konfiguration

- im ```motoren.txt``` file die entsprechenden Motoren des Arms konfigurieren
- scripts aufzeichnen und in eine Datein innerhalb scripts/ Ordner auf dem Raspberry kopieren
- in ```main.py``` das entsprechende script in der gewünschten Reihenfolge ausführen
- freude haben :-)

## Ausgabe

```
1590966 [INFO ] 536897996 Motor                - Motor[M1] erstellt. bezeichnung=Motor 1, forwaertsPin=1, rueckwaertsPin=2
1590971 [INFO ] 536897996 Motor                - Motor[M2] erstellt. bezeichnung=Motor 2, forwaertsPin=5, rueckwaertsPin=6
1590976 [INFO ] 536897996 Motor                - Motor[M3] erstellt. bezeichnung=Motor 3, forwaertsPin=9, rueckwaertsPin=10
1590981 [INFO ] 536897996 Motor                - Motor[M4] erstellt. bezeichnung=Motor 4, forwaertsPin=13, rueckwaertsPin=14
1590986 [INFO ] 536897996 Motor                - Motor[M5] erstellt. bezeichnung=Motor 5, forwaertsPin=17, rueckwaertsPin=18
1590997 [TRACE] 536897996 Motor                - Motor[M1] drehen. richtung=0, dauer=0ms
1591002 [TRACE] 536897996 Motor                - Motor[M2] drehen. richtung=0, dauer=0ms
1591006 [TRACE] 536897996 Motor                - Motor[M3] drehen. richtung=0, dauer=0ms
1591010 [TRACE] 536897996 Motor                - Motor[M4] drehen. richtung=0, dauer=0ms
1591014 [TRACE] 536897996 Motor                - Motor[M5] drehen. richtung=0, dauer=0ms
1591026 [TRACE] 536897996 Motor                - Motor[M1] drehen. richtung=1, dauer=1000ms
1592031 [TRACE] 536897996 Motor                - Motor[M2] drehen. richtung=1, dauer=1000ms
1593035 [TRACE] 536897996 Motor                - Motor[M4] drehen. richtung=1, dauer=3000ms
1596040 [TRACE] 536897996 Motor                - Motor[M5] drehen. richtung=1, dauer=1000ms
1597044 [TRACE] 536897996 Motor                - Motor[M1] drehen. richtung=-1, dauer=1000ms
1598049 [TRACE] 536897996 Motor                - Motor[M2] drehen. richtung=-1, dauer=1000ms
1599053 [TRACE] 536897996 Motor                - Motor[M4] drehen. richtung=-1, dauer=2000ms
1601057 [TRACE] 536897996 Motor                - Motor[M5] drehen. richtung=-1, dauer=1000ms
```
