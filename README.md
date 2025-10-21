# Position Locator Automation

Deze eenvoudige Python-app opent automatisch de pagina [SteamDB Free Packages](https://steamdb.info/freepackages/), wacht 5 seconden, beweegt de muis naar positie `(658, 650)` en klikt, waarna het proces zichzelf beëindigt.

## Vereisten

- Python 3.10 of hoger
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)

Installeer de afhankelijkheid:

```bash
pip install pyautogui
```

## Uitvoeren zonder terminalvenster

Op Windows kun je het script uitvoeren zonder terminalvenster door `pythonw` te gebruiken:

```bash
pythonw main.py
```

Je kunt het script ook bundelen met tools zoals `pyinstaller` (`pyinstaller --onefile --noconsole main.py`) om een uitvoerbaar bestand zonder console te maken.

## Werking

1. Het script opent de doelpagina in de standaardbrowser.
2. Het wacht 5 seconden zodat de pagina kan laden.
3. De muiscursor beweegt naar de coördinaten `(658, 650)` en voert een klik uit.
4. Het proces eindigt automatisch.

> **Let op:** De opgegeven coördinaten zijn afhankelijk van je schermresolutie en schaalinstellingen. Pas `CLICK_COORDS` in `main.py` aan indien nodig.
