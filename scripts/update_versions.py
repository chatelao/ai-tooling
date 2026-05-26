import os
import re

# Mapping of tools to their Latest and LTS versions (grounded for early 2025)
version_mapping = {
    "animation/blender": {"Latest": "4.3.2", "LTS": "4.2 LTS"},
    "animation/ffmpeg": {"Latest": "7.1", "LTS": "N/A"},
    "animation/imagemagick": {"Latest": "7.1.1", "LTS": "N/A"},
    "animation/krita": {"Latest": "5.2.6", "LTS": "N/A"},
    "animation/manim": {"Latest": "0.18.1", "LTS": "N/A"},
    "animation/pencil2d": {"Latest": "0.6.6", "LTS": "N/A"},
    "animation/synfig-studio": {"Latest": "1.5.3", "LTS": "N/A"},
    "app-entwicklung/flutter": {"Latest": "3.24.5", "LTS": "N/A"},
    "app-entwicklung/react": {"Latest": "18.3.1", "LTS": "N/A"},
    "app-entwicklung/react-native": {"Latest": "0.76.3", "LTS": "N/A"},
    "app-entwicklung/spring-boot": {"Latest": "3.4.0", "LTS": "3.3.x"},
    "bioinformatik/biopython": {"Latest": "1.84", "LTS": "N/A"},
    "bioinformatik/bkchem": {"Latest": "0.14.0-pre4", "LTS": "N/A"},
    "bioinformatik/chemfig": {"Latest": "1.67", "LTS": "N/A"},
    "bioinformatik/jmol": {"Latest": "16.2.31", "LTS": "N/A"},
    "bioinformatik/pymol": {"Latest": "3.0.0", "LTS": "N/A"},
    "bioinformatik/rdkit": {"Latest": "2024.09.1", "LTS": "N/A"},
    "bioinformatik/seqkit": {"Latest": "2.9.0", "LTS": "N/A"},
    "cad-3d/freecad": {"Latest": "0.21.2", "LTS": "N/A"},
    "cad-3d/ldview": {"Latest": "4.7", "LTS": "N/A"},
    "cad-3d/mcp-freecad": {"Latest": "0.1.0", "LTS": "N/A"},
    "cad-3d/meshlab": {"Latest": "2023.12", "LTS": "N/A"},
    "cad-3d/openscad": {"Latest": "2021.01", "LTS": "N/A"},
    "datenbanken/mariadb": {"Latest": "11.5", "LTS": "11.4 (LTS)"},
    "datenbanken/mssql": {"Latest": "2022", "LTS": "2022"},
    "datenbanken/oracle": {"Latest": "23c", "LTS": "19c"},
    "datenbanken/postgresql": {"Latest": "17.2", "LTS": "N/A"},
    "dokumentation/apache-fop": {"Latest": "2.9", "LTS": "N/A"},
    "dokumentation/img2pdf": {"Latest": "0.5.1", "LTS": "N/A"},
    "dokumentation/plantuml": {"Latest": "1.2024.7", "LTS": "N/A"},
    "dokumentation/redocly-cli": {"Latest": "1.25.0", "LTS": "N/A"},
    "dokumentation/wavedrom": {"Latest": "3.5.0", "LTS": "N/A"},
    "eda/circuitikz": {"Latest": "1.6.7", "LTS": "N/A"},
    "eda/cocotb": {"Latest": "1.9.0", "LTS": "N/A"},
    "eda/kibot": {"Latest": "0.18.0", "LTS": "N/A"},
    "eda/kicad-10-0": {"Latest": "8.0.6", "LTS": "N/A"},
    "eda/openfpgaloader": {"Latest": "0.12.0", "LTS": "N/A"},
    "eda/skidl": {"Latest": "1.2.2", "LTS": "N/A"},
    "eda/yosys": {"Latest": "0.41", "LTS": "N/A"},
    "firmware-analyse/binwalk": {"Latest": "2.4.0", "LTS": "N/A"},
    "firmware-analyse/cve-bin-tool": {"Latest": "3.3", "LTS": "N/A"},
    "firmware-analyse/emba": {"Latest": "1.5.0", "LTS": "N/A"},
    "firmware-analyse/ghidra": {"Latest": "11.2.1", "LTS": "N/A"},
    "firmware-analyse/gnu-binutils": {"Latest": "2.43", "LTS": "N/A"},
    "firmware-analyse/hexdump": {"Latest": "2.40", "LTS": "N/A"},
    "firmware-analyse/panda": {"Latest": "2.2", "LTS": "N/A"},
    "firmware-analyse/radare2": {"Latest": "5.9.8", "LTS": "N/A"},
    "firmware-analyse/yara": {"Latest": "4.5.1", "LTS": "N/A"},
    "funktechnik/gnuradio": {"Latest": "3.10.11", "LTS": "N/A"},
    "funktechnik/gqrx-sdr": {"Latest": "2.17.5", "LTS": "N/A"},
    "funktechnik/inspectrum": {"Latest": "0.3.1", "LTS": "N/A"},
    "funktechnik/node-red": {"Latest": "4.0.5", "LTS": "N/A"},
    "funktechnik/rtl-sdr": {"Latest": "2.0.2", "LTS": "N/A"},
    "funktechnik/urh": {"Latest": "2.9.8", "LTS": "N/A"},
    "geodaten/josm": {"Latest": "19253", "LTS": "N/A"},
    "geodaten/osm2pgsql": {"Latest": "1.11.0", "LTS": "N/A"},
    "geodaten/osmium-tool": {"Latest": "1.16.0", "LTS": "N/A"},
    "geodaten/osmosis": {"Latest": "0.49.2", "LTS": "N/A"},
    "geodaten/postgis": {"Latest": "3.5.0", "LTS": "N/A"},
    "hardware-simulation/renode": {"Latest": "1.15.3", "LTS": "N/A"},
    "infrastruktur/aws-cli": {"Latest": "2.21.0", "LTS": "N/A"},
    "infrastruktur/aws-mcp-server": {"Latest": "1.0.1", "LTS": "N/A"},
    "infrastruktur/azure-cli": {"Latest": "2.66.0", "LTS": "N/A"},
    "infrastruktur/azure-mcp-server": {"Latest": "1.0.1", "LTS": "N/A"},
    "infrastruktur/docker": {"Latest": "27.3.1", "LTS": "N/A"},
    "infrastruktur/docker-compose": {"Latest": "2.29.7", "LTS": "N/A"},
    "infrastruktur/google-cloud-run-mcp": {"Latest": "0.5.0", "LTS": "N/A"},
    "infrastruktur/google-cloud-sdk": {"Latest": "499.0.0", "LTS": "N/A"},
    "infrastruktur/kubernetes": {"Latest": "1.31.2", "LTS": "N/A"},
    "infrastruktur/vast-ai-sdk": {"Latest": "0.1.34", "LTS": "N/A"},
    "infrastruktur/xvfb": {"Latest": "21.1", "LTS": "N/A"},
    "ki-inferenz/ollama": {"Latest": "0.4.1", "LTS": "N/A"},
    "ki-inferenz/vllm": {"Latest": "0.6.3", "LTS": "N/A"},
    "programmierung/ant": {"Latest": "1.10.15", "LTS": "N/A"},
    "programmierung/arduino-cli": {"Latest": "1.1.0", "LTS": "N/A"},
    "programmierung/arm-gdb": {"Latest": "15.1", "LTS": "N/A"},
    "programmierung/blockly": {"Latest": "11.1.1", "LTS": "N/A"},
    "programmierung/composer": {"Latest": "2.8.2", "LTS": "N/A"},
    "programmierung/gnu-toolchain-for-arm": {"Latest": "13.2", "LTS": "N/A"},
    "programmierung/hibernate": {"Latest": "6.6.1", "LTS": "N/A"},
    "programmierung/java": {"Latest": "23", "LTS": "21 (LTS)"},
    "programmierung/maven": {"Latest": "3.9.9", "LTS": "N/A"},
    "programmierung/nodejs": {"Latest": "23.2.0", "LTS": "22.11.0 (LTS)"},
    "programmierung/openocd": {"Latest": "0.12.0", "LTS": "N/A"},
    "programmierung/pawn-compiler": {"Latest": "3.10.10", "LTS": "N/A"},
    "programmierung/pillow": {"Latest": "11.0.0", "LTS": "N/A"},
    "programmierung/platformio-core": {"Latest": "6.1.16", "LTS": "N/A"},
    "schnittstellen/graphqurl": {"Latest": "1.0.3", "LTS": "N/A"},
    "schnittstellen/grpcurl": {"Latest": "1.9.1", "LTS": "N/A"},
    "schnittstellen/openapi-generator": {"Latest": "7.10.0", "LTS": "N/A"},
    "schnittstellen/rasqal": {"Latest": "0.9.33", "LTS": "N/A"},
    "schnittstellen/sparkql": {"Latest": "2.4.0", "LTS": "N/A"},
    "schnittstellen/sparqlwrapper": {"Latest": "2.0.0", "LTS": "N/A"},
    "schnittstellen/xmllint": {"Latest": "2.13.5", "LTS": "N/A"},
    "schnittstellen/xmlstarlet": {"Latest": "1.6.1", "LTS": "N/A"},
    "schnittstellen/xsltproc": {"Latest": "1.1.42", "LTS": "N/A"},
    "schnittstellen/zeep": {"Latest": "4.3.1", "LTS": "N/A"},
    "template-engines/blade": {"Latest": "11.0", "LTS": "N/A"},
    "template-engines/ejs": {"Latest": "3.1.10", "LTS": "N/A"},
    "template-engines/erb": {"Latest": "4.0.4", "LTS": "N/A"},
    "template-engines/handlebars": {"Latest": "4.7.8", "LTS": "N/A"},
    "template-engines/jinja2": {"Latest": "3.1.4", "LTS": "N/A"},
    "template-engines/liquid": {"Latest": "5.5.0", "LTS": "N/A"},
    "template-engines/mustache": {"Latest": "4.2.0", "LTS": "N/A"},
    "template-engines/pug": {"Latest": "3.0.3", "LTS": "N/A"},
    "template-engines/razor": {"Latest": "8.0", "LTS": "N/A"},
    "template-engines/thymeleaf": {"Latest": "3.1.2", "LTS": "N/A"},
    "template-engines/twig": {"Latest": "3.14.0", "LTS": "N/A"},
    "testing/hurl": {"Latest": "5.0.0", "LTS": "N/A"},
    "testing/playwright": {"Latest": "1.49.0", "LTS": "N/A"},
    "testing/prism": {"Latest": "5.10.0", "LTS": "N/A"},
    "testing/schemathesis": {"Latest": "3.38.0", "LTS": "N/A"},
    "testing/spectral": {"Latest": "6.11.1", "LTS": "N/A"},
    "testing/step-ci": {"Latest": "2.5.0", "LTS": "N/A"},
}

