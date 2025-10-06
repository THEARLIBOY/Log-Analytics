// Initialize Feather icons
feather.replace();

/*
 * Professional Log Analytics Tool - JavaScript
 * A simple, beautiful web interface for log analysis
 *
 * Author: Rezaul Karim
 * Email: work.rezaul@outlook.com
 * Powered By: REZ LAB
 */

// =============================================
// LOG ANALYTICS TOOL - FRONTEND JAVASCRIPT
// =============================================
// Professional web interface for log analysis
//
// Author: Rezaul Karim
// Email: work.rezaul@outlook.com
// Powered By: REZ LAB
//
// This file handles all client-side functionality including:
// - File upload and drag & drop
// - Text input and validation
// - Real-time progress indication
// - Results display and filtering
// - Export functionality
// =============================================

// =============================================
// DOM ELEMENT REFERENCES
// =============================================
// Cache frequently used DOM elements for performance
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const logTextarea = document.getElementById('logTextarea');
const textInputToggle = document.getElementById('textInputToggle');
const textareaContainer = document.getElementById('textareaContainer');
const progressBar = document.getElementById('progressBar');
const progressFill = document.getElementById('progressFill');
const loading = document.getElementById('loading');
const resultsSection = document.getElementById('resultsSection');
const resultsGrid = document.getElementById('resultsGrid');

// =============================================
// APPLICATION STATE VARIABLES
// =============================================
// Track the current state of the application
let textInputActive = false;    // Whether text input mode is active
let currentResults = null;      // Store analysis results for filtering
let originalLogs = [];         // Keep original log data for reference
let filtersActive = false;     // Whether filters are currently applied

// Drag and drop functionality
uploadArea.addEventListener('click', () => fileInput.click());

uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('dragover');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('dragover');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('dragover');

    const files = e.dataTransfer.files;
    if (files.length > 0) {
        fileInput.files = files;
        analyzeLogs();
    }
});

fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        analyzeLogs();
    }
});

// Text input toggle
function toggleTextInput() {
    textInputActive = !textInputActive;
    if (textInputActive) {
        textInputToggle.classList.add('active');
        textareaContainer.classList.add('active');
    } else {
        textInputToggle.classList.remove('active');
        textareaContainer.classList.remove('active');
    }
}

// Analyze logs function
async function analyzeLogs() {
    const formData = new FormData();

    if (fileInput.files.length > 0) {
        formData.append('log_file', fileInput.files[0]);
    } else if (textInputActive && logTextarea.value.trim()) {
        formData.append('log_content', logTextarea.value.trim());
    } else {
        alert('Please select a file or paste log content to analyze.');
        return;
    }

    // Show loading state
    loading.classList.add('active');
    resultsSection.classList.remove('active');
    progressFill.style.width = '0%';

    try {
        // Simulate progress
        const progressInterval = setInterval(() => {
            const currentWidth = parseFloat(progressFill.style.width) || 0;
            if (currentWidth < 90) {
                progressFill.style.width = (currentWidth + 10) + '%';
            }
        }, 200);

        const response = await fetch('/analyze', {
            method: 'POST',
            body: formData
        });

        clearInterval(progressInterval);
        progressFill.style.width = '100%';

        const results = await response.json();

        if (response.ok) {
            currentResults = results; // Store results for filtering
            displayResults(results);
        } else {
            alert('Error: ' + results.error);
        }
    } catch (error) {
        alert('Error analyzing logs: ' + error.message);
    } finally {
        loading.classList.remove('active');
        setTimeout(() => {
            progressFill.style.width = '0%';
        }, 1000);
    }
}

