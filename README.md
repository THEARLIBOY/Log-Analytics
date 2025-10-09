<center>
# 🔍 Log Analytics Tool
</center>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Flask-2.3+-green.svg" alt="Flask">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg" alt="PRs Welcome">
  <img src="https://img.shields.io/badge/Platform-Cross--Platform-orange.svg" alt="Cross-Platform">
</p>

<p align="center">
  <strong>🚀 Professional Log Analysis Tool for ISP & Office Environments</strong>
</p>

<p align="center">
  A powerful, web-based log analysis application designed for ISP and office environments. Built with modern web technologies to provide comprehensive log parsing, analysis, and visualization capabilities.
</p>

</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📖 Usage Guide](#-usage-guide)
- [🎯 Supported Log Formats](#-supported-log-formats)
- [💻 Technology Stack](#-technology-stack)
- [📁 Project Structure](#-project-structure)
- [🔧 Configuration](#-configuration)
- [🚢 Deployment](#-deployment)
- [🤝 Contributing](#-contributing)
- [📋 Changelog](#-changelog)
- [🐛 Troubleshooting](#-troubleshooting)
- [📞 Support](#-support)
- [📜 License](#-license)

---

## ✨ Features

### 🔧 **Core Functionality**
- **📁 Multiple Input Methods**: Upload log files or paste content directly
- **🧠 Intelligent Format Detection**: Automatic recognition of Apache, Nginx, Syslog, and custom formats
- **⚡ Real-time Processing**: Instant analysis with live progress updates
- **📊 Export Capabilities**: Download results in CSV, JSON, TXT formats
- **📱 Responsive Interface**: Optimized for desktop, tablet, and mobile devices

### 📊 **Analysis Engine**
- **📈 Statistical Overview**: Entry counts, error rates, format detection
- **🌐 IP Intelligence**: Top client IPs and geographic distribution (web logs)
- **📊 HTTP Analytics**: Status code distribution and trends (web logs)
- **🔗 URL Analytics**: Most requested endpoints and patterns (web logs)
- **🖥️ System Monitoring**: Hostname tracking and process analysis (syslog)

### 🎨 **User Experience**
- **💫 Modern UI/UX**: Clean, professional design with intuitive navigation
- **🌓 Dark/Light Theme**: Adaptive theming for comfortable viewing
- **📊 Interactive Visualizations**: Charts and graphs for better insights
- **🎯 Drag & Drop**: Seamless file upload experience
- **⏳ Progress Indicators**: Real-time feedback during processing

### 🛡️ **Security & Performance**
- **🔒 Secure File Handling**: Safe processing of uploaded files with size limits
- **🧠 Memory Efficient**: Optimized parsing for large log files (50MB+ support)
- **🛠️ Error Handling**: Comprehensive error reporting and recovery
- **✅ Input Validation**: Robust validation for all input types
- **🌐 Cross-Platform**: Compatible with Windows, macOS, and Linux

---

## 🚀 Quick Start

### 📋 Prerequisites
- **Python 3.7+** 🐍
- **Modern web browser** 🌐
- **100MB+ free disk space** 💾

### ⚡ Installation & Setup

#### 🚀 **Option 1: Quick Start (Recommended)**

```bash
# Clone the repository
git clone <repository-url>
cd log-analytics

# Create virtual environment
python -m venv log_analytics_venv
source log_analytics_venv/bin/activate  # Windows: log_analytics_venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch application
python app.py

# Open browser and navigate to:
# http://localhost:5000
```

#### 🐳 **Option 2: Docker (Alternative)**

```bash
# Build Docker image
docker build -t log-analytics .

# Run container
docker run -p 5000:5000 log-analytics

# Access at: http://localhost:5000
```

#### 📦 **Option 3: Production Deployment**

```bash
# Using Gunicorn (Recommended for production)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Access at: http://your-server:5000
```

---

## 📖 Usage Guide

### 📁 **File Upload Method**
1. **📂 Select Upload Option**: Click the file upload area or drag files directly
2. **📋 File Requirements**: Supports `.log`, `.txt` formats (max 50MB)
3. **🚀 Initiate Processing**: Click "Analyze Logs" to begin parsing
4. **📊 View Dashboard**: Explore results across multiple analysis tabs

### ✏️ **Direct Input Method**
1. **📝 Select Text Input**: Choose "Paste logs directly" option
2. **📋 Content Entry**: Paste log content in the provided text area
3. **⚡ Process Data**: Click "Analyze Logs" for immediate processing
4. **📈 Review Results**: Examine analysis across all available views

### 📊 **Analysis Results Overview**

#### 📈 **Summary Dashboard**
- 📊 Total log entries processed
- 🚨 Error and warning counts
- 🔍 Detected log format information
- ⏰ Processing timestamp and metadata

#### 🌐 **Network Intelligence** (Web Logs)
- **🔝 Top IP Addresses**: Most active client IPs with request counts
- **🗺️ Geographic Data**: Country/region distribution (if available)
- **📈 Access Patterns**: Peak usage times and trends

#### 📊 **HTTP Analytics** (Web Logs)
- **📊 Status Code Distribution**: 2xx, 3xx, 4xx, 5xx response breakdown
- **⚡ Performance Metrics**: Response time analysis
- **🚨 Error Tracking**: Failed request patterns and sources

---

## 🎯 Supported Log Formats

| Format | Description | Use Case |
|--------|-------------|----------|
| **🌐 Apache** | Standard web server access logs | Web traffic analysis |
| **🌐 Nginx** | HTTP server logs with configurable formatting | Load balancer logs |
| **💻 Syslog** | Standard system logging protocol | System monitoring |
| **🛜 MikroTik** | RouterOS firewall and system logs | ISP network devices |
| **🌐 Cisco IOS** | Router and switch logs | Enterprise networking |
| **🛜 Juniper** | Firewall and routing platform logs | Network infrastructure |

### 📝 **Log Format Examples**

#### Apache Access Log
```apache
192.168.1.100 - - [10/Oct/2023:13:55:36 +0000] "GET /api/users HTTP/1.1" 200 1234 "-" "Mozilla/5.0"
```

#### Syslog Entry
```syslog
Oct 10 13:55:36 server1 sshd[12345]: Failed password for invalid user admin from 192.168.1.100 port 22 ssh2
```

---

## 💻 Technology Stack

### **Core Technologies**
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
</p>

### **Key Dependencies**
- **🔗 Flask**: Web framework for Python
- **⚙️ Werkzeug**: WSGI utility library
- **📊 Python Standard Library**: Built-in modules for file handling, regex, etc.

### **Development Tools**
<p align="center">
  <img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" alt="VS Code">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/Virtual_Environment-4B8BBE?style=for-the-badge&logo=python&logoColor=white" alt="Virtual Env">
</p>

---

## 📁 Project Structure

```
log-analytics/
├── 📄 app.py                    # 🚀 Main Flask application
├── 📄 requirements.txt          # 📦 Python dependencies
├── 📄 README.md                 # 📚 Project documentation
├── 📄 LICENSE                   # 📜 MIT license file
├── 📄 .gitignore               # 🚫 Git ignore patterns
├── 📁 templates/               # 🎨 HTML templates
│   └── index.html              # 🌐 Main web interface
├── 📁 static/                  # 🎨 Static assets
│   ├── styles.css              # 💅 Application styling
│   └── script.js               # ⚡ Frontend functionality
├── 📁 uploads/                 # 📁 Log files (auto-generated)
└── 📁 __pycache__/             # 🐍 Python bytecode (auto-generated)
```

---

## 🔧 Configuration

### **Application Settings**
```python
# Default Configuration (app.py)
PORT = 5000
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
UPLOAD_FOLDER = 'uploads'
SECRET_KEY = 'your-secret-key-here'  # Change in production
```

### **Environment Variables**
```bash
export FLASK_ENV=production
export SECRET_KEY=your-production-secret
export PORT=8080
```

---

## 🚢 Deployment

### **🖥️ Development Deployment**
```bash
# Using Flask development server
python app.py

# Access at: http://localhost:5000
```

### **🏭 Production Deployment**

#### **Option A: Gunicorn (Recommended)**
```bash
# Install Gunicorn
pip install gunicorn

# Run with multiple workers
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Access at: http://your-server:5000
```

#### **Option B: Docker Deployment**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

```bash
# Build and run
docker build -t log-analytics .
docker run -p 5000:5000 log-analytics
```

---

## 🤝 Contributing

We welcome contributions from the community! 🌟

### **🚀 Getting Started**
1. 🍴 Fork the repository
2. 🌿 Create a feature branch: `git checkout -b feature/amazing-feature`
3. 💻 Make your changes
4. ✅ Test thoroughly
5. 📤 Submit a pull request

### **📋 Contribution Guidelines**
- 📝 Follow PEP 8 style guidelines for Python code
- 🧪 Write comprehensive tests for new features
- 📚 Update documentation for API changes
- 📱 Ensure responsive design for UI modifications
- 🔄 Maintain backward compatibility when possible

### **🎯 Areas for Contribution**
- 🔧 **New Log Format Support**: Additional network devices or applications
- 📊 **Enhanced Analytics**: New visualization types or analysis methods
- ⚡ **Performance Improvements**: Memory usage, processing speed
- 💫 **UI/UX Enhancements**: Accessibility, mobile optimization
- 🧪 **Testing**: Unit tests, integration tests, performance benchmarks

---

## 📋 Changelog

### **🆕 Version 1.0.0 (Current)**
- ✨ Initial release with core log analysis functionality
- 🌐 Support for Apache, Nginx, and Syslog formats
- 📱 Modern responsive web interface
- 📊 Export capabilities (CSV, JSON, TXT)
- ⚡ Real-time processing with progress indicators

### **🔮 Planned Features**
- [ ] 💾 Database integration for result persistence
- [ ] 🔍 Advanced filtering and search capabilities
- [ ] 🚀 API endpoints for programmatic access
- [ ] 🌍 Multi-language support
- [ ] 🔌 Plugin system for custom log formats

---

## 🐛 Troubleshooting

### **❌ Common Issues**

| Problem | Solution |
|---------|----------|
| **Application won't start** | Verify Python 3.7+ is installed, check if port 5000 is available |
| **File upload fails** | Confirm file size is under 50MB limit, check upload directory permissions |
| **Memory errors with large files** | Increase system memory allocation, process files in smaller chunks |
| **Slow processing times** | Enable async processing for large files, optimize regex patterns |

### **🔧 Getting Help**
1. 📖 Check this README thoroughly
2. 🔍 Search existing GitHub issues
3. 💬 Create a new issue with detailed information
4. 📧 Contact: [work.rezaul@outlook.com](mailto:work.rezaul@outlook.com)

---

## 📞 Support & Contact

### **💬 Get Help**
- **📧 Email**: [work.rezaul@outlook.com](mailto:work.rezaul@outlook.com)
- **🐛 Issues**: [Create a GitHub issue](https://github.com/rezaworks/log-analytics/issues)
- **💭 Discussions**: [GitHub Discussions](https://github.com/rezaworks/log-analytics/discussions)

### **🌟 Show Your Support**
- ⭐ **Star this project** if you find it helpful
- 🐛 **Report bugs** to help improve the tool
- 💡 **Suggest features** for future releases
- 📖 **Share with others** who might benefit

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2023 REZ LAB

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👨‍💻 Author & Contact

<p align="center">
  <strong>Rezaul Karim</strong>
</p>

<p align="center">
  <a href="mailto:work.rezaul@outlook.com">
    <img src="https://img.shields.io/badge/Email-work.rezaul@outlook.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
  <a href="https://www.linkedin.com/in/rezaul-bd/">
    <img src="https://img.shields.io/badge/LinkedIn-REZ%20LAB-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="https://github.com/rezaworks">
    <img src="https://img.shields.io/badge/GitHub-rezaworks-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
</p>

<p align="center">
  <strong>🏢 REZ LAB</strong>
</p>

---

<div align="center">

## 🎯 **About This Project**

<p align="center">
  <strong>Built with ❤️ for ISP and office environments</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg" alt="Production Ready">
  <img src="https://img.shields.io/badge/Maintenance-Active-green.svg" alt="Actively Maintained">
</p>

<p align="center">
  <strong>⭐ If you find this project helpful, please give it a star!</strong>
</p>

<p align="center">
  <a href="#-features">✨ Features</a> •
  <a href="#-quick-start">🚀 Quick Start</a> •
  <a href="#-usage-guide">📖 Usage</a> •
  <a href="#-contributing">🤝 Contribute</a>
</p>

</div>

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

### 🛡️ **Security & Performance**
- **Secure File Handling**: Safe processing of uploaded files with size limits
- **Memory Efficient**: Optimized parsing for large log files (50MB+ support)
- **Error Handling**: Comprehensive error reporting and recovery
- **Input Validation**: Robust validation for all input types
- **Cross-Platform**: Compatible with Windows, macOS, and Linux

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
**Organization:** [REZ LAB](https://www.linkedin.com/in/rezaul-bd/)

## 🎯 Why Choose Log Analytics Tool?

### **Purpose-Built for ISP & Office Environments**
- **Network-Focused**: Specifically designed for ISP networks, office IT infrastructure
- **Multi-Format Support**: Handles the diverse log formats found in real-world deployments
- **Practical Analytics**: Focuses on actionable insights rather than academic metrics
- **Ease of Use**: Designed for IT professionals, not just data scientists

### **Technical Excellence**
- **Lightweight Architecture**: Minimal resource requirements, maximum performance
- **Modern Tech Stack**: Built with current, maintainable technologies
- **Extensible Design**: Easy to add new log formats and analysis features
- **Production Ready**: Includes security, error handling, and scalability considerations

### **Competitive Advantages**
- **No Complex Setup**: Single Python file deployment with minimal dependencies
- **Real-Time Processing**: Instant results without lengthy batch processing
- **Intuitive Interface**: Clean, professional UI that requires no training
- **Export Flexibility**: Multiple format support for integration with existing tools

## 📋 System Requirements

### **Minimum Requirements**
- **Operating System**: Windows 10+, macOS 10.14+, Ubuntu 18.04+, CentOS 7+
- **Processor**: 1 GHz dual-core (64-bit)
- **Memory**: 2 GB RAM (4 GB recommended for large files)
- **Storage**: 100 MB free space + log file size
- **Network**: None required (local processing)

### **Recommended Specifications**
- **Processor**: 2 GHz quad-core or better
- **Memory**: 8 GB RAM for processing 100MB+ log files
- **Storage**: SSD for improved performance
- **Browser**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

### **Performance Scaling**
- **Small Files** (< 1MB): 1 GB RAM sufficient
- **Medium Files** (1-10MB): 2-4 GB RAM recommended
- **Large Files** (10-50MB): 8 GB RAM recommended
- **Very Large Files** (>50MB): Consider file splitting or incremental processing

## 🚢 Deployment Guide

### **Development Deployment**
```bash
# Clone and setup
git clone <repository-url>
cd log-analytics
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run development server
python app.py
```

### **Production Deployment**

#### **Using Gunicorn (Recommended)**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### **Using Docker**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

```bash
docker build -t log-analytics .
docker run -p 5000:5000 log-analytics
```

#### **Using Nginx + Gunicorn**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### **Environment Configuration**
```bash
# Production environment variables
export FLASK_ENV=production
export SECRET_KEY=your-secure-secret-key-here
export PORT=5000
export MAX_FILE_SIZE=52428800  # 50MB in bytes
```

## 🔒 Security Considerations

### **File Upload Security**
- **Size Limits**: Maximum 50MB file uploads to prevent resource exhaustion
- **Format Validation**: Strict file type checking before processing
- **Path Traversal Protection**: Secure file handling prevents directory traversal
- **Temporary File Cleanup**: Automatic cleanup of uploaded files after processing

### **Application Security**
- **Secret Key Management**: Use strong, unique secret keys in production
- **Input Sanitization**: All user inputs are validated and sanitized
- **Error Handling**: Secure error messages that don't leak system information
- **HTTPS Enforcement**: Use reverse proxy (nginx) for SSL/TLS termination

### **Operational Security**
- **Access Control**: Run application with minimal required permissions
- **Log Security**: Avoid logging sensitive information from processed files
- **Update Management**: Keep dependencies updated for security patches
- **Network Security**: Use firewall rules to restrict access to necessary ports

## ❓ Frequently Asked Questions (FAQ)

### **General Questions**
**Q: What types of log files can I analyze?**
A: Web server logs (Apache, Nginx, IIS), network device logs (Cisco, MikroTik, Juniper), system logs (Syslog), and custom formats.

**Q: How large can the log files be?**
A: Up to 50MB per file. For larger files, consider splitting them or using incremental processing.

**Q: Is my data stored permanently?**
A: No, uploaded files are processed in memory and automatically deleted after analysis. No data is persisted.

### **Technical Questions**
**Q: Can I add support for custom log formats?**
A: Yes! The application is designed to be extensible. See the Development section for details.

**Q: Does it work on Windows?**
A: Absolutely! The application is cross-platform and works on Windows, macOS, and Linux.

**Q: Can I integrate this with my existing monitoring tools?**
A: Yes, results can be exported as CSV or JSON for integration with other systems.

### **Troubleshooting Questions**
**Q: The application won't start. What should I check?**
A: Verify Python 3.7+ is installed, port 5000 is available, and all dependencies are installed.

**Q: File uploads fail with large files.**
A: Check available memory and consider increasing system RAM or processing files in smaller chunks.

**Q: Processing seems slow.**
A: Large files require more memory and processing time. Consider upgrading hardware or optimizing regex patterns.

## 🏆 Acknowledgments

### **Technologies & Libraries**
- **[Flask](https://flask.palletsprojects.com/)** - Lightweight Python web framework
- **[Jinja2](https://jinja.palletsprojects.com/)** - Template engine for HTML rendering
- **[Werkzeug](https://werkzeug.palletsprojects.com/)** - WSGI utility library
- **[Python](https://www.python.org/)** - Core programming language

### **Development Tools**
- **[Visual Studio Code](https://code.visualstudio.com/)** - Primary development environment
- **[Git](https://git-scm.com/)** - Version control system
- **[Python Virtual Environments](https://docs.python.org/3/library/venv.html)** - Dependency management

### **Inspiration & References**
- Network administration communities and forums
- ISP and office IT professionals who provided valuable feedback
- Open source log analysis tools that inspired various features

---

<div align="center">

## 🎯 **About This Project**

**Built with ❤️ for ISP and office environments**

**[REZ LAB](https://www.linkedin.com/in/rezaul-bd/) | [Email](mailto:work.rezaul@outlook.com) | [GitHub](https://github.com/rezaworks)**

**⭐ If you find this project helpful, please give it a star!**

</div>
