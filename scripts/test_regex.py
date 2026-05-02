import re

def find_and_replace_links(content):
    pos = 0
    new_content = ""
    while True:
        match = re.search(r'\[[Ll]ink\]\(', content[pos:])
        if not match:
            new_content += content[pos:]
            break

        start_index = pos + match.start()
        new_content += content[pos:start_index]

        url_start = start_index + 7
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

test_str = '| Wikipedia | [Link](https://de.wikipedia.org/wiki/Oracle_(Datenbank)) |'
print(f"Original: '{test_str}'")
fixed = find_and_replace_links(test_str)
print(f"Fixed:    '{fixed}'")