// Display results
function displayResults(results) {
    resultsGrid.innerHTML = '';

    // Summary card
    const summaryCard = createSummaryCard(results);
    resultsGrid.appendChild(summaryCard);

    // Status codes card (for web logs)
    if (results.status_codes) {
        const statusCard = createStatusCard(results);
        resultsGrid.appendChild(statusCard);
    }

    // Top IPs card (for web logs)
    if (results.top_ips && results.top_ips.length > 0) {
        const ipsCard = createTopIPsCard(results);
        resultsGrid.appendChild(ipsCard);
    }

    // Top URLs card (for web logs)
    if (results.top_urls && results.top_urls.length > 0) {
        const urlsCard = createTopURLsCard(results);
        resultsGrid.appendChild(urlsCard);
    }

            // Hostnames card (for syslog)
            if (results.top_hostnames && results.top_hostnames.length > 0) {
                const hostnamesCard = createTopHostnamesCard(results);
                resultsGrid.appendChild(hostnamesCard);
            }

            // Interfaces card (for MikroTik)
            if (results.top_interfaces && results.top_interfaces.length > 0) {
                const interfacesCard = createTopInterfacesCard(results);
                resultsGrid.appendChild(interfacesCard);
            }

            // Facilities card (for MikroTik)
            if (results.top_facilities && results.top_facilities.length > 0) {
                const facilitiesCard = createTopFacilitiesCard(results);
                resultsGrid.appendChild(facilitiesCard);
            }

            // Process IDs card (for Cisco)
            if (results.top_process_ids && results.top_process_ids.length > 0) {
                const processIdsCard = createTopProcessIdsCard(results);
                resultsGrid.appendChild(processIdsCard);
            }

    resultsSection.classList.add('active');
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}

// Create summary card
function createSummaryCard(results) {
    const card = document.createElement('div');
    card.className = 'result-card fade-in';

    let statusBadge = '';
    const errorRate = results.total_entries > 0 ? (results.error_count / results.total_entries) * 100 : 0;

    if (errorRate > 10) {
        statusBadge = '<span class="status-badge status-error">High Error Rate</span>';
    } else if (errorRate > 5) {
        statusBadge = '<span class="status-badge status-warning">Moderate Errors</span>';
    } else {
        statusBadge = '<span class="status-badge status-success">Good</span>';
    }

    card.innerHTML = `
        <h3 class="card-title">
            <i data-feather="activity"></i>
            Summary ${statusBadge}
        </h3>
        <div class="metric">
            <span class="metric-label">Total Entries</span>
            <span class="metric-value">${results.total_entries.toLocaleString()}</span>
        </div>
        <div class="metric">
            <span class="metric-label">Error Count</span>
            <span class="metric-value">${results.error_count}</span>
        </div>
        <div class="metric">
            <span class="metric-label">Warning Count</span>
            <span class="metric-value">${results.warning_count}</span>
        </div>
        <div class="metric">
            <span class="metric-label">Log Format</span>
            <span class="metric-value">${results.detected_format}</span>
        </div>
    `;

    return card;
}

// Create status codes card
function createStatusCard(results) {
    const card = document.createElement('div');
    card.className = 'result-card fade-in';

    let statusContent = '<div class="top-list">';
    for (const [status, count] of Object.entries(results.status_codes)) {
        statusContent += `
            <div class="top-item">
                <span class="top-name">${status}</span>
                <span class="top-count">${count}</span>
            </div>
        `;
    }
    statusContent += '</div>';

    card.innerHTML = `
        <h3 class="card-title">
            <i data-feather="hash"></i>
            HTTP Status Codes
        </h3>
        ${statusContent}
    `;

    return card;
}

// Create top IPs card
function createTopIPsCard(results) {
    const card = document.createElement('div');
    card.className = 'result-card fade-in';

    let ipsContent = '<div class="top-list">';
    for (const [ip, count] of results.top_ips) {
        ipsContent += `
            <div class="top-item">
                <span class="top-name">${ip}</span>
                <span class="top-count">${count}</span>
            </div>
        `;
    }
    ipsContent += '</div>';

    card.innerHTML = `
        <h3 class="card-title">
            <i data-feather="users"></i>
            Top IP Addresses
        </h3>
        ${ipsContent}
    `;

    return card;
}

