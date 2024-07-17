#!/bin/bash

sudo -v

echo "Installing the shai tool..."

mkdir -p ~/.shai

echo "Downloading the repository..."
git clone https://github.com/santato7/shai.git ~/.shai/ > /dev/null 2>&1

echo "Creating virtual environment..."
python3 -m venv ~/.shai/venv > /dev/null 2>&1

echo "Activating virtual environment..."
source ~/.shai/venv/bin/activate > /dev/null 2>&1

echo "Installing dependencies..."
pip install -r ~/.shai/requirements.txt > /dev/null 2>&1

echo '#!/bin/bash' > ~/.shai/shai
echo '~/.shai/venv/bin/python3 ~/.shai/src/main.py "$@"' >> ~/.shai/shai

deactivate > /dev/null 2>&1

chmod +x ~/.shai/shai > /dev/null 2>&1
sudo ln -s ~/.shai/shai /usr/local/bin/shai > /dev/null 2>&1

echo "Installation complete!"