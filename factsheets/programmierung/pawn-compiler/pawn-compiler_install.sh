#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

# Abhängigkeiten installieren
sudo apt-get update
sudo apt-get install -y build-essential cmake git

# Repository klonen
if [ ! -d "pawn" ]; then
    git clone https://github.com/compuphase/pawn.git
fi

cd pawn

# Build-Verzeichnis erstellen
mkdir -p build
cd build

# CMake konfigurieren und bauen
cmake ..
make

# Binaries installieren
sudo make install
sudo ldconfig

echo "Pawn compiler installed successfully."
