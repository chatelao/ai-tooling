#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive
cd "$(dirname "$0")"

php -r 'if (file_exists("/usr/share/php/Twig/Environment.php")) echo "Twig installed\n";'
