# Factsheet: Img2pdf

## Gruppe: Dokumentation

## Zweck: Img2pdf ist ein Werkzeug, das Bilddateien verlustfrei und ohne Neukodierung der Pixeldaten in PDF-Dokumente konvertiert.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [github.com/josch/img2pdf](https://github.com/josch/img2pdf) |

## Installation (Ubuntu 24.04)

```bash
sudo apt install img2pdf
```

## Hello World

```bash
img2pdf -o out.pdf in.jpg
```

## Beispieldaten

Im Ordner `examples/` befinden sich verschiedene Skripte zur Nutzung von `img2pdf`:

1.  `convert_single.sh`: Grundlegende Konvertierung eines einzelnen Bildes.
2.  `convert_multiple.sh`: Konvertierung mehrerer Bilder in ein einzelnes PDF.
3.  `set_metadata.sh`: Setzen von PDF-Metadaten während der Konvertierung.
4.  `set_pagesize.sh`: Festlegen einer spezifischen Seitengröße (z.B. A4).
5.  `fit_image.sh`: Einpassen des Bildes in die Seite unter Beibehaltung des Seitenverhältnisses.

## Validierung

Bilder zu PDF konvertieren:

```bash
img2pdf factsheets/dokumentation/img2pdf/examples/*.jpg -o output.pdf
```
