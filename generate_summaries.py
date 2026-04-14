import os
import re

def extract_info(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract name from # Factsheet: ... or # ...
    name_match = re.search(r'^# (?:Factsheet:)?\s*(.*)', content, re.MULTILINE)

    # Extract purpose from ## Zweck: ... or ## Zweck ...
    zweck = ""
    zweck_header_match = re.search(r'^## Zweck:?\s*(.*)', content, re.MULTILINE)
    if zweck_header_match:
        val = zweck_header_match.group(1).strip()
        if val:
            zweck = val
        else:
            lines = content[zweck_header_match.end():].splitlines()
            for line in lines:
                if line.strip().startswith('##'): break
                if line.strip():
                    zweck = line.strip()
                    break

    name = name_match.group(1).strip() if name_match else os.path.basename(os.path.dirname(filepath))

    def extract_section(header):
        match = re.search(rf'^## {header}:?\s*(.*)', content, re.MULTILINE)
        if not match: return ""
        val = match.group(1).strip()
        if val: return val
        lines = content[match.end():].splitlines()
        for line in lines:
            if line.strip().startswith('##'): break
            if line.strip():
                return line.strip()
        return ""

    reifegrad = extract_section("Reifegrad")
    schulden = extract_section("Technische Schulden")
    eol = extract_section("Erwartetes Lebensende")

    return name, zweck, reifegrad, schulden, eol

def generate_summaries():
    factsheets_dir = 'factsheets'
    groups = {}

    # Traverse factsheets directory
    for group_name in sorted(os.listdir(factsheets_dir)):
        group_path = os.path.join(factsheets_dir, group_name)
        if not os.path.isdir(group_path):
            continue

        tools = []
        for tool_name in sorted(os.listdir(group_path)):
            tool_path = os.path.join(group_path, tool_name)
            readme_path = os.path.join(tool_path, 'README.md')

            if os.path.isfile(readme_path):
                name, zweck, reifegrad, schulden, eol = extract_info(readme_path)
                tools.append({
                    'name': name,
                    'zweck': zweck,
                    'reifegrad': reifegrad,
                    'schulden': schulden,
                    'eol': eol,
                    'path': tool_name
                })

        if tools:
            groups[group_name] = tools

            # Generate group README.md
            group_readme_content = f"# Gruppe: {group_name.capitalize()}\n\n"
            group_readme_content += "## Verfügbare Werkzeuge\n\n"
            group_readme_content += "| Werkzeug | Zweck | Reifegrad | Technische Schulden | Erwartetes Lebensende | Link |\n"
            group_readme_content += "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
            for tool in tools:
                short_zweck = tool['zweck'].replace('|', '\\|')
                if len(short_zweck) > 100:
                    short_zweck = short_zweck[:97] + "..."
                group_readme_content += f"| {tool['name']} | {short_zweck} | {tool['reifegrad']} | {tool['schulden']} | {tool['eol']} | [Link]({tool['path']}/README.md) |\n"

            with open(os.path.join(group_path, 'README.md'), 'w', encoding='utf-8') as f:
                f.write(group_readme_content)

    # Generate factsheets/README.md
    factsheets_readme_content = "# Factsheets\n\n"
    factsheets_readme_content += "## Werkzeuggruppen\n\n"
    factsheets_readme_content += "| Gruppe | Anzahl Werkzeuge | Link |\n"
    factsheets_readme_content += "| :--- | :---: | :--- |\n"
    for group_name in sorted(groups.keys()):
        count = len(groups[group_name])
        factsheets_readme_content += f"| {group_name.capitalize()} | {count} | [Link]({group_name}/README.md) |\n"

    with open(os.path.join(factsheets_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(factsheets_readme_content)

    print("Summaries generated successfully.")

if __name__ == "__main__":
    generate_summaries()