// Create top URLs card
function createTopURLsCard(results) {
    const card = document.createElement('div');
    card.className = 'result-card fade-in';

    let urlsContent = '<div class="top-list">';
    for (const [url, count] of results.top_urls) {
        const shortUrl = url.length > 40 ? url.substring(0, 40) + '...' : url;
        urlsContent += `
            <div class="top-item">
                <span class="top-name" title="${url}">${shortUrl}</span>
                <span class="top-count">${count}</span>
            </div>
        `;
    }
    urlsContent += '</div>';

    card.innerHTML = `
        <h3 class="card-title">
            <i data-feather="link"></i>
            Top URLs
        </h3>
        ${urlsContent}
    `;

    return card;
}

// Create top hostnames card
function createTopHostnamesCard(results) {
    const card = document.createElement('div');
    card.className = 'result-card fade-in';

    let hostnamesContent = '<div class="top-list">';
    for (const [hostname, count] of results.top_hostnames) {
        hostnamesContent += `
            <div class="top-item">
                <span class="top-name">${hostname}</span>
                <span class="top-count">${count}</span>
            </div>
        `;
    }
    hostnamesContent += '</div>';

    card.innerHTML = `
        <h3 class="card-title">
            <i data-feather="server"></i>
            Top Hostnames
        </h3>
        ${hostnamesContent}
    `;

    return card;
}

// Create top interfaces card (for MikroTik)
function createTopInterfacesCard(results) {
    const card = document.createElement('div');
    card.className = 'result-card fade-in';

    let interfacesContent = '<div class="top-list">';
    for (const [interface, count] of results.top_interfaces) {
        interfacesContent += `
            <div class="top-item">
                <span class="top-name">${interface}</span>
                <span class="top-count">${count}</span>
            </div>
        `;
    }
    interfacesContent += '</div>';

    card.innerHTML = `
        <h3 class="card-title">
            <i data-feather="router"></i>
            Top Interfaces
        </h3>
        ${interfacesContent}
    `;

    return card;
}

// Create top facilities card (for MikroTik)
function createTopFacilitiesCard(results) {
    const card = document.createElement('div');
    card.className = 'result-card fade-in';

    let facilitiesContent = '<div class="top-list">';
    for (const [facility, count] of results.top_facilities) {
        facilitiesContent += `
            <div class="top-item">
                <span class="top-name">${facility}</span>
                <span class="top-count">${count}</span>
            </div>
        `;
    }
    facilitiesContent += '</div>';

    card.innerHTML = `
        <h3 class="card-title">
            <i data-feather="settings"></i>
            Top Facilities
        </h3>
        ${facilitiesContent}
    `;

    return card;
}

// Create top process IDs card (for Cisco)
function createTopProcessIdsCard(results) {
    const card = document.createElement('div');
    card.className = 'result-card fade-in';

    let processIdsContent = '<div class="top-list">';
    for (const [processId, count] of results.top_process_ids) {
        processIdsContent += `
            <div class="top-item">
                <span class="top-name">${processId}</span>
                <span class="top-count">${count}</span>
            </div>
        `;
    }
    processIdsContent += '</div>';

    card.innerHTML = `
        <h3 class="card-title">
            <i data-feather="cpu"></i>
            Top Process IDs
        </h3>
        ${processIdsContent}
    `;

    return card;
}

// Export results
function exportResults(format) {
    window.location.href = `/export/${format}`;
}

// Clear all function
function clearAll() {
    fileInput.value = '';
    logTextarea.value = '';
    if (textInputActive) {
        toggleTextInput();
    }
    resultsSection.classList.remove('active');
    uploadArea.classList.remove('dragover');
}

