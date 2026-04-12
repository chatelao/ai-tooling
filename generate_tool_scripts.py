import os
import re

def extract_section_content(content, section_name):
    pattern = rf"## {section_name}.*?\n(.*?)(?=\n## |\Z)"
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return ""

def extract_code_blocks(text):
    blocks = re.findall(r"```(?:bash)?\n(.*?)\n```", text, re.DOTALL)
    if blocks:
        return "\n".join(blocks).strip()
    return ""

def refine_commands(code, tool_path):
    # Strip tool_path from commands
    if tool_path.startswith('./'):
        tool_path = tool_path[2:]

    # Ensure tool_path ends with / for replacement
    if not tool_path.endswith('/'):
        tool_path_esc = re.escape(tool_path + '/')
    else:
        tool_path_esc = re.escape(tool_path)

    code = re.sub(tool_path_esc, '', code)

    # Fix google-cloud-sdk exec -l $SHELL
    code = code.replace('exec -l $SHELL', '# exec -l $SHELL (skipped in automated script)')

    return code

def create_script(filepath, content, script_type, tool_path):
    with open(filepath, 'w') as f:
        f.write("#!/bin/bash\nset -e\ncd \"$(dirname \"$0\")\"\n\n")
        if content:
            code = extract_code_blocks(content)
            if code:
                code = refine_commands(code, tool_path)
                f.write(code + "\n")
            else:
                for line in content.split('\n'):
                    f.write(f"# {line}\n")
        else:
            f.write(f"# No {script_type} instructions found.\n")
    os.chmod(filepath, 0o755)

def main():
    factsheets_dir = 'factsheets'
    for root, dirs, files in os.walk(factsheets_dir):
        if 'README.md' in files:
            tool_name = os.path.basename(root)
            readme_path = os.path.join(root, 'README.md')

            with open(readme_path, 'r') as f:
                content = f.read()

            install_content = extract_section_content(content, "Installation")
            test_content = extract_section_content(content, "Validierung")

            install_script_path = os.path.join(root, f"{tool_name}_install.sh")
            test_script_path = os.path.join(root, f"{tool_name}_run_test.sh")

            create_script(install_script_path, install_content, "installation", root)
            create_script(test_script_path, test_content, "validation", root)

            print(f"Generated scripts for {tool_name}")

if __name__ == "__main__":
    main()
