Nummerierung immer links nach rechts, oben nach unten.

## Datenformat (senden und empfangen)
```t ID data;```

t: Typ {A,D,P,C} analog, digital, patch, character
ID: Integer, der das Modul angibt
data: Wert

## Indexierung

# Module
## Input
Eingaben am Koffer.

### Potis
Signal kommt bei Veränderung um 10.
Typ: `A`
ID:
* 0-1 Drehpotis
* 2-3 Slider
Wert: 0-4096

### Patchpanel
Signal kommt, wenn ein Kabel aus- oder eingesteckt wird.
Typ: `P`
ID: 
Wert: n m
n: 0-4 (linke Seite, von oben nach unten)
m: 0-4 oder 255 (rechte Seite, von oben nach unten)

### Knöpfe
Typ: `D`
ID: 
* 0 Notaus
* 1-5 Tastenkreuz
* 6-10 Kippschalter
* 11 Kippschalter des Todes (links)
* 12 Schlüsselschalter (links)
* 13 Schlüsselschalter (rechts)
* 14 Kippschalter des Todes (rechts)

### Lüfter
Ein/Aus
Typ: D
ID: 17

## Output
Output sind Dige, die Informationen auf dem Board ausgeben

### LEDs
ID:
* 0-4 Reihe mitte
* 5 Schlüsselschalter-Indikator (links)
* 6 Schlüsselschalter-Indikator (rechts)
* 7-10 Reihe unten

### Piepser
Typ: D
ID:
* 15 Hoch
* 16 Tief
