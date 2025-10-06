# 🔍 Log Analytics Tool

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with ❤️ by REZ LAB](https://img.shields.io/badge/Made%20with%20%E2%9D%A4%EF%B8%8F%20by-REZ%20LAB-red.svg)](https://rezaulkarim.com)

A powerful, web-based log analysis application designed for ISP and office environments. Built with modern web technologies to provide comprehensive log parsing, analysis, and visualization capabilities.

## 🌟 Key Features

### 🔧 **Core Functionality**
- **Multiple Input Methods**: Upload log files or paste content directly
- **Intelligent Format Detection**: Automatic recognition of Apache, Nginx, Syslog, and custom formats
- **Real-time Processing**: Instant analysis with live progress updates
- **Export Capabilities**: Download results in CSV, JSON formats
- **Responsive Interface**: Optimized for desktop, tablet, and mobile devices

### 📊 **Analysis Engine**
- **Statistical Overview**: Entry counts, error rates, format detection
- **IP Intelligence**: Top client IPs and geographic distribution (web logs)
- **HTTP Analytics**: Status code distribution and trends (web logs)
- **URL Analytics**: Most requested endpoints and patterns (web logs)
- **System Monitoring**: Hostname tracking and process analysis (syslog)

### 🎨 **User Experience**
- **Modern UI/UX**: Clean, professional design with intuitive navigation
- **Dark/Light Theme**: Adaptive theming for comfortable viewing
- **Interactive Visualizations**: Charts and graphs for better insights
- **Drag & Drop**: Seamless file upload experience
- **Progress Indicators**: Real-time feedback during processing

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.7 or higher
- Modern web browser
- 100MB+ free disk space for log processing

### Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd log-analytics
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv log_analytics_venv
   source log_analytics_venv/bin/activate  # On Windows: log_analytics_venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Application**
   ```bash
   python app.py
   ```

5. **Access Web Interface**
   ```
   Open: http://localhost:5000
   ```

## 📖 Usage Guide

### File Upload Method
1. **Select Upload Option**: Click the file upload area or drag files directly
2. **File Requirements**: Supports `.log`, `.txt` formats (max 50MB)
3. **Initiate Processing**: Click "Analyze Logs" to begin parsing
4. **View Dashboard**: Explore results across multiple analysis tabs

### Direct Input Method
1. **Select Text Input**: Choose "Paste logs directly" option
2. **Content Entry**: Paste log content in the provided text area
3. **Process Data**: Click "Analyze Logs" for immediate processing
4. **Review Results**: Examine analysis across all available views

### Analysis Results Overview

#### 📈 **Summary Dashboard**
- Total log entries processed
- Error and warning counts
- Detected log format information
- Processing timestamp and metadata

#### 🌐 **Network Intelligence** (Web Logs)
- **Top IP Addresses**: Most active client IPs with request counts
- **Geographic Data**: Country/region distribution (if available)
- **Access Patterns**: Peak usage times and trends

#### 📊 **HTTP Analytics** (Web Logs)
- **Status Code Distribution**: 2xx, 3xx, 4xx, 5xx response breakdown
- **Performance Metrics**: Response time analysis
- **Error Tracking**: Failed request patterns and sources

#### 🔗 **Content Analysis** (Web Logs)
- **Popular Endpoints**: Most requested URLs and resources
- **Content Types**: Distribution of served file types
- **Referral Analysis**: Traffic source breakdown

#### 🖥️ **System Monitoring** (Syslog)
- **Hostname Tracking**: System activity by host
- **Process Analysis**: Application and service monitoring
- **Security Events**: Authentication and access pattern review

## 🎯 Supported Log Formats

### Web Server Logs
- **Apache HTTP Server**: Standard access logs with Common/Combined formats
- **Nginx**: HTTP server logs with configurable formatting
- **IIS**: Microsoft Internet Information Services logs

### Network Infrastructure Logs
- **MikroTik RouterOS**: Firewall, DHCP, wireless, and system logs
- **Cisco IOS/XE**: Router and switch logs with process information
- **Juniper Junos**: Firewall and routing platform logs
- **Ubiquiti UniFi**: Wireless access point and network logs

### System & Security Logs
- **Syslog (RFC 5424)**: Standard system logging protocol
- **Windows Event Logs**: System, security, and application events
- **Linux Audit Logs**: Security and compliance monitoring
- **Custom Formats**: Extensible parser for proprietary formats

## 🔧 Technical Configuration

### Application Settings
```python
# Default Configuration (app.py)
PORT = 5000
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
UPLOAD_FOLDER = 'uploads'
SECRET_KEY = 'your-secret-key-here'  # Change in production
```

### Environment Variables
```bash
export FLASK_ENV=production
export SECRET_KEY=your-production-secret
export PORT=8080
```

## 📁 Project Architecture

```
log-analytics/
├── 📄 app.py                    # Main Flask application
├── 📄 requirements.txt          # Python dependencies
├── 📄 README.md                 # Project documentation
├── 📄 LICENSE                   # MIT license file
├── 📄 .gitignore               # Git ignore patterns
├── 📁 templates/               # HTML templates
│   └── index.html              # Main web interface
├── 📁 static/                  # Static assets
│   ├── styles.css              # Application styling
│   └── script.js               # Frontend functionality
├── 📁 uploads/                 # Log files (auto-generated)
└── 📁 __pycache__/             # Python bytecode (auto-generated)
```

## 🛠️ Development & Extension

### Adding New Log Formats

1. **Extend Parser Class**: Modify `LogAnalyzer` in `app.py`
2. **Define Format Rules**: Add regex patterns and parsing logic
3. **Create Analysis Methods**: Implement format-specific analytics
4. **Update UI**: Add format selection and result visualization

### Customizing the Interface

1. **Template Modification**: Edit `templates/index.html`
2. **Styling Updates**: Modify `static/styles.css`
3. **JavaScript Enhancement**: Extend `static/script.js`
4. **Responsive Design**: Ensure mobile compatibility

### Performance Optimization

- **Memory Management**: Efficient handling of large log files
- **Caching Strategy**: Redis integration for repeated analyses
- **Database Integration**: PostgreSQL for result persistence
- **Async Processing**: Background job processing for large files

## 📝 Log Format Examples

### Apache Access Log
```apache
192.168.1.100 - - [10/Oct/2023:13:55:36 +0000] "GET /api/users HTTP/1.1" 200 1234 "-" "Mozilla/5.0"
192.168.1.101 - - [10/Oct/2023:13:55:37 +0000] "POST /api/login HTTP/1.1" 401 567 "-" "curl/7.68.0"
```

### Syslog Entry
```syslog
Oct 10 13:55:36 server1 sshd[12345]: Failed password for invalid user admin from 192.168.1.100 port 22 ssh2
Oct 10 13:55:37 server2 kernel: [12345.678901] USB device disconnected
```

### Cisco IOS Log
```cisco
*Oct 10 13:55:36.123: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up
*Oct 10 13:55:37.456: %SECURITY-6-IPACCESSLOGP: list 100 denied tcp 192.168.1.100(12345) -> 10.0.0.1(80)
```

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Getting Started
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Contribution Guidelines
- Follow PEP 8 style guidelines for Python code
- Write comprehensive tests for new features
- Update documentation for API changes
- Ensure responsive design for UI modifications
- Maintain backward compatibility when possible

### Areas for Contribution
- **New Log Format Support**: Additional network devices or applications
- **Enhanced Analytics**: New visualization types or analysis methods
- **Performance Improvements**: Memory usage, processing speed
- **UI/UX Enhancements**: Accessibility, mobile optimization
- **Testing**: Unit tests, integration tests, performance benchmarks

## 📋 Changelog

### Version 1.0.0 (Current)
- Initial release with core log analysis functionality
- Support for Apache, Nginx, and Syslog formats
- Modern responsive web interface
- Export capabilities (CSV, JSON)
- Real-time processing with progress indicators

### Planned Features
- [ ] Database integration for result persistence
- [ ] Advanced filtering and search capabilities
- [ ] API endpoints for programmatic access
- [ ] Multi-language support
- [ ] Plugin system for custom log formats

## 🐛 Troubleshooting

### Common Issues

**Application won't start**
- Verify Python 3.7+ is installed
- Check if port 5000 is available
- Ensure all dependencies are installed

**File upload fails**
- Confirm file size is under 50MB limit
- Check upload directory permissions
- Verify file format is supported

**Memory errors with large files**
- Increase system memory allocation
- Process files in smaller chunks
- Consider upgrading hardware

**Slow processing times**
- Enable async processing for large files
- Optimize regex patterns for better performance
- Consider background processing for very large logs

## 📞 Support & Contact

For support, feature requests, or bug reports:

- **Email**: [work.rezaul@outlook.com](mailto:work.rezaul@outlook.com)
- **Issues**: Create a GitHub issue with detailed information
- **Discussions**: Use GitHub Discussions for questions and ideas

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author & Contact

**Author:** Rezaul Karim
**Email:** [work.rezaul@outlook.com](mailto:work.rezaul@outlook.com)
**Organization:** [REZ LAB](https://rezaulkarim.com)

---

<div align="center">

**Built with ❤️ for ISP and office environments**

**[REZ LAB](https://rezaulkarim.com) | [Email](mailto:work.rezaul@outlook.com) | [GitHub](https://github.com)**

</div>