def update_factsheets():
    factsheets_root = 'factsheets'
    for category in os.listdir(factsheets_root):
        cat_path = os.path.join(factsheets_root, category)
        if not os.path.isdir(cat_path): continue
        for tool in os.listdir(cat_path):
            tool_path = os.path.join(cat_path, tool)
            if not os.path.isdir(tool_path): continue
            readme_path = os.path.join(tool_path, 'README.md')
            if not os.path.exists(readme_path): continue

            tool_key = f"{category}/{tool}"
            versions = version_mapping.get(tool_key, {"Latest": "N/A", "LTS": "N/A"})

            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Find the metadata table
            table_match = re.search(r'(\| Eigenschaft \| Wert \|\n\| :--- \| :--- \|\n)', content)
            if table_match:
                table_start = table_match.end()
                # Remove any existing Latest/LTS rows to avoid duplicates or misordered rows
                content = re.sub(r'\| Latest \|.*?\|\n', '', content)
                content = re.sub(r'\| LTS \|.*?\|\n', '', content)

                # Re-find the header since we might have removed rows above it (actually they were below)
                table_match = re.search(r'(\| Eigenschaft \| Wert \|\n\| :--- \| :--- \|\n)', content)
                table_start = table_match.end()

                # Insert new rows
                new_rows = f"| Latest | {versions['Latest']} |\n| LTS | {versions['LTS']} |\n"
                content = content[:table_start] + new_rows + content[table_start:]

                with open(readme_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {readme_path}")
            else:
                # No table, try to insert after Zweck
                zweck_match = re.search(r'## Zweck:?.*?\n', content)
                if zweck_match:
                    table = f"\n| Eigenschaft | Wert |\n| :--- | :--- |\n| Latest | {versions['Latest']} |\n| LTS | {versions['LTS']} |\n"
                    content = content[:zweck_match.end()] + table + content[zweck_match.end():]
                    with open(readme_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Created table in {readme_path}")
                else:
                    print(f"No metadata table or Zweck found in {readme_path}")

if __name__ == "__main__":
    update_factsheets()
