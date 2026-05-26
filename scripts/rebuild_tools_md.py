import os
import re

def extract_all_info(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def extract_section(header):
        table_match = re.search(rf'^\|\s*{header}\s*\|\s*([^|]+)\s*\|', content, re.MULTILINE)
        if table_match:
            return table_match.group(1).strip()
        return "N/A"

    name_match = re.search(r'^# (?:Factsheet:)?\s*(.*)', content, re.MULTILINE)
    name = name_match.group(1).strip() if name_match else os.path.basename(os.path.dirname(readme_path))

    zweck = ""
    zweck_match = re.search(r'^## Zweck:?\s*(.*)', content, re.MULTILINE)
    if zweck_match:
        val = zweck_match.group(1).strip()
        if val:
            zweck = val
        else:
            lines = content[zweck_match.end():].splitlines()
            for line in lines:
                if line.strip().startswith('##'): break
                if line.strip():
                    zweck = line.strip()
                    break

    latest = extract_section("Latest")
    lts = extract_section("LTS")
    reifegrad = extract_section("Reifegrad")
    schulden = extract_section("Technische Schulden")
    eol = extract_section("Erwartetes Lebensende")
    manual = extract_section("Referenzhandbuch")

    # Gruppe
    gruppe = ""
    grp_match = re.search(r'## Gruppe:?\s*(.*)', content)
    if grp_match:
        gruppe = grp_match.group(1).strip()

    # Installation (minimal version for the table)
    inst = ""
    inst_match = re.search(r'## Installation.*?\n+```(?:bash)?\n(.*?)\n```', content, re.DOTALL)
    if inst_match:
        inst = inst_match.group(1).strip().replace('\n', '; ')
        if len(inst) > 100:
            inst = inst[:97] + "..."

    return {
        'gruppe': gruppe,
        'name': name,
        'latest': latest,
        'lts': lts,
        'zweck': zweck,
        'inst': f"`{inst}`" if inst else "-",
        'manual': manual,
        'reifegrad': reifegrad,
        'schulden': schulden,
        'eol': eol,
        'path': readme_path
    }

def rebuild_tools_md():
    factsheets_root = 'factsheets'
    all_tools = []
    for category in sorted(os.listdir(factsheets_root)):
        cat_path = os.path.join(factsheets_root, category)
        if not os.path.isdir(cat_path): continue
        for tool in sorted(os.listdir(cat_path)):
            tool_path = os.path.join(cat_path, tool)
            readme_path = os.path.join(tool_path, 'README.md')
            if os.path.exists(readme_path):
                all_tools.append(extract_all_info(readme_path))

    header = "# Werkzeuge\n\n"
    table_header = "| Gruppe | Name | Latest | LTS | Zweck | Installationsbefehle | Referenzhandbuch | Reifegrad | Technische Schulden | Erwartetes Lebensende | Factsheet |\n"
    table_sep = "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n"

    rows = []
    for t in all_tools:
        name_link = f"[{t['path']}]({t['path']})"
        row = f"| {t['gruppe']} | {name_link} | {t['latest']} | {t['lts']} | {t['zweck']} | {t['inst']} | {t['manual']} | {t['reifegrad']} | {t['schulden']} | {t['eol']} | {name_link} |\n"
        rows.append(row)

    with open('TOOLS.md', 'w', encoding='utf-8') as f:
        f.write(header)
        f.write(table_header)
        f.write(table_sep)
        f.writelines(rows)
    print(f"Rebuilt TOOLS.md with {len(rows)} entries.")

if __name__ == "__main__":
    rebuild_tools_md()
