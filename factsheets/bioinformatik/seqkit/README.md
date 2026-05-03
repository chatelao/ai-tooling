# Factsheet: Seqkit

## Gruppe: Bioinformatik

## Zweck: SeqKit ist ein schnelles und vielseitiges Kommandozeilenwerkzeug zur Manipulation und Analyse von Sequenzdaten in den Formaten FASTA und FASTQ.

| Eigenschaft | Wert |
| :--- | :--- |
| Reifegrad | Stabil |
| Technische Schulden | Gering |
| Erwartetes Lebensende | Kein EOL bekannt |
| Referenzhandbuch | [bioinf.shenwei.me/seqkit](https://bioinf.shenwei.me/seqkit/) |

## Installation (Ubuntu 24.04)

```bash
sudo apt update
sudo apt install seqkit
```

## Hello World

```bash
seqkit version
```

## Beispieldaten

Die folgenden Beispieldaten befinden sich im Ordner `examples/`:

- `data.fasta`
- `data.fastq`
- `test1.fa`
- `test2.fa`
- `test3.fa`
- `test4.fa`
- `test5.fa`

## Validierung

Verwenden Sie seqkit für Statistiken:

```bash
seqkit stats factsheets/bioinformatik/seqkit/examples/data.fasta
```
