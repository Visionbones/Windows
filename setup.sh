#!/bin/bash
# MCP Kali Server Setup Script for Hostinger VPS
# Run this on your Kali Linux server

echo "🚀 Setting up MCP Kali Server..."
echo "=================================="

# Update system
echo "📋 Updating system packages..."
apt update -y
apt upgrade -y

# Install Python and pip
echo "🐍 Installing Python dependencies..."
apt install python3 python3-pip -y

# Install required Python packages
echo "📦 Installing Python packages..."
pip3 install -r requirements.txt

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p /root/c2builds
mkdir -p /root/output
mkdir -p /root/logs

# Set permissions
echo "🔐 Setting permissions..."
chmod +x kali_server.py
chmod +x dystopia_windows_builder.py

# Create systemd service (optional)
echo "⚙️  Creating systemd service..."
cat > /etc/systemd/system/mcp-kali.service << EOF
[Unit]
Description=MCP Kali Server
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/Windows
ExecStart=/usr/bin/python3 kali_server.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

# Enable but don't start the service yet
systemctl enable mcp-kali

echo ""
echo "✅ Setup complete!"
echo ""
echo "🎯 Next steps:"
echo "1. Start the server: python3 kali_server.py"
echo "2. Or use systemd: systemctl start mcp-kali"
echo "3. Check status: systemctl status mcp-kali"
echo ""
echo "🌐 Server will be available at:"
echo "   - http://localhost:5000"
echo "   - http://YOUR_SERVER_IP:5000"
echo ""
echo "📋 Make sure port 5000 is open in your firewall!"
echo "   ufw allow 5000/tcp"