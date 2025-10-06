# 📊 Professional Log Analytics Tool

A beautiful, easy-to-use web application for analyzing log files from ISP and office environments.

**Author:** Rezaul Karim
**Email:** work.rezaul@outlook.com
**Powered By:** REZ LAB

## ✨ Features

- **Beautiful UI/UX**: Professional, minimal design with clean aesthetics
- **Multiple Input Methods**: Upload files or paste logs directly
- **Auto-Detection**: Automatically detects log formats (Apache, Nginx, Syslog, etc.)
- **Real-time Analysis**: Instant insights and visualizations
- **Export Options**: Download results as CSV or JSON
- **Responsive Design**: Works on desktop, tablet, and mobile

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```

### 3. Open in Browser
Navigate to `http://localhost:5000`

## 📖 How to Use

### Option 1: Upload Log File
1. Click on the upload area or drag & drop your log file
2. Supported formats: `.log`, `.txt` (up to 50MB)
3. Click "Analyze Logs" to process

### Option 2: Paste Logs Directly
1. Click "Paste logs directly" button
2. Paste your log content in the text area
3. Click "Analyze Logs" to process

### View Results
- **Summary**: Overview with total entries, error counts, and format detection
- **Top IPs**: Most active IP addresses (for web logs)
- **Status Codes**: HTTP response code distribution (for web logs)
- **Top URLs**: Most accessed endpoints (for web logs)
- **Hostnames**: System hostnames (for syslog)

## 🎨 Design Features

- **Minimal Color Palette**: Professional blue theme with subtle grays
- **Clean Typography**: Inter font for excellent readability
- **Intuitive Icons**: Feather icons for consistent visual language
- **Smooth Animations**: Subtle transitions and loading states
- **Responsive Layout**: Optimized for all screen sizes

## 📊 Supported Log Formats

### 🌐 Web Server Logs
- **Apache HTTP Server**: Standard access logs with IP, timestamp, method, URL, status codes
- **Nginx**: HTTP server logs with similar structure to Apache

### 🔌 Network Device Logs
- **MikroTik RouterOS**: Firewall, DHCP, wireless, and system logs
  - Format: `timestamp interface,facility message`
  - Analysis: Top interfaces, facilities, dropped packets, warnings

- **Cisco IOS**: Router and switch logs with process information
  - Format: `timestamp hostname process_id: message`
  - Analysis: Interface state changes, security events, process monitoring

- **Juniper Junos**: Firewall and routing logs
  - Format: `timestamp hostname process: message`
  - Analysis: Session events, security threats, system processes

### 💻 System Logs
- **Syslog**: Standard system logs with hostname and process tracking
- **Generic**: Custom log formats with basic parsing and analysis

## 🔧 Configuration

The application runs with sensible defaults:
- **Port**: 5000
- **Max File Size**: 50MB
- **Upload Directory**: `uploads/`

## 📁 Project Structure

```
log-analytics/
├── log_analytics_venv/    # Virtual environment
│   ├── Scripts/          # Windows activation scripts
│   └── Lib/              # Python packages
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html       # Clean HTML structure
├── static/               # Separated assets
│   ├── styles.css       # All styling and responsive design
│   └── script.js        # All JavaScript functionality
├── uploads/              # Log files and results
└── README.md            # This file
```

## 🛠️ Development

To modify or extend the application:

1. **Add Log Formats**: Extend the `LogAnalyzer` class in `app.py`
2. **Customize UI**: Modify `templates/index.html`
3. **Add Analytics**: Enhance the analysis functions in `LogAnalyzer`

## 📝 Sample Log Formats

### Apache/Nginx Web Logs
```
192.168.1.100 - - [10/Oct/2023:13:55:36] "GET /api/users HTTP/1.1" 200 1234
192.168.1.101 - - [10/Oct/2023:13:55:37] "POST /api/login HTTP/1.1" 401 567
```

### Syslog
```
Oct 10 13:55:36 server1 sshd[12345]: Failed password for invalid user admin
Oct 10 13:55:37 server2 kernel: [12345.678901] USB device disconnected
```

## 🤝 Support

This tool is designed to be intuitive for everyone - from ISP administrators to office IT staff. The clean interface and automated analysis make log investigation fast and efficient.

---

*Built with ❤️ for ISP and office environments*
