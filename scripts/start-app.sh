#!/bin/bash

set -e

echo "****************************************"
echo " Starting Back-End Pictures Application"
echo "****************************************"
echo ""

# ------------------------------------------------------------
# 1. Obtener directorio raíz del proyecto
# ------------------------------------------------------------

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_DIR"

echo "Project directory:"
echo "$PROJECT_DIR"
echo ""

# ------------------------------------------------------------
# 2. Comprobar entorno virtual
# ------------------------------------------------------------

if [ ! -f ".venv/Scripts/activate" ]; then
    echo "ERROR: Python virtual environment not found:"
    echo "  $PROJECT_DIR/.venv"
    exit 1
fi

# ------------------------------------------------------------
# 3. Autorizar IP en MongoDB Atlas
# ------------------------------------------------------------

echo "Configuring MongoDB Atlas access..."
echo ""

powershell.exe \
    -NoProfile \
    -ExecutionPolicy Bypass \
    -File "$SCRIPT_DIR/mongodb-atlas-access.ps1"

ATLAS_EXIT_CODE=$?

if [ $ATLAS_EXIT_CODE -ne 0 ]; then
    echo ""
    echo "ERROR: MongoDB Atlas access configuration failed."
    echo "Application will not be started."
    exit $ATLAS_EXIT_CODE
fi

echo ""
echo "MongoDB Atlas access configured successfully."

# ------------------------------------------------------------
# 4. Activar entorno virtual
# ------------------------------------------------------------

echo ""
echo "Activating Python virtual environment..."

source ".venv/Scripts/activate"

echo "Python:"
python --version

# ------------------------------------------------------------
# 5. Arrancar aplicación
# ------------------------------------------------------------

echo ""
echo "Starting application..."
echo "****************************************"
echo ""

flask run