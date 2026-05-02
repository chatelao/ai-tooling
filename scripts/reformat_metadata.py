import os
import re

def extract_section_content(content, header):
    match = re.search(rf'^## {header}:?\s*(.*)', content, re.MULTILINE)
    if not match:
        return None, None

    val = match.group(1).strip()
    end_pos = match.end()

    if not val:
        lines = content[match.end():].splitlines()
        for line in lines:
            if line.strip().startswith('##'):
                break
            if line.strip():
                val = line.strip()
                end_pos = match.end() + content[match.end():].find(line) + len(line)
                break

    # Find where the next section starts to know what to remove
    next_section = re.search(r'^## ', content[end_pos:], re.MULTILINE)
    if next_section:
        full_end = end_pos + next_section.start()
    else:
        full_end = len(content)

    return val, (match.start(), full_end)

def reformat_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    headers = ["Reifegrad", "Technische Schulden", "Erwartetes Lebensende", "Referenzhandbuch", "Wikipedia"]
    metadata = {}
    ranges = []

    for header in headers:
        val, r = extract_section_content(content, header)
        if val:
            metadata[header] = val
            ranges.append(r)

    if not metadata:
        return

    # Sort ranges in reverse to delete from bottom up
    ranges.sort(key=lambda x: x[0], reverse=True)

    new_content = content
    for start, end in ranges:
        new_content = new_content[:start] + new_content[end:]

    # Clean up multiple newlines
    new_content = re.sub(r'\n{3,}', '\n\n', new_content)

    # Prepare table
    table = "| Eigenschaft | Wert |\n| :--- | :--- |\n"
    for header in headers:
        if header in metadata:
            table += f"| {header} | {metadata[header]} |\n"

    # Insert table after Zweck section if possible, else after Gruppe
    insert_pos = -1
    zweck_match = re.search(r'^## Zweck:?.*', new_content, re.MULTILINE)
    if zweck_match:
        # Find end of Zweck section
        next_sec = re.search(r'^## ', new_content[zweck_match.end():], re.MULTILINE)
        if next_sec:
            insert_pos = zweck_match.end() + next_sec.start()
        else:
            insert_pos = len(new_content)
    else:
        gruppe_match = re.search(r'^## Gruppe:?.*', new_content, re.MULTILINE)
        if gruppe_match:
            insert_pos = gruppe_match.end()

    if insert_pos != -1:
        new_content = new_content[:insert_pos].rstrip() + "\n\n" + table + "\n" + new_content[insert_pos:].lstrip()
    else:
        # Fallback to after the first line (title)
        first_line_end = new_content.find('\n')
        if first_line_end != -1:
            new_content = new_content[:first_line_end+1] + "\n" + table + "\n" + new_content[first_line_end+1:]
        else:
            new_content = table + "\n" + new_content

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    factsheets_dir = 'factsheets'
    for root, dirs, files in os.walk(factsheets_dir):
        if 'README.md' in files:
            # Check if it's a tool README (depth check or just try)
            # Tool READMEs are in factsheets/<group>/<tool>/README.md
            rel_path = os.path.relpath(root, factsheets_dir)
            parts = rel_path.split(os.sep)
            if len(parts) == 2:
                reformat_file(os.path.join(root, 'README.md'))

if __name__ == "__main__":
    main()
