import os
import re

factsheets_root = 'factsheets'
install_missing_path = 'INSTALL_MISSING.md'
fixme_path = 'FIXME.md'
roadmap_file = 'FACTSHEET_ROADMAP.md'

def analyze():
    # Parse INSTALL_MISSING.md
    missing_info = {}
    if os.path.exists(install_missing_path):
        with open(install_missing_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if '|' in line and '`factsheets/' in line:
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 4:
                        # parts[2] is directory, parts[3] is reason
                        dir_path = parts[2].strip('`')
                        reason = parts[3]
                        missing_info[dir_path] = reason

    # Parse FIXME.md
    fixme_info = {}
    if os.path.exists(fixme_path):
        with open(fixme_path, 'r') as f:
            content = f.read()
            # Very simple check for tool names in FIXME
            # Looking for lines like '- **FreeCAD**:'
            tools_in_fixme = re.findall(r'-\s+\*\*([^*]+)\*\*:', content)
            for tool in tools_in_fixme:
                fixme_info[tool.lower()] = 'Listed in FIXME.md'

    roadmap_data = []
    total_factsheets = 0

    for category in os.listdir(factsheets_root):
        cat_path = os.path.join(factsheets_root, category)
        if not os.path.isdir(cat_path):
            continue

        for tool in os.listdir(cat_path):
            tool_path = os.path.join(cat_path, tool)
            if not os.path.isdir(tool_path):
                continue

            readme_path = os.path.join(tool_path, 'README.md')
            if not os.path.exists(readme_path):
                continue

            total_factsheets += 1
            group, tool_name = category, tool

            with open(readme_path, 'r') as f:
                content = f.read()

            issues = []

            # Check Purpose
            if 'ist ein Werkzeug für' in content:
                 lines = content.split('\n')
                 for line in lines:
                    if 'ist ein Werkzeug für' in line:
                        if line.strip().endswith('für'):
                            issues.append('Placeholder purpose')
                        break

            # Check Examples
            examples_dir = os.path.join(tool_path, 'examples')
            example_count = 0
            if os.path.exists(examples_dir):
                example_count = len([f for f in os.listdir(examples_dir) if os.path.isfile(os.path.join(examples_dir, f))])

            if example_count == 0:
                issues.append('No examples')
            elif example_count < 5:
                issues.append(f'Few examples ({example_count})')

            # Check Validation
            if '## Validierung' not in content or len(content.split('## Validierung')[1].strip()) < 10:
                issues.append('Minimal/Missing validation')

            # Check INSTALL_MISSING
            rel_root = os.path.relpath(tool_path, '.')
            if rel_root in missing_info:
                issues.append(f'Installation issue: {missing_info[rel_root]}')

            # Check FIXME
            if tool_name.lower() in fixme_info:
                issues.append(fixme_info[tool_name.lower()])

            if issues:
                roadmap_data.append({'tool': tool_name, 'group': group, 'issues': issues})

    # Sort by group then tool
    roadmap_data.sort(key=lambda x: (x['group'], x['tool']))
    return roadmap_data, total_factsheets

def generate_roadmap(roadmap_data, total_factsheets):
    content = """# Roadmap für Factsheet-Verbesserungen

Diese Roadmap dokumentiert den aktuellen Stand der Werkzeug-Factsheets und definiert Meilensteine zur Erreichung einer vollständigen und qualitativ hochwertigen Dokumentation gemäß [GEMINI.md](GEMINI.md).

## Status Quo

Nach einer automatisierten Analyse aller Factsheets wurden folgende Defizite identifiziert:

- **Gesamtanzahl Factsheets:** """ + str(total_factsheets) + """
- **Factsheets mit Verbesserungsbedarf:** """ + str(len(roadmap_data)) + """
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
"""

    for item in roadmap_data:
        content += f"| {item['group'].capitalize()} | {item['tool']} | {', '.join(item['issues'])} |\n"

    with open(roadmap_file, 'w') as f:
        f.write(content)
    print(f"Roadmap generated at {roadmap_file}")

if __name__ == "__main__":
    data, total = analyze()
    generate_roadmap(data, total)
