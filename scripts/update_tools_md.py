import os
import re

def extract_versions(readme_path):
    if not os.path.exists(readme_path):
        return "N/A", "N/A"
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    latest = "N/A"
    lts = "N/A"

    latest_match = re.search(r'\| Latest \| (.*?) \|', content)
    if latest_match:
        latest = latest_match.group(1).strip()

    lts_match = re.search(r'\| LTS \| (.*?) \|', content)
    if lts_match:
        lts = lts_match.group(1).strip()

    return latest, lts

def update_tools_md():
    with open('TOOLS.md', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines: return

    new_lines = []

    for line in lines:
        if line.startswith('| Gruppe | Name | Zweck |'):
            # Update header
            # Find the index of Name and Zweck
            parts = [p.strip() for p in line.split('|')]
            # Expected: ['', 'Gruppe', 'Name', 'Zweck', ...]
            # Insert Latest and LTS after Name (index 2)
            parts.insert(3, "Latest")
            parts.insert(4, "LTS")
            new_line = "| " + " | ".join(p for p in parts if p) + " |\n"
            new_lines.append(new_line)
        elif line.startswith('| :--- | :--- | :--- |'):
            # Update separator
            parts = [p.strip() for p in line.split('|')]
            parts.insert(3, ":---")
            parts.insert(4, ":---")
            new_line = "| " + " | ".join(p for p in parts if p) + " |\n"
            new_lines.append(new_line)
        elif line.startswith('|') and '| Gruppe |' not in line and '| :--- |' not in line:
            # Table row
            parts = line.split('|')
            # parts: ['', ' Gruppe ', ' [Name](path) ', ' Zweck ', ...]

            if len(parts) < 4:
                new_lines.append(line)
                continue

            name_cell = parts[2].strip()
            path_match = re.search(r'\((factsheets/.*?/README\.md)\)', name_cell)
            if path_match:
                factsheet_path = path_match.group(1)
                latest, lts = extract_versions(factsheet_path)
            else:
                latest, lts = "N/A", "N/A"

            # Construct new row: keep everything but insert 2 columns
            new_parts = parts[:3] + [f" {latest} ", f" {lts} "] + parts[3:]
            new_line = "|".join(new_parts)
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    with open('TOOLS.md', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Non-destructively updated TOOLS.md")

if __name__ == "__main__":
    update_tools_md()
