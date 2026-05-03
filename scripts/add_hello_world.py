import os
import re

# Mapping of tool path to Hello World snippet
# Format: { 'factsheets/category/tool': ('language', 'snippet') }
SNIPPETS = {
    'factsheets/animation/blender': ('python', 'import bpy\nbpy.ops.mesh.primitive_cube_add()'),
    'factsheets/animation/ffmpeg': ('bash', 'ffmpeg -version'),
    'factsheets/animation/imagemagick': ('bash', "convert -size 100x100 xc:white -draw \"text 10,50 'Hello World'\" hello.png"),
    'factsheets/animation/krita': ('bash', 'krita --version'),
    'factsheets/animation/manim': ('python', 'from manim import *\n\nclass HelloWorld(Scene):\n    def construct(self):\n        self.add(Text("Hello World"))'),
    'factsheets/animation/pencil2d': ('bash', 'pencil2d --version'),
    'factsheets/animation/synfig-studio': ('bash', 'synfig --version'),
    'factsheets/app-entwicklung/flutter': ('dart', "import 'package:flutter/material.dart';\n\nvoid main() => runApp(Text('Hello World'));"),
    'factsheets/app-entwicklung/react': ('jsx', "import React from 'react';\nimport ReactDOM from 'react-dom';\n\nReactDOM.render(<h1>Hello, world!</h1>, document.getElementById('root'));"),
    'factsheets/app-entwicklung/react-native': ('jsx', "import React from 'react';\nimport { Text } from 'react-native';\n\nexport default () => <Text>Hello World</Text>;"),
    'factsheets/app-entwicklung/spring-boot': ('java', "@RestController\nclass Hello {\n    @GetMapping(\"/\")\n    String hi() { return \"Hello World\"; }\n}"),
    'factsheets/bioinformatik/biopython': ('python', 'from Bio.Seq import Seq\nprint(Seq("AGT").reverse_complement())'),
    'factsheets/bioinformatik/bkchem': ('bash', 'bkchem --version'),
    'factsheets/bioinformatik/chemfig': ('latex', '\\chemfig{H-O-H}'),
    'factsheets/bioinformatik/jmol': ('bash', 'jmol -n -g 100x100 -J "load $caffeine; write image hello.png"'),
    'factsheets/bioinformatik/pymol': ('python', 'import pymol\npymol.finish_launching()'),
    'factsheets/bioinformatik/rdkit': ('python', "from rdkit import Chem\nprint(Chem.MolToSmiles(Chem.MolFromSmiles('C')))"),
    'factsheets/bioinformatik/seqkit': ('bash', 'seqkit version'),
    'factsheets/cad-3d/freecad': ('python', 'import FreeCAD\nFreeCAD.Console.PrintMessage("Hello World\\n")'),
    'factsheets/cad-3d/ldview': ('bash', 'ldview --version'),
    'factsheets/cad-3d/mcp-freecad': ('bash', 'npx mcp-freecad'),
    'factsheets/cad-3d/meshlab': ('bash', 'meshlabserver -version'),
    'factsheets/cad-3d/openscad': ('openscad', 'cube([10,10,10]);'),
    'factsheets/datenbanken/mariadb': ('sql', "SELECT 'Hello World';"),
    'factsheets/datenbanken/mssql': ('sql', "SELECT 'Hello World';"),
    'factsheets/datenbanken/oracle': ('sql', "SELECT 'Hello World' FROM dual;"),
    'factsheets/datenbanken/postgresql': ('sql', "SELECT 'Hello World';"),
    'factsheets/dokumentation/apache-fop': ('xml', '<fo:block>Hello World</fo:block>'),
    'factsheets/dokumentation/img2pdf': ('bash', 'img2pdf -o out.pdf in.jpg'),
    'factsheets/dokumentation/plantuml': ('plantuml', '@startuml\nAlice -> Bob: Hello World\n@enduml'),
    'factsheets/dokumentation/redocly-cli': ('bash', 'redocly lint openapi.yaml'),
    'factsheets/dokumentation/wavedrom': ('json', '{ "signal": [ { "name": "clk", "wave": "p....." } ] }'),
    'factsheets/eda/circuitikz': ('latex', '\\begin{circuitikz}\n\\draw (0,0) to[R=1<\\ohm>] (2,0);\n\\end{circuitikz}'),
    'factsheets/eda/cocotb': ('python', '@cocotb.test()\nasync def test(dut):\n    dut._log.info("Hello World")'),
    'factsheets/eda/kibot': ('bash', 'kibot --version'),
    'factsheets/eda/kicad-10-0': ('bash', 'kicad --version'),
    'factsheets/eda/openfpgaloader': ('bash', 'openFPGALoader --version'),
    'factsheets/eda/skidl': ('python', 'from skidl import *\nr1 = Part("Device", "R")\nprint("Hello SKiDL")'),
    'factsheets/eda/yosys': ('bash', 'yosys -p "help"'),
    'factsheets/firmware-analyse/binwalk': ('bash', 'binwalk firmware.bin'),
    'factsheets/firmware-analyse/cve-bin-tool': ('bash', 'cve-bin-tool .'),
    'factsheets/firmware-analyse/emba': ('bash', './emba -h'),
    'factsheets/firmware-analyse/ghidra': ('bash', './analyzeHeadless . temp -preScript HelloWorldScript.java'),
    'factsheets/firmware-analyse/gnu-binutils': ('bash', 'objdump -h file.o'),
    'factsheets/firmware-analyse/hexdump': ('bash', 'echo "Hello" | hexdump -C'),
    'factsheets/firmware-analyse/panda': ('bash', 'panda-system-x86_64 --version'),
    'factsheets/firmware-analyse/radare2': ('bash', 'r2 -c "pd 10" /bin/ls'),
    'factsheets/firmware-analyse/yara': ('yara', 'rule hello { condition: true }'),
    'factsheets/funktechnik/gnuradio': ('bash', 'gnuradio-config-info --version'),
    'factsheets/funktechnik/gqrx-sdr': ('bash', 'gqrx --version'),
    'factsheets/funktechnik/inspectrum': ('bash', 'inspectrum --version'),
    'factsheets/funktechnik/node-red': ('bash', 'node-red --version'),
    'factsheets/funktechnik/rtl-sdr': ('bash', 'rtl_test'),
    'factsheets/funktechnik/urh': ('bash', 'urh --version'),
    'factsheets/geodaten/josm': ('bash', 'josm --version'),
    'factsheets/geodaten/osm2pgsql': ('bash', 'osm2pgsql --version'),
    'factsheets/geodaten/osmium-tool': ('bash', 'osmium --version'),
    'factsheets/geodaten/osmosis': ('bash', 'osmosis --help'),
    'factsheets/geodaten/postgis': ('sql', 'SELECT PostGIS_Full_Version();'),
    'factsheets/hardware-simulation/renode': ('bash', 'renode -e "echo \'Hello World\'; quit"'),
    'factsheets/infrastruktur/aws-cli': ('bash', 'aws --version'),
    'factsheets/infrastruktur/aws-mcp-server': ('bash', 'npx @awslabs/aws-api-mcp-server'),
    'factsheets/infrastruktur/azure-cli': ('bash', 'az --version'),
    'factsheets/infrastruktur/azure-mcp-server': ('bash', 'npx @microsoft/azmcp'),
    'factsheets/infrastruktur/docker': ('bash', 'docker run hello-world'),
    'factsheets/infrastruktur/docker-compose': ('bash', 'docker-compose --version'),
    'factsheets/infrastruktur/google-cloud-run-mcp': ('bash', 'npx @google-cloud/cloud-run-mcp'),
    'factsheets/infrastruktur/google-cloud-sdk': ('bash', 'gcloud --version'),
    'factsheets/infrastruktur/kubernetes': ('bash', 'kubectl version'),
    'factsheets/infrastruktur/vast-ai-sdk': ('bash', 'vastai --version'),
    'factsheets/infrastruktur/xvfb': ('bash', 'Xvfb :99 &'),
    'factsheets/ki-inferenz/ollama': ('bash', 'ollama run llama3 "Hello World"'),
    'factsheets/ki-inferenz/vllm': ('bash', 'python3 -m vllm.entrypoints.openai.api_server'),
    'factsheets/programmierung/ant': ('xml', '<project><target name="hello"><echo>Hello World</echo></target></project>'),
    'factsheets/programmierung/arduino-cli': ('bash', 'arduino-cli version'),
    'factsheets/programmierung/arm-gdb': ('bash', 'arm-none-eabi-gdb --version'),
    'factsheets/programmierung/blockly': ('javascript', "Blockly.inject('blocklyDiv', {toolbox: toolbox});"),
    'factsheets/programmierung/composer': ('bash', 'composer --version'),
    'factsheets/programmierung/gnu-toolchain-for-arm': ('bash', 'arm-none-eabi-gcc --version'),
    'factsheets/programmierung/java': ('java', 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello World");\n    }\n}'),
    'factsheets/programmierung/maven': ('bash', 'mvn -version'),
    'factsheets/programmierung/nodejs': ('javascript', 'console.log("Hello World");'),
    'factsheets/programmierung/openocd': ('bash', 'openocd --version'),
    'factsheets/programmierung/pawn-compiler': ('pawn', 'main() {\n    print("Hello World");\n}'),
    'factsheets/programmierung/pillow': ('python', "from PIL import Image\nimg = Image.new('RGB', (100, 100), color='red')\nimg.save('hello.png')"),
    'factsheets/programmierung/platformio-core': ('bash', 'pio --version'),
    'factsheets/schnittstellen/graphqurl': ('bash', 'gq https://countries.trevorblades.com/ --query "{ countries { name } }"'),
    'factsheets/schnittstellen/grpcurl': ('bash', 'grpcurl -plaintext localhost:50051 list'),
    'factsheets/schnittstellen/openapi-generator': ('bash', 'openapi-generator-cli version'),
    'factsheets/schnittstellen/rasqal': ('bash', 'roqet -q -e "SELECT * WHERE { ?s ?p ?o } LIMIT 1"'),
    'factsheets/schnittstellen/sparkql': ('javascript', "const { select } = require('sparkql');\n\nconst query = select('*')\n  .from('<http://dbpedia.org>')\n  .where('?s', '?p', '?o')\n  .limit(1)\n  .build();\nconsole.log(query);"),
    'factsheets/schnittstellen/sparqlwrapper': ('python', 'from SPARQLWrapper import SPARQLWrapper\n\nsparql = SPARQLWrapper("http://dbpedia.org/sparql")\nsparql.setQuery("SELECT * WHERE { ?s ?p ?o } LIMIT 1")\nresults = sparql.query().convert()\nprint(results)'),
    'factsheets/schnittstellen/xmllint': ('bash', 'xmllint --version'),
    'factsheets/schnittstellen/xmlstarlet': ('bash', 'xmlstarlet --version'),
    'factsheets/schnittstellen/xsltproc': ('bash', 'xsltproc --version'),
    'factsheets/schnittstellen/zeep': ('python', "import zeep\nclient = zeep.Client(wsdl='http://www.soapclient.com/xml/soapresponder.wsdl')"),
    'factsheets/template-engines/blade': ('blade', 'Hello, {{ $name }}!'),
    'factsheets/template-engines/ejs': ('ejs', "<%= 'Hello World' %>"),
    'factsheets/template-engines/erb': ('erb', '<%= "Hello World" %>'),
    'factsheets/template-engines/handlebars': ('handlebars', '{{title}}'),
    'factsheets/template-engines/jinja2': ('jinja2', 'Hello {{ name }}!'),
    'factsheets/template-engines/liquid': ('liquid', '{{ "Hello World" | upcase }}'),
    'factsheets/template-engines/mustache': ('mustache', '{{name}}'),
    'factsheets/template-engines/pug': ('pug', 'p Hello World'),
    'factsheets/template-engines/razor': ('razor', '@("Hello World")'),
    'factsheets/template-engines/thymeleaf': ('html', '<p th:text="\'Hello World\'"></p>'),
    'factsheets/template-engines/twig': ('twig', '{{ "Hello World" }}'),
    'factsheets/testing/hurl': ('hurl', 'GET http://localhost:3000\nHTTP 200'),
    'factsheets/testing/playwright': ('javascript', "const { chromium } = require('playwright');\n\n(async () => {\n  const browser = await chromium.launch();\n  const page = await browser.newPage();\n  await page.goto('https://playwright.dev/');\n  console.log(await page.title());\n  await browser.close();\n})();"),
    'factsheets/testing/prism': ('bash', 'prism mock api.yaml'),
    'factsheets/testing/schemathesis': ('bash', 'schemathesis run http://localhost:8080/openapi.json'),
    'factsheets/testing/spectral': ('bash', 'spectral lint openapi.yaml'),
    'factsheets/testing/step-ci': ('bash', 'step-ci run workflow.yml'),
}

def add_hello_world_snippet(tool_path, lang, snippet):
    readme_path = os.path.join(tool_path, 'README.md')
    if not os.path.exists(readme_path):
        print(f"README.md not found in {tool_path}")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if '## Hello World' in content:
        print(f"## Hello World already exists in {readme_path}")
        return

    hello_world_section = f"## Hello World\n\n```{lang}\n{snippet}\n```\n\n"

    # Try to find a good place to insert:
    # 1. Before "Beispiel" or "Beispieldaten"
    # 2. Before "Validierung"
    # 3. At the end

    insertion_points = [r'## Beispiele', r'## Beispieldaten', r'## Validierung']

    inserted = False
    for point in insertion_points:
        match = re.search(f'^{point}', content, re.MULTILINE)
        if match:
            new_content = content[:match.start()] + hello_world_section + content[match.start():]
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            inserted = True
            print(f"Inserted ## Hello World in {readme_path} before {point}")
            break

    if not inserted:
        with open(readme_path, 'a', encoding='utf-8') as f:
            if not content.endswith('\n'):
                f.write('\n\n')
            f.write(hello_world_section)
        print(f"Appended ## Hello World to {readme_path}")

def main():
    for tool_path, (lang, snippet) in SNIPPETS.items():
        add_hello_world_snippet(tool_path, lang, snippet)

if __name__ == "__main__":
    main()
