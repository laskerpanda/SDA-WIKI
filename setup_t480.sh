#!/bin/bash
# Run this ONCE on hermespad (T480) as your regular user (with sudo).
# Sets up mkdocs + systemd service for the SDA wiki.
# Usage: bash ~/Desktop/sda-wiki/setup_t480.sh

set -e

echo "=== Installing python3-pip and venv ==="
sudo apt-get install -y python3-pip python3-venv

echo "=== Installing mkdocs as hermes user ==="
sudo -u hermes python3 -m pip install --user mkdocs mkdocs-material mkdocs-awesome-pages-plugin

echo "=== Creating systemd service ==="
sudo tee /etc/systemd/system/sda-wiki.service > /dev/null <<'EOF'
[Unit]
Description=SDA Commons Wiki (MkDocs)
After=network.target

[Service]
Type=simple
User=hermes
WorkingDirectory=/home/hermes/Desktop/sda-wiki
ExecStart=/home/hermes/.local/bin/mkdocs serve -a 0.0.0.0:5010
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

echo "=== Enabling and starting wiki service ==="
sudo systemctl daemon-reload
sudo systemctl enable sda-wiki
sudo systemctl start sda-wiki

echo ""
echo "Done. Wiki should be live at:"
echo "  http://$(hostname -I | awk '{print $1}'):5010"
echo "  http://hermespad:5010"
