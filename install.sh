#!/bin/bash

sudo -v

echo "Installing the shai tool..."

mkdir -p ~/.shai

echo "Downloading the repository..."
git clone https://github.com/santato7/shai.git ~/.shai/ > /dev/null 2>&1

echo "Creating virtual environment..."
python3 -m venv ~/.shai/venv

echo "Activating virtual environment..."
source ~/.shai/venv/bin/activate

echo "Installing dependencies..."
~/.shai/venv/bin/pip install -r ~/.shai/requirements.txt --quiet

echo '#!/bin/bash' > ~/.shai/shai
echo '~/.shai/venv/bin/python3 ~/.shai/src/main.py "$@"' >> ~/.shai/shai

deactivate

chmod +x ~/.shai/shai > /dev/null 2>&1
sudo ln -s ~/.shai/shai /usr/local/bin/shai > /dev/null 2>&1

echo "Installation complete!"
