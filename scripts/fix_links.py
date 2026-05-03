import os
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find broken links like [url... (text](url... (text))
    # It looks for [prefix (text](prefix (text))
    # pattern = r'\[([^\]]*\([^\]\)]*)\]\(([^\)]*\([^)]*\))\)'

    # Actually, let's re-apply the logic correctly.
    # The previous regex was: r'\[([^\]]+)\]\(([^\)]+)\)'
    # Which stopped at the first ')' it saw in the URL part.

    # Improved regex for markdown links that handles nested parentheses once (common for Wikipedia)
    # This one matches [label](url) where url can contain one level of ()
    markdown_link_regex = r'\[([^\]]+)\]\((https?://[^\s\)]+(?:\([^\s\)]*\)[^\s\)]*)*|[^ \)]+)\)'

    def replace_link(match):
        label = match.group(1)
        url = match.group(2)

        # Check if the label is already a cleaned URL or "Link"
        # If it's a broken cleaned URL, we want to fix it.
        # A broken cleaned URL often looks like it's missing the final ')'
        # compared to the URL.

        if url.startswith('http'):
            display_url = url.replace('https://', '').replace('http://', '')
            display_url = display_url.rstrip('/')
            return f'[{display_url}]({url})'
        else:
            # Internal link
            return f'[{url}]({url})'

    new_content = re.sub(markdown_link_regex, replace_link, content)

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
                if fix_file(os.path.join(root, file)):
                    count += 1
    print(f"Fixed {count} files.")

if __name__ == "__main__":
    main()
