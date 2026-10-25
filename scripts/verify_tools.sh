#!/bin/bash
set -e

mkdir -p log
rm -f log/version.txt

# Ensure test data is available and valid
# For img2pdf
mkdir -p factsheets/dokumentation/img2pdf/examples
for i in {1..5}; do
    /usr/bin/python3 -c "from PIL import Image; img = Image.new('RGB', (100, 100), color = 'red'); img.save('factsheets/dokumentation/img2pdf/examples/test$i.jpg', 'JPEG')"
done

tools=(
    "factsheets/dokumentation/img2pdf/img2pdf"
    "factsheets/schnittstellen/xmllint/xmllint"
    "factsheets/schnittstellen/xmlstarlet/xmlstarlet"
    "factsheets/schnittstellen/xsltproc/xsltproc"
    "factsheets/testing/hurl/hurl"
    "factsheets/schnittstellen/zeep/zeep"
    "factsheets/testing/spectral/spectral"
    "factsheets/testing/prism/prism"
    "factsheets/dokumentation/redocly-cli/redocly-cli"
    "factsheets/dokumentation/apache-fop/apache-fop"
)

for tool_path in "${tools[@]}"; do
    tool_name=$(basename "$tool_path")
    echo "Processing $tool_name..."

    # Install
    ./${tool_path}_install.sh > "log/${tool_name}.install.log" 2>&1 || echo "Install failed for $tool_name" >> "log/${tool_name}.install.log"

    # Test
    if [[ "$tool_name" == "prism" ]]; then
        timeout 10s ./${tool_path}_run_test.sh > "log/${tool_name}.test.log" 2>&1 || true
    else
        ./${tool_path}_run_test.sh > "log/${tool_name}.test.log" 2>&1 || echo "Test failed for $tool_name" >> "log/${tool_name}.test.log"
    fi

    # Version
    case "$tool_name" in
        "img2pdf") img2pdf --version >> log/version.txt 2>&1 || true ;;
        "xmllint") xmllint --version >> log/version.txt 2>&1 || true ;;
        "xmlstarlet") xmlstarlet --version >> log/version.txt 2>&1 || true ;;
        "xsltproc") xsltproc --version >> log/version.txt 2>&1 || true ;;
        "hurl") hurl --version >> log/version.txt 2>&1 || true ;;
        "zeep") /usr/bin/python3 -c "import zeep; print(f'zeep {zeep.__version__}')" >> log/version.txt 2>&1 || true ;;
        "spectral") (cd factsheets/testing/spectral && npx spectral --version) >> log/version.txt 2>&1 || true ;;
        "prism") (cd factsheets/testing/prism && npx prism --version) >> log/version.txt 2>&1 || true ;;
        "redocly-cli") (cd factsheets/dokumentation/redocly-cli && npx redocly --version) >> log/version.txt 2>&1 || true ;;
        "apache-fop") fop -version >> log/version.txt 2>&1 || true ;;
    esac
done

# Cleanup generated test data
/usr/bin/python3 -c "import os; [os.remove(f'factsheets/dokumentation/img2pdf/examples/test{i}.jpg') for i in range(1,6) if os.path.exists(f'factsheets/dokumentation/img2pdf/examples/test{i}.jpg')]"
rm -f factsheets/dokumentation/img2pdf/output.pdf factsheets/dokumentation/apache-fop/examples/test.pdf
