# Roadmap für Factsheet-Verbesserungen

Diese Roadmap dokumentiert den aktuellen Stand der Werkzeug-Factsheets und definiert Meilensteine zur Erreichung einer vollständigen und qualitativ hochwertigen Dokumentation gemäß [GEMINI.md](GEMINI.md).

## Status Quo

Nach einer automatisierten Analyse aller Factsheets wurden folgende Defizite identifiziert:

- **Gesamtanzahl Factsheets:** 114 (geschätzt)
- **Factsheets mit Verbesserungsbedarf:** 61
- **Hauptprobleme:**
    - Platzhalter-Beschreibungen (Zweck-Sektion unvollständig)
    - Fehlende oder unzureichende Beispieldaten (weniger als 5 Beispiele)
    - Fehlende Verifizierung (Hashes) oder bekannte Installationsfehler
    - Minimale oder fehlende Validierungsschritte

## Meilensteine

### Meilenstein 1: Inhaltsvervollständigung (Content Completion)
- Ersetzen aller Platzhalter-Texte ("ist ein Werkzeug für") durch präzise Beschreibungen des Werkzeugzwecks.
- Ergänzung fehlender Metadaten wie Wikipedia-Links oder Referenzhandbücher, wo sinnvoll.

### Meilenstein 2: Beispieldatensatz-Erweiterung (Example Richness)
- Sicherstellung, dass jedes Factsheet mindestens 5-10 relevante Beispieldaten im `examples/`-Ordner enthält.
- Dokumentation der Beispiele im jeweiligen `README.md`.

### Meilenstein 3: Installations- und Validierungssicherheit (Deployment Confidence)
- Behebung der in `INSTALL_MISSING.md` und `FIXME.md` gelisteten Probleme.
- Generierung aller fehlenden `.hash.sha256` Verifizierungsdateien nach erfolgreicher Testdurchführung.
- Ausbau minimaler Validierungsschritte zu aussagekräftigen Funktionstests.

## Detaillierte Verbesserungsliste

| Gruppe | Werkzeug | Notwendige Verbesserungen |
| :--- | :--- | :--- |
| Animation | ffmpeg | Few examples (4) |
| Animation | krita | Few examples (4) |
| App-entwicklung | flutter | Few examples (4) |
| App-entwicklung | react-native | Few examples (4) |
| App-entwicklung | spring-boot | No examples |
| Bioinformatik | bkchem | Few examples (2), Installation issue: Log-Fehler: ModuleNotFoundError, Python Traceback |
| Bioinformatik | chemfig | Few examples (1), Installation issue: Log-Fehler: LaTeX Error |
| Cad-3d | freecad | Installation issue: In FIXME.md gelistet, Listed in FIXME.md |
| Cad-3d | mcp-freecad | Few examples (4) |
| Datenbanken | mariadb | Few examples (2), Installation issue: Verifizierungsdatei fehlt (.hash.sha256) |
| Datenbanken | mssql | Few examples (1), Installation issue: Verifizierungsdatei fehlt (.hash.sha256) |
| Datenbanken | oracle | Few examples (1), Installation issue: Verifizierungsdatei fehlt (.hash.sha256) |
| Datenbanken | postgresql | Few examples (2), Installation issue: Verifizierungsdatei fehlt (.hash.sha256) |
| Dokumentation | img2pdf | Few examples (1) |
| Dokumentation | redocly-cli | Few examples (2) |
| Eda | openfpgaloader | Few examples (2) |
| Firmware-analyse | emba | Few examples (4) |
| Firmware-analyse | panda | Installation issue: Verifizierungsdatei fehlt (.hash.sha256) |
| Funktechnik | gnuradio | No examples |
| Funktechnik | gqrx-sdr | No examples |
| Funktechnik | inspectrum | No examples |
| Funktechnik | node-red | No examples |
| Funktechnik | rtl-sdr | No examples |
| Funktechnik | urh | No examples |
| Geodaten | josm | No examples |
| Geodaten | osm2pgsql | No examples |
| Geodaten | osmium-tool | No examples |
| Geodaten | osmosis | No examples |
| Geodaten | postgis | No examples |
| Hardware-simulation | renode | Installation issue: Verifizierungsdatei fehlt (.hash.sha256) |
| Infrastruktur | aws-cli | No examples, Installation issue: Verifizierungsdatei fehlt (.hash.sha256) |
| Infrastruktur | aws-mcp-server | Few examples (4), Installation issue: Verifizierungsdatei fehlt (.hash.sha256) |
| Infrastruktur | azure-cli | No examples, Installation issue: Verifizierungsdatei fehlt (.hash.sha256) |
| Infrastruktur | azure-mcp-server | Few examples (4), Installation issue: Verifizierungsdatei fehlt (.hash.sha256) |
| Infrastruktur | google-cloud-run-mcp | Few examples (4), Installation issue: Verifizierungsdatei fehlt (.hash.sha256) |
| Infrastruktur | google-cloud-sdk | No examples, Installation issue: Verifizierungsdatei fehlt (.hash.sha256) |
| Infrastruktur | vast-ai-sdk | Few examples (4) |
| Infrastruktur | xvfb | Few examples (3) |
| Ki-inferenz | vllm | Few examples (4) |
| Programmierung | ant | No examples |
| Programmierung | composer | No examples |
| Programmierung | java | No examples |
| Programmierung | maven | No examples |
| Programmierung | nodejs | No examples |
| Schnittstellen | graphqurl | Few examples (2) |
| Schnittstellen | grpcurl | Few examples (2) |
| Schnittstellen | openapi-generator | Few examples (4) |
| Schnittstellen | rasqal | Few examples (2) |
| Schnittstellen | sparkql | Few examples (1) |
| Schnittstellen | sparqlwrapper | Few examples (1) |
| Template-engines | blade | No examples |
| Template-engines | ejs | No examples |
| Template-engines | erb | No examples |
| Template-engines | liquid | No examples |
| Template-engines | pug | No examples |
| Template-engines | razor | No examples |
| Template-engines | thymeleaf | No examples |
| Template-engines | twig | No examples |
| Testing | prism | Few examples (2) |
| Testing | schemathesis | Installation issue: Log-Fehler: Fehlgeschlagen |
| Testing | spectral | Few examples (4), Installation issue: Verifizierungsdatei fehlt (.hash.sha256) |
