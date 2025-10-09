#!/usr/bin/env python3
"""
Professional Log Analytics Tool
A simple, beautiful web interface for log analysis

Author: Rezaul Karim
Email: work.rezaul@outlook.com
Powered By: REZ LAB
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import json
import datetime
from werkzeug.utils import secure_filename
import re
from collections import Counter, defaultdict
import csv
import io

# Flask application configuration
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Directory for storing uploaded files and analysis results
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # Maximum file size: 50MB
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'  # Secret key for session management

# Create uploads directory if it doesn't exist
# This ensures the application can save uploaded files and analysis results
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

class LogAnalyzer:
    """
    Main log analysis engine that handles parsing, format detection, and analysis of various log types.

    This class supports multiple log formats commonly used in ISP and office environments:
    - Web server logs (Apache, Nginx)
    - Network device logs (MikroTik, Cisco, Juniper)
    - System logs (Syslog)
    - Generic log formats
    """

    def __init__(self):
        """
        Initialize the LogAnalyzer with regex patterns for different log formats.

        Each pattern is designed to capture specific fields from different log types:
        - Web logs: IP, timestamp, method, URL, status code, response size, user agent
        - Network logs: timestamp, hostname/interface, process, message
        - Generic logs: flexible pattern for unknown formats
        """
        self.log_patterns = {
            # Apache/Nginx web server logs
            # Format: IP ident user [timestamp] "method URL protocol" status size "referrer" "user_agent"
            'apache': re.compile(r'^(\S+) (\S+) (\S+) \[([^\]]+)\] "([^"]*)" (\d+) (\S+)(?: "([^"]*)" "([^"]*)")?$'),
            'nginx': re.compile(r'^(\S+) (\S+) (\S+) \[([^\]]+)\] "([^"]*)" (\d+) (\S+)(?: "([^"]*)" "([^"]*)")?$'),

            # Syslog format: Month Day Time Hostname Process: Message
            'syslog': re.compile(r'^(\w+\s+\d+\s+\d+:\d+:\d+)\s+(\S+)\s+([^:]+):\s+(.+)$'),

            # MikroTik RouterOS logs: timestamp interface,facility message
            'mikrotik': re.compile(r'^(\w+\s+\d+\s+\d+:\d+:\d+)\s+(\S+),\s*(\w+)\s+(.+)$'),

            # Cisco IOS logs: timestamp hostname process_id: message
            'cisco': re.compile(r'^(\w+\s+\d+\s+\d+:\d+:\d+)\s+(\S+)\s+(\d+):\s*(.+)$'),

            # Juniper Junos logs: timestamp hostname process: message
            'juniper': re.compile(r'^(\w+\s+\d+\s+\d+:\d+:\d+)\s+(\S+)\s+([^:]+):\s+(.+)$'),

            # Generic fallback pattern for unknown log formats
            'generic': re.compile(r'^(\S+)\s+(\S+)\s+(\S+)\s+(\S+.*)$')
        }

    def detect_log_format(self, sample_lines):
        """
        Automatically detect the log format by testing regex patterns against sample lines.

        Args:
            sample_lines (list): List of log lines to analyze

        Returns:
            str: Detected format name ('apache', 'nginx', 'syslog', 'mikrotik', 'cisco', 'juniper', or 'generic')

        Logic:
        - Tests each regex pattern against the first 10 lines
        - If 50% or more lines match a pattern, that format is selected
        - Falls back to 'generic' if no format matches well
        """
        for fmt, pattern in self.log_patterns.items():
            matches = 0
            # Check first 10 lines to avoid processing entire file during detection
            for line in sample_lines[:10]:
                if pattern.match(line.strip()):
                    matches += 1
            # If 50% of sample lines match, consider it a positive detection
            if matches >= 5:
                return fmt
        return 'generic'

    def parse_logs(self, content, log_format=None):
        """Parse log content and return structured data"""
        lines = content.split('\n')
        if not log_format:
            log_format = self.detect_log_format(lines)

        pattern = self.log_patterns.get(log_format, self.log_patterns['generic'])
        parsed_logs = []

        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue

            match = pattern.match(line)
            if match:
                if log_format in ['apache', 'nginx']:
                    parsed_logs.append({
                        'ip': match.group(1),
                        'timestamp': match.group(4),
                        'method': match.group(5).split()[0] if len(match.group(5).split()) > 0 else '',
                        'url': match.group(5).split()[1] if len(match.group(5).split()) > 1 else '',
                        'status': match.group(6),
                        'size': match.group(7),
                        'user_agent': match.group(8) or '',
                        'line_number': line_num
                    })
                elif log_format == 'mikrotik':
                    parsed_logs.append({
                        'timestamp': match.group(1),
                        'interface': match.group(2),
                        'facility': match.group(3),
                        'message': match.group(4),
                        'line_number': line_num
                    })
                elif log_format == 'cisco':
                    parsed_logs.append({
                        'timestamp': match.group(1),
                        'hostname': match.group(2),
                        'process_id': match.group(3),
                        'message': match.group(4),
                        'line_number': line_num
                    })
                elif log_format == 'juniper':
                    parsed_logs.append({
                        'timestamp': match.group(1),
                        'hostname': match.group(2),
                        'process': match.group(3),
                        'message': match.group(4),
                        'line_number': line_num
                    })
                elif log_format == 'syslog':
                    parsed_logs.append({
                        'timestamp': match.group(1),
                        'hostname': match.group(2),
                        'process': match.group(3),
                        'message': match.group(4),
                        'line_number': line_num
                    })
                else:  # generic
                    parsed_logs.append({
                        'field1': match.group(1),
                        'field2': match.group(2),
                        'field3': match.group(3),
                        'message': match.group(4),
                        'line_number': line_num
                    })

        return parsed_logs, log_format

    def analyze_logs(self, parsed_logs):
        """
        Analyze parsed logs and extract meaningful insights based on log format.

        This method performs format-specific analysis:
        - Web logs: IP analysis, status codes, URL tracking, error counting
        - Network logs: Hostname/interface analysis, process tracking, security events
        - Time-based analysis for all formats

        Args:
            parsed_logs (list): List of parsed log entries with structured data

        Returns:
            dict: Comprehensive analysis results with metrics and insights
        """
        if not parsed_logs:
            return {}

        # Initialize analysis structure with default metrics
        analysis = {
            'total_entries': len(parsed_logs),
            'time_range': '',
            'top_ips': [],
            'status_codes': Counter(),
            'error_count': 0,
            'warning_count': 0,
            'top_urls': Counter(),
            'hourly_distribution': Counter(),
            'daily_distribution': Counter()
        }

        # Determine log type by checking the structure of the first parsed log entry
        first_log = parsed_logs[0] if parsed_logs else {}

        # Web Server Logs Analysis (Apache/Nginx)
        # Identified by presence of 'ip' field in the parsed structure
        if 'ip' in first_log:
            """
            Web server log analysis focuses on:
            - Client IP addresses and request patterns
            - HTTP status codes and error rates
            - Popular URLs and endpoints
            - Traffic timing patterns
            """
            analysis['top_ips'] = Counter(log.get('ip', '') for log in parsed_logs).most_common(10)
            analysis['status_codes'] = Counter(log.get('status', '') for log in parsed_logs)
            analysis['top_urls'] = Counter(log.get('url', '') for log in parsed_logs).most_common(10)

            # Count HTTP errors (4xx client errors, 5xx server errors)
            analysis['error_count'] = sum(1 for log in parsed_logs if log.get('status', '').startswith(('4', '5')))

            # Analyze request timing patterns by hour
            for log in parsed_logs:
                if log.get('timestamp'):
                    try:
                        # Parse Apache timestamp format: DD/MMM/YYYY:HH:MM:SS
                        dt = datetime.datetime.strptime(log['timestamp'], '%d/%b/%Y:%H:%M:%S')
                        analysis['hourly_distribution'][dt.hour] += 1
                    except (ValueError, TypeError):
                        # Skip malformed timestamps
                        pass

        # Syslog Analysis
        # Identified by presence of 'hostname' field (but not 'interface' or 'process_id')
        elif 'hostname' in first_log and 'interface' not in first_log and 'process_id' not in first_log:
            """
            Syslog analysis focuses on:
            - System hostnames generating logs
            - Process activity and system events
            - Error and warning classification
            """
            analysis['top_hostnames'] = Counter(log.get('hostname', '') for log in parsed_logs).most_common(10)
            analysis['top_processes'] = Counter(log.get('process', '') for log in parsed_logs).most_common(10)

            # Classify log messages by severity
            for log in parsed_logs:
                message = log.get('message', '').lower()
                # Count error-level messages
                if any(word in message for word in ['error', 'critical', 'failed', 'failure']):
                    analysis['error_count'] += 1
                # Count warning-level messages
                elif any(word in message for word in ['warning', 'warn']):
                    analysis['warning_count'] += 1

        # MikroTik RouterOS Logs Analysis
        # Identified by presence of 'interface' field
        elif 'interface' in first_log:
            """
            MikroTik log analysis focuses on:
            - Network interface activity and utilization
            - Logging facilities and their activity levels
            - Network-specific events (drops, denials, alerts)
            """
            analysis['top_interfaces'] = Counter(log.get('interface', '') for log in parsed_logs).most_common(10)
            analysis['top_facilities'] = Counter(log.get('facility', '') for log in parsed_logs).most_common(10)

            # Network-specific analysis for MikroTik logs
            for log in parsed_logs:
                message = log.get('message', '').lower()
                # Count dropped packets and denied connections
                if 'drop' in message or 'denied' in message:
                    analysis['error_count'] += 1
                # Count warning and alert messages
                elif any(word in message for word in ['warning', 'warn', 'alert']):
                    analysis['warning_count'] += 1

        # Cisco IOS Logs Analysis
        # Identified by presence of 'process_id' field
        elif 'process_id' in first_log:
            """
            Cisco log analysis focuses on:
            - Network device hostnames and their activity
            - Process IDs and system processes
            - Interface state changes and network events
            - Security-related events and violations
            """
            analysis['top_hostnames'] = Counter(log.get('hostname', '') for log in parsed_logs).most_common(10)
            analysis['top_process_ids'] = Counter(log.get('process_id', '') for log in parsed_logs).most_common(10)

            # Cisco-specific analysis
            for log in parsed_logs:
                message = log.get('message', '').lower()
                # Count interface state changes (link up/down events)
                if 'updown' in message or 'changed state' in message:
                    if 'up' in message:
                        analysis['info_count'] = analysis.get('info_count', 0) + 1
                    elif 'down' in message:
                        analysis['warning_count'] += 1
                # Count security events (access denied, blocked, violations)
                elif any(word in message for word in ['denied', 'blocked', 'violation']):
                    analysis['error_count'] += 1

        # Juniper Junos Logs Analysis
        # Identified by presence of both 'process' and 'hostname' fields
        elif 'process' in first_log and 'hostname' in first_log:
            """
            Juniper log analysis focuses on:
            - Network device hostnames and activity
            - System processes and their behavior
            - Session management events
            - Security threats and attacks
            """
            analysis['top_hostnames'] = Counter(log.get('hostname', '') for log in parsed_logs).most_common(10)
            analysis['top_processes'] = Counter(log.get('process', '') for log in parsed_logs).most_common(10)

            # Juniper-specific analysis
            for log in parsed_logs:
                message = log.get('message', '').lower()
                # Count session events (creation and termination)
                if 'session' in message:
                    if 'create' in message or 'established' in message:
                        analysis['info_count'] = analysis.get('info_count', 0) + 1
                    elif 'close' in message or 'terminated' in message:
                        analysis['info_count'] = analysis.get('info_count', 0) + 1
                # Count security events (attacks, threats, violations)
                elif any(word in message for word in ['attack', 'threat', 'violation', 'intrusion']):
                    analysis['error_count'] += 1

        return analysis

    def apply_filters(self, parsed_logs, filters):
        """Apply filters to parsed logs"""
        if not filters or not parsed_logs:
            return parsed_logs

        filtered_logs = parsed_logs

        # Date/Time filter
        if filters.get('start_date') or filters.get('end_date'):
            try:
                if 'timestamp' in parsed_logs[0]:
                    filtered_logs = []
                    for log in parsed_logs:
                        if log.get('timestamp'):
                            try:
                                log_dt = datetime.datetime.strptime(log['timestamp'], '%d/%b/%Y:%H:%M:%S')
                                if filters.get('start_date'):
                                    start_dt = datetime.datetime.strptime(filters['start_date'], '%Y-%m-%dT%H:%M')
                                    if log_dt < start_dt:
                                        continue
                                if filters.get('end_date'):
                                    end_dt = datetime.datetime.strptime(filters['end_date'], '%Y-%m-%dT%H:%M')
                                    if log_dt > end_dt:
                                        continue
                                filtered_logs.append(log)
                            except:
                                continue
            except:
                pass

        # IP filter
        if filters.get('ip_filter'):
            ip_filter = filters['ip_filter'].lower().strip()
            if ip_filter:
                filtered_logs = [log for log in filtered_logs if ip_filter in log.get('ip', '').lower()]

        # Status code filter
        if filters.get('status_filter'):
            status_filter = filters['status_filter'].strip()
            if status_filter:
                filtered_logs = [log for log in filtered_logs if log.get('status') == status_filter]

        # URL filter
        if filters.get('url_filter'):
            url_filter = filters['url_filter'].lower().strip()
            if url_filter:
                filtered_logs = [log for log in filtered_logs if url_filter in log.get('url', '').lower()]

        # Search text filter
        if filters.get('search_text'):
            search_text = filters['search_text'].lower().strip()
            if search_text:
                filtered_logs = []
                for log in parsed_logs:  # Search in original logs for better matching
                    log_text = str(log).lower()
                    if search_text in log_text:
                        filtered_logs.append(log)

        return filtered_logs

# Global analyzer instance
analyzer = LogAnalyzer()

@app.route('/')
def index():
    """
    Main dashboard route that serves the web interface.

    This route renders the main HTML template with the log analysis interface.
    The template includes file upload, text input, filtering, and results display.

    Returns:
        str: Rendered HTML template for the main dashboard
    """
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Analyze uploaded file or pasted log content.

    This endpoint handles two types of input:
    1. File upload: Users can upload log files (.log, .txt) up to 50MB
    2. Text paste: Users can paste log content directly into a textarea

    The function performs the following steps:
    1. Validates input (file or text content)
    2. Saves uploaded files to the uploads directory
    3. Detects log format automatically
    4. Parses logs using appropriate regex patterns
    5. Performs comprehensive analysis based on log type
    6. Saves results as JSON for export functionality
    7. Returns analysis results as JSON response

    Returns:
        JSON response with analysis results or error message

    Error Handling:
    - Returns error if no content provided
    - Returns error if file is too large (handled by Flask's MAX_CONTENT_LENGTH)
    - Returns error if parsing fails
    - Returns error if analysis encounters exceptions
    """
    try:
        # Check if file was uploaded
        if 'log_file' in request.files and request.files['log_file'].filename:
            # Handle file upload
            file = request.files['log_file']
            filename = secure_filename(file.filename or 'uploaded_file.log')  # Sanitize filename for security
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)  # Save file to uploads directory

            # Read file content with error handling for encoding issues
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        else:
            # Handle pasted content
            content = request.form.get('log_content', '')

        # Validate that content was provided
        if not content.strip():
            return jsonify({'error': 'No log content provided'})

        # Parse and analyze logs using the LogAnalyzer engine
        parsed_logs, detected_format = analyzer.parse_logs(content)
        analysis_results = analyzer.analyze_logs(parsed_logs)

        # Add metadata to results
        analysis_results['detected_format'] = detected_format
        analysis_results['analyzed_at'] = datetime.datetime.now().isoformat()

        # Save analysis results for export functionality
        # Files are named with timestamp for uniqueness
        results_file = f"analysis_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        results_path = os.path.join(app.config['UPLOAD_FOLDER'], results_file)
        with open(results_path, 'w') as f:
            json.dump(analysis_results, f, indent=2)

        return jsonify(analysis_results)

    except Exception as e:
        # Return error information for debugging
        return jsonify({'error': str(e)})

