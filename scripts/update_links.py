import os
import re

def find_and_replace_links(content):
    pos = 0
    new_content = ""
    while True:
        # Match [Link]( or [link](
        match = re.search(r'\[[Ll]ink\]\(', content[pos:])
        if not match:
            new_content += content[pos:]
            break

        start_index = pos + match.start()
        new_content += content[pos:start_index]

        url_start = start_index + 7 # len("[Link](")
        paren_count = 1
        i = url_start
        while i < len(content) and paren_count > 0:
            if content[i] == '(':
                paren_count += 1
            elif content[i] == ')':
                paren_count -= 1
            i += 1

        if paren_count == 0:
            url = content[url_start:i-1]
            if url.startswith('http'):
                display_url = url.replace('https://', '').replace('http://', '')
                display_url = display_url.rstrip('/')
                new_content += f'[{display_url}]({url})'
            else:
                new_content += f'[{url}]({url})'
            pos = i
        else:
            new_content += content[start_index:url_start]
            pos = url_start

    return new_content

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = find_and_replace_links(content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    count = 0
    for root, dirs, files in os.walk('.'):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            if file == 'README.md' or file == 'TOOLS.md':
                if update_file(os.path.join(root, file)):
                    count += 1
    print(f"Updated {count} files.")

if __name__ == "__main__":
    main()