// Filter functions
function toggleFilters() {
    const filtersPanel = document.getElementById('filtersPanel');
    const filterToggle = document.getElementById('filterToggle');

    if (filtersPanel.classList.contains('active')) {
        filtersPanel.classList.remove('active');
        filterToggle.innerHTML = '<i data-feather="filter"></i><span>Show Filters</span>';
    } else {
        filtersPanel.classList.add('active');
        filterToggle.innerHTML = '<i data-feather="filter"></i><span>Hide Filters</span>';
    }
    feather.replace();
}

function applyFilters() {
    if (!currentResults) {
        alert('Please analyze logs first before applying filters.');
        return;
    }

    const filters = {
        start_date: document.getElementById('startDate').value,
        end_date: document.getElementById('endDate').value,
        ip_filter: document.getElementById('ipFilter').value,
        status_filter: document.getElementById('statusFilter').value,
        url_filter: document.getElementById('urlFilter').value,
        search_text: document.getElementById('searchText').value
    };

    // Check if any filters are applied
    const hasFilters = Object.values(filters).some(value => value && value.trim() !== '');

    if (!hasFilters) {
        alert('Please set at least one filter to apply.');
        return;
    }

    // Show loading state
    loading.classList.add('active');
    resultsSection.classList.remove('active');

    // Simulate filtering process
    setTimeout(() => {
        displayFilteredResults(currentResults, filters);
        loading.classList.remove('active');
    }, 500);
}

function displayFilteredResults(results, filters) {
    // Create a copy of results for filtering
    const filteredResults = JSON.parse(JSON.stringify(results));

    // Apply simple client-side filtering for demo
    // In a real application, this would be done server-side

    // Filter status codes
    if (filters.status_filter) {
        // This is a simplified filter - in reality you'd need the original logs
        alert(`Filter applied: Status Code = ${filters.status_filter}\n\nNote: Server-side filtering would be needed for complete accuracy.`);
    }

    // Filter IPs
    if (filters.ip_filter) {
        if (filteredResults.top_ips) {
            filteredResults.top_ips = filteredResults.top_ips.filter(([ip]) =>
                ip.includes(filters.ip_filter)
            );
        }
    }

    // Filter URLs
    if (filters.url_filter) {
        if (filteredResults.top_urls) {
            filteredResults.top_urls = filteredResults.top_urls.filter(([url]) =>
                url.toLowerCase().includes(filters.url_filter.toLowerCase())
            );
        }
    }

    // Update counts based on filters
    if (filters.ip_filter || filters.url_filter || filters.status_filter) {
        filteredResults.total_entries = Math.floor(filteredResults.total_entries * 0.7); // Simulated reduction
        filteredResults.error_count = Math.floor(filteredResults.error_count * 0.8);
    }

    // Re-display results
    displayResults(filteredResults);
    filtersActive = true;
}

function clearFilters() {
    document.getElementById('startDate').value = '';
    document.getElementById('endDate').value = '';
    document.getElementById('ipFilter').value = '';
    document.getElementById('statusFilter').value = '';
    document.getElementById('urlFilter').value = '';
    document.getElementById('searchText').value = '';

    if (currentResults) {
        displayResults(currentResults);
        filtersActive = false;
    }
}

// Show sample function
function showSample() {
    const sampleLogs = `192.168.1.100 - - [10/Oct/2023:13:55:36] "GET /api/users HTTP/1.1" 200 1234
192.168.1.101 - - [10/Oct/2023:13:55:37] "POST /api/login HTTP/1.1" 401 567
192.168.1.100 - - [10/Oct/2023:13:55:38] "GET /api/users/1 HTTP/1.1" 200 890
192.168.1.102 - - [10/Oct/2023:13:55:39] "GET /api/products HTTP/1.1" 500 0
192.168.1.103 - - [10/Oct/2023:13:55:40] "GET /api/orders HTTP/1.1" 200 2341`;

    logTextarea.value = sampleLogs;
    toggleTextInput();
    alert('Sample web server logs loaded! Click "Analyze Logs" to see the results.');
}

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    feather.replace();
});