@app.route('/export/<format_type>')
def export_results(format_type):
    """
    Export analysis results in various formats (CSV, TXT, JSON).

    This endpoint retrieves the most recent analysis results and exports them
    in the requested format. The export includes:
    - Summary statistics (total entries, error counts, format detection)
    - Format-specific analysis (IPs, URLs, hostnames, etc.)
    - Time-based distributions
    - Professional formatting with headers and sections

    Args:
        format_type (str): Export format - 'csv', 'txt', or 'json'

    Returns:
        File download response or error message

    Supported Formats:
    - CSV: Structured data with sections for different analysis types
    - TXT: Human-readable text report with ASCII formatting
    - JSON: Enhanced JSON structure with metadata and organized sections
    """
    try:
        # Get latest analysis results file
        results_files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if f.startswith('analysis_')]
        if not results_files:
            return "No analysis results found"

        # Find most recently created results file
        latest_file = max(results_files, key=lambda f: os.path.getctime(os.path.join(app.config['UPLOAD_FOLDER'], f)))
        results_path = os.path.join(app.config['UPLOAD_FOLDER'], latest_file)

        # Load analysis results from JSON file
        with open(results_path, 'r') as f:
            results = json.load(f)

        if format_type == 'csv':
            output = io.StringIO()
            writer = csv.writer(output)

            # Write header
            writer.writerow(['LOG ANALYTICS REPORT'])
            writer.writerow(['Generated on', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
            writer.writerow([])

            # Analysis Summary Section
            writer.writerow(['ANALYSIS SUMMARY'])
            writer.writerow(['================'])
            writer.writerow(['Metric', 'Value'])
            writer.writerow(['Total Log Entries', results.get('total_entries', 0)])
            writer.writerow(['Error Count', results.get('error_count', 0)])
            writer.writerow(['Warning Count', results.get('warning_count', 0)])
            writer.writerow(['Log Format Detected', results.get('detected_format', 'Unknown')])

            # Add network-specific metrics if available
            if 'info_count' in results:
                writer.writerow(['Info Events', results.get('info_count', 0)])

            writer.writerow([])

            # Web Server Logs Section
            if 'top_ips' in results and results['top_ips']:
                writer.writerow(['WEB SERVER ANALYSIS'])
                writer.writerow(['=================='])
                writer.writerow(['Top IP Addresses', 'Request Count'])
                writer.writerow(['IP Address', 'Count'])
                for ip, count in results['top_ips']:
                    writer.writerow([ip, count])
                writer.writerow([])

            if 'status_codes' in results and results['status_codes']:
                writer.writerow(['HTTP Status Codes', 'Count'])
                writer.writerow(['Status Code', 'Count'])
                # Convert dict to sorted items (JSON doesn't preserve Counter objects)
                status_items = sorted(results['status_codes'].items(), key=lambda x: x[1], reverse=True)
                for status, count in status_items:
                    writer.writerow([status, count])
                writer.writerow([])

            if 'top_urls' in results and results['top_urls']:
                writer.writerow(['Top URLs/Endpoints', 'Access Count'])
                writer.writerow(['URL', 'Count'])
                for url, count in results['top_urls']:
                    writer.writerow([url, count])
                writer.writerow([])

            # Network Device Logs Section
            if 'top_interfaces' in results and results['top_interfaces']:
                writer.writerow(['NETWORK DEVICE ANALYSIS'])
                writer.writerow(['======================'])
                writer.writerow(['Top Network Interfaces', 'Activity Count'])
                writer.writerow(['Interface', 'Count'])
                for interface, count in results['top_interfaces']:
                    writer.writerow([interface, count])
                writer.writerow([])

            if 'top_facilities' in results and results['top_facilities']:
                writer.writerow(['Logging Facilities', 'Event Count'])
                writer.writerow(['Facility', 'Count'])
                for facility, count in results['top_facilities']:
                    writer.writerow([facility, count])
                writer.writerow([])

            if 'top_hostnames' in results and results['top_hostnames']:
                writer.writerow(['Device Hostnames', 'Log Count'])
                writer.writerow(['Hostname', 'Count'])
                for hostname, count in results['top_hostnames']:
                    writer.writerow([hostname, count])
                writer.writerow([])

            if 'top_processes' in results and results['top_processes']:
                writer.writerow(['System Processes', 'Activity Count'])
                writer.writerow(['Process', 'Count'])
                for process, count in results['top_processes']:
                    writer.writerow([process, count])
                writer.writerow([])

            if 'top_process_ids' in results and results['top_process_ids']:
                writer.writerow(['Cisco Process IDs', 'Event Count'])
                writer.writerow(['Process ID', 'Count'])
                for process_id, count in results['top_process_ids']:
                    writer.writerow([process_id, count])
                writer.writerow([])

            # Time Distribution (if available)
            if 'hourly_distribution' in results and results['hourly_distribution']:
                writer.writerow(['HOURLY DISTRIBUTION'])
                writer.writerow(['=================='])
                writer.writerow(['Hour', 'Log Count'])
                for hour in range(24):
                    count = results['hourly_distribution'].get(hour, 0)
                    if count > 0:
                        writer.writerow([f'{hour:02d}:00', count])
                writer.writerow([])

            # Footer
            writer.writerow(['END OF REPORT'])
            writer.writerow(['============='])
            writer.writerow(['Report generated by Log Analytics Tool'])

            return output.getvalue(), 200, {
                'Content-Type': 'text/csv',
                'Content-Disposition': f'attachment; filename="log_analysis_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.csv"'
            }

        elif format_type == 'txt':
            # Create plain text report
            output = io.StringIO()

            # Header
            output.write("=" * 60 + "\n")
            output.write("LOG ANALYTICS REPORT\n")
            output.write("=" * 60 + "\n")
            output.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            output.write(f"Total Log Entries: {results.get('total_entries', 0)}\n")
            output.write(f"Log Format Detected: {results.get('detected_format', 'Unknown').upper()}\n")
            output.write("\n")

            # Analysis Summary
            output.write("-" * 40 + "\n")
            output.write("ANALYSIS SUMMARY\n")
            output.write("-" * 40 + "\n")
            output.write(f"Total Entries: {results.get('total_entries', 0)}\n")
            output.write(f"Error Count: {results.get('error_count', 0)}\n")
            output.write(f"Warning Count: {results.get('warning_count', 0)}\n")
            if 'info_count' in results:
                output.write(f"Info Events: {results.get('info_count', 0)}\n")
            output.write("\n")

            # Web Server Logs Section
            if 'top_ips' in results and results['top_ips']:
                output.write("-" * 40 + "\n")
                output.write("WEB SERVER ANALYSIS\n")
                output.write("-" * 40 + "\n")
                output.write("Top IP Addresses (Request Count):\n")
                output.write("-" * 30 + "\n")
                for ip, count in results['top_ips']:
                    output.write(f"{ip:<20} {count:>6}\n")
                output.write("\n")

            if 'status_codes' in results and results['status_codes']:
                output.write("HTTP Status Codes (Count):\n")
                output.write("-" * 25 + "\n")
                status_items = sorted(results['status_codes'].items(), key=lambda x: x[1], reverse=True)
                for status, count in status_items:
                    output.write(f"{status:<8} {count:>6}\n")
                output.write("\n")

            if 'top_urls' in results and results['top_urls']:
                output.write("Top URLs/Endpoints (Access Count):\n")
                output.write("-" * 35 + "\n")
                for url, count in results['top_urls']:
                    output.write(f"{url:<30} {count:>6}\n")
                output.write("\n")

            # Network Device Logs Section
            if 'top_interfaces' in results and results['top_interfaces']:
                output.write("-" * 40 + "\n")
                output.write("NETWORK DEVICE ANALYSIS\n")
                output.write("-" * 40 + "\n")
                output.write("Top Network Interfaces (Activity Count):\n")
                output.write("-" * 40 + "\n")
                for interface, count in results['top_interfaces']:
                    output.write(f"{interface:<25} {count:>6}\n")
                output.write("\n")

            if 'top_facilities' in results and results['top_facilities']:
                output.write("Logging Facilities (Event Count):\n")
                output.write("-" * 32 + "\n")
                for facility, count in results['top_facilities']:
                    output.write(f"{facility:<20} {count:>6}\n")
                output.write("\n")

            if 'top_hostnames' in results and results['top_hostnames']:
                output.write("Device Hostnames (Log Count):\n")
                output.write("-" * 28 + "\n")
                for hostname, count in results['top_hostnames']:
                    output.write(f"{hostname:<20} {count:>6}\n")
                output.write("\n")

            if 'top_processes' in results and results['top_processes']:
                output.write("System Processes (Activity Count):\n")
                output.write("-" * 33 + "\n")
                for process, count in results['top_processes']:
                    output.write(f"{process:<20} {count:>6}\n")
                output.write("\n")

            if 'top_process_ids' in results and results['top_process_ids']:
                output.write("Cisco Process IDs (Event Count):\n")
                output.write("-" * 31 + "\n")
                for process_id, count in results['top_process_ids']:
                    output.write(f"{process_id:<15} {count:>6}\n")
                output.write("\n")

            # Time Distribution (if available)
            if 'hourly_distribution' in results and results['hourly_distribution']:
                output.write("-" * 40 + "\n")
                output.write("HOURLY DISTRIBUTION\n")
                output.write("-" * 40 + "\n")
                output.write("Hour     Log Count\n")
                output.write("-" * 18 + "\n")
                for hour in range(24):
                    count = results['hourly_distribution'].get(hour, 0)
                    if count > 0:
                        output.write(f"{hour:02d}:00    {count:>6}\n")
                output.write("\n")

            # Footer
            output.write("=" * 60 + "\n")
            output.write("END OF REPORT\n")
            output.write("Report generated by Log Analytics Tool\n")
            output.write("=" * 60 + "\n")

            return output.getvalue(), 200, {
                'Content-Type': 'text/plain',
                'Content-Disposition': f'attachment; filename="log_analysis_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.txt"'
            }

        elif format_type == 'json':
            # Create enhanced JSON structure
            enhanced_results = {
                'metadata': {
                    'export_timestamp': datetime.datetime.now().isoformat(),
                    'tool_version': '1.0.0',
                    'report_type': 'Log Analysis Report',
                    'total_entries': results.get('total_entries', 0),
                    'detected_format': results.get('detected_format', 'Unknown')
                },
                'summary': {
                    'total_entries': results.get('total_entries', 0),
                    'error_count': results.get('error_count', 0),
                    'warning_count': results.get('warning_count', 0),
                    'info_count': results.get('info_count', 0),
                    'detected_format': results.get('detected_format', 'Unknown'),
                    'analyzed_at': results.get('analyzed_at', '')
                },
                'web_server_analysis': {
                    'top_ip_addresses': results.get('top_ips', []),
                    'status_codes': results.get('status_codes', {}),
                    'top_urls': results.get('top_urls', []),
                    'hourly_distribution': results.get('hourly_distribution', {})
                } if 'top_ips' in results or 'status_codes' in results else None,
                'network_device_analysis': {
                    'top_interfaces': results.get('top_interfaces', []),
                    'top_facilities': results.get('top_facilities', []),
                    'top_hostnames': results.get('top_hostnames', []),
                    'top_processes': results.get('top_processes', []),
                    'top_process_ids': results.get('top_process_ids', [])
                } if 'top_interfaces' in results or 'top_hostnames' in results else None,
                'raw_analysis_data': results
            }

            # Remove None sections for cleaner output
            enhanced_results = {k: v for k, v in enhanced_results.items() if v is not None}

            return json.dumps(enhanced_results, indent=2), 200, {
                'Content-Type': 'application/json',
                'Content-Disposition': f'attachment; filename="log_analysis_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.json"'
            }

    except Exception as e:
        return f"Export error: {str(e)}"

if __name__ == '__main__':
    """
    Main entry point for the Log Analytics Tool application.

    This block runs when the script is executed directly (not imported as a module).
    It starts the Flask development server with the following configuration:
    - debug=True: Enables debug mode for development (auto-reload, detailed errors)
    - host='0.0.0.0': Binds to all available network interfaces (accessible from other machines)
    - port=5000: Runs the application on port 5000

    In production, consider using a WSGI server like Gunicorn or uWSGI instead of Flask's development server.
    """
    try:
        print("🚀 Starting Log Analytics Tool...")
        print("📊 Web interface available at: http://localhost:5000")
        print("🔧 Debug mode: Enabled")
        print("📁 Upload directory: uploads/")
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        print("💡 Make sure port 5000 is available and not used by another application")
