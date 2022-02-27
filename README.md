# Plan

 * Frontend: Flask
 * DB: MariaDB
 * Deployment: Docker

Daten:
 * Name
 * Telfonnr.
 * Email
 * Str.
 * Hausnr.
 * PLZ
 * Stadt
 * Land
 * Bundesland
 * Kapazitaet
 * Zeitraum
 * Kinderfreundlich
 * Haustiere

TODO:

[] Static Files bauen
[] Flask Code schreiben
[] SQLAlchemy lernen
[] Dockerimages bauen
[] Server einrichten
[] Adminpanel ??


## Setup

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

## Development server starten

cd rundenudel/
flask run

NOTES:
 - Datenbank URI bitte in Env-Variable "DB_URI" speichern (wird von flask gelesen)
