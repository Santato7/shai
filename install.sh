#!/bin/bash

sudo -v

echo "Installing the shai tool..."

mkdir -p ~/.shai
cd ~/.shai

echo "Downloading the repository..."
git clone https://github.com/santato7/shai.git . > /dev/null 2>&1-

echo "Creating virtual environment..."
python3 -m venv venv > /dev/null 2>&1-

echo "Activating virtual environment..."
source venv/bin/activate > /dev/null 2>&1-

echo "Installing dependencies..."
pip install -r requirements.txt > /dev/null 2>&1-

echo '#!/bin/bash' > shai
echo './venv/bin/python3 main.py "$@"' >> shai

deactivate > /dev/null 2>&1-

chmod +x ./shai > /dev/null 2>&1-
sudo ln -s ~/.shai/shai /usr/local/bin/shai > /dev/null 2>&1-

echo "Installation complete!"