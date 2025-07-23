// Main application logic
let uploadedFile = null;
let audioBlob = null;

// Initialize the app
document.addEventListener('DOMContentLoaded', () => {
    setupFileUpload();
    loadSavedSettings();
    updateProviderSettings();
});

// File upload handling
function setupFileUpload() {
    const uploadArea = document.getElementById('uploadArea');
    const fileInput = document.getElementById('fileInput');

    // Make sure the click event works
    uploadArea.addEventListener('click', (e) => {
        e.preventDefault();
        fileInput.click();
    });
    
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
        if (files.length > 0 && files[0].name.match(/\.(md|markdown)$/i)) {
            handleFileSelect(files[0]);
        } else {
            addLog('Please upload a valid markdown file (.md or .markdown)', 'error');
        }
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleFileSelect(e.target.files[0]);
        }
    });
}

// Handle file selection
function handleFileSelect(file) {
    uploadedFile = file;
    
    // Update UI
    document.getElementById('uploadArea').style.display = 'none';
    document.getElementById('fileInfo').style.display = 'flex';
    document.querySelector('.file-name').textContent = file.name;
    document.getElementById('convertBtn').disabled = false;
    
    addLog(`File loaded: ${file.name} (${formatFileSize(file.size)})`);
}

// Remove uploaded file
function removeFile() {
    uploadedFile = null;
    
    // Reset UI
    document.getElementById('uploadArea').style.display = 'flex';
    document.getElementById('fileInfo').style.display = 'none';
    document.getElementById('convertBtn').disabled = true;
    document.getElementById('fileInput').value = '';
    
    addLog('File removed');
}

// Update provider-specific settings
function updateProviderSettings() {
    const provider = document.getElementById('provider').value;
    const settingsContainer = document.getElementById('providerSettings');
    
    // Clear existing settings
    settingsContainer.innerHTML = '';
    
    // Add provider-specific settings
    const settings = getProviderSettings(provider);
    
    settings.forEach(setting => {
        const formGroup = document.createElement('div');
        formGroup.className = 'form-group';
        
        const label = document.createElement('label');
        label.setAttribute('for', setting.id);
        label.textContent = setting.label;
        formGroup.appendChild(label);
        
        if (setting.type === 'select') {
            const select = document.createElement('select');
            select.id = setting.id;
            setting.options.forEach(opt => {
                const option = document.createElement('option');
                option.value = opt.value;
                option.textContent = opt.label;
                if (opt.default) option.selected = true;
                select.appendChild(option);
            });
            formGroup.appendChild(select);
        } else {
            const input = document.createElement('input');
            input.type = setting.type;
            input.id = setting.id;
            input.value = setting.default || '';
            if (setting.min) input.min = setting.min;
            if (setting.max) input.max = setting.max;
            if (setting.step) input.step = setting.step;
            formGroup.appendChild(input);
        }
        
        if (setting.description) {
            const small = document.createElement('small');
            small.textContent = setting.description;
            formGroup.appendChild(small);
        }
        
        settingsContainer.appendChild(formGroup);
    });
    
    // Load saved settings for this provider
    loadProviderSettings(provider);
}

// Start the conversion process
async function startConversion() {
    if (!uploadedFile) {
        addLog('No file selected', 'error');
        return;
    }
    
    const apiKey = document.getElementById('apiKey').value;
    if (!apiKey) {
        addLog('Please enter your API key', 'error');
        return;
    }
    
    // Save settings
    saveSettings();
    
    // Update UI
    document.getElementById('convertBtn').disabled = true;
    document.querySelector('.btn-text').style.display = 'none';
    document.querySelector('.spinner').style.display = 'block';
    document.getElementById('progressContainer').style.display = 'block';
    document.getElementById('downloadSection').style.display = 'none';
    
    try {
        // Read the markdown file
        const markdown = await readFile(uploadedFile);
        addLog('Reading markdown file...');
        
        // Start conversion
        const provider = document.getElementById('provider').value;
        const settings = collectSettings();
        
        addLog(`Starting conversion with ${provider}...`);
        
        const audioData = await convertToAudiobookInternal(markdown, provider, apiKey, settings);
        
        // Create blob from audio data
        audioBlob = new Blob(audioData, { type: getAudioMimeType(settings.outputFormat) });
        
        // Show download section
        document.getElementById('downloadSection').style.display = 'block';
        addLog('Conversion complete! Your audiobook is ready for download.', 'success');
        
    } catch (error) {
        addLog(`Error: ${error.message}`, 'error');
        console.error('Conversion error:', error);
    } finally {
        // Reset button
        document.getElementById('convertBtn').disabled = false;
        document.querySelector('.btn-text').style.display = 'inline';
        document.querySelector('.spinner').style.display = 'none';
    }
}

// Download the audiobook
function downloadAudiobook() {
    if (!audioBlob) return;
    
    const fileName = uploadedFile.name.replace(/\.(md|markdown)$/i, '') + '.' + document.getElementById('outputFormat').value;
    const url = URL.createObjectURL(audioBlob);
    
    const a = document.createElement('a');
    a.href = url;
    a.download = fileName;
    a.click();
    
    URL.revokeObjectURL(url);
    addLog(`Downloaded: ${fileName}`);
}

// Utility functions
function readFile(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = (e) => resolve(e.target.result);
        reader.onerror = reject;
        reader.readAsText(file);
    });
}

function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

function addLog(message, type = 'info') {
    const logContainer = document.getElementById('logContainer');
    const entry = document.createElement('p');
    entry.className = `log-entry log-${type}`;
    
    const timestamp = new Date().toLocaleTimeString();
    entry.textContent = `[${timestamp}] ${message}`;
    
    logContainer.appendChild(entry);
    logContainer.scrollTop = logContainer.scrollHeight;
}

function updateProgress(current, total, message) {
    const percentage = (current / total) * 100;
    document.getElementById('progressFill').style.width = percentage + '%';
    document.getElementById('progressText').textContent = message || `Processing... ${Math.round(percentage)}%`;
}

function collectSettings() {
    const provider = document.getElementById('provider').value;
    const settings = {
        provider: provider,
        chunkSize: parseInt(document.getElementById('chunkSize').value),
        outputFormat: document.getElementById('outputFormat').value
    };
    
    // Collect provider-specific settings
    const providerSettingsList = getProviderSettings(provider);
    providerSettingsList.forEach(setting => {
        const element = document.getElementById(setting.id);
        if (element) {
            settings[setting.id] = element.value;
        }
    });
    
    return settings;
}

function getAudioMimeType(format) {
    const mimeTypes = {
        'mp3': 'audio/mpeg',
        'wav': 'audio/wav',
        'opus': 'audio/opus'
    };
    return mimeTypes[format] || 'audio/mpeg';
}

// Settings persistence
function saveSettings() {
    const provider = document.getElementById('provider').value;
    const settings = collectSettings();
    localStorage.setItem(`audiobook-converter-${provider}`, JSON.stringify(settings));
    localStorage.setItem('audiobook-converter-last-provider', provider);
}

function loadSavedSettings() {
    const lastProvider = localStorage.getItem('audiobook-converter-last-provider');
    if (lastProvider) {
        document.getElementById('provider').value = lastProvider;
    }
}

function loadProviderSettings(provider) {
    const saved = localStorage.getItem(`audiobook-converter-${provider}`);
    if (saved) {
        try {
            const settings = JSON.parse(saved);
            Object.keys(settings).forEach(key => {
                const element = document.getElementById(key);
                if (element && key !== 'provider') {
                    element.value = settings[key];
                }
            });
        } catch (e) {
            console.error('Error loading saved settings:', e);
        }
    }
}

// Core conversion logic
async function convertToAudiobookInternal(markdown, provider, apiKey, settings) {
    // Clean and prepare the markdown text
    const text = prepareTextInternal(markdown);
    
    // Split text into chunks
    const chunks = splitTextIntoChunksInternal(text, settings.chunkSize);
    addLog(`Split text into ${chunks.length} chunks`);
    
    // Convert chunks to audio
    const audioChunks = [];
    
    for (let i = 0; i < chunks.length; i++) {
        updateProgress(i, chunks.length, `Converting chunk ${i + 1} of ${chunks.length}...`);
        
        try {
            const audioData = await convertChunkInternal(chunks[i], provider, apiKey, settings);
            audioChunks.push(audioData);
            addLog(`Converted chunk ${i + 1}/${chunks.length}`);
        } catch (error) {
            addLog(`Error converting chunk ${i + 1}: ${error.message}`, 'error');
            throw error;
        }
    }
    
    updateProgress(chunks.length, chunks.length, 'Merging audio chunks...');
    
    // Merge audio chunks
    const mergedAudio = await mergeAudioChunksInternal(audioChunks, settings.outputFormat);
    
    return mergedAudio;
}

// Prepare markdown text for TTS
function prepareTextInternal(markdown) {
    let text = markdown;
    
    // Remove Unicode box drawing characters and other problematic characters
    text = text.replace(/[\u2500-\u257F]/g, ''); // Box drawing characters
    text = text.replace(/[\u2580-\u259F]/g, ''); // Block elements
    text = text.replace(/[\u25A0-\u25FF]/g, ''); // Geometric shapes
    text = text.replace(/[\u2190-\u21FF]/g, ''); // Arrows
    text = text.replace(/[\u2600-\u26FF]/g, ''); // Miscellaneous symbols
    text = text.replace(/[\u2700-\u27BF]/g, ''); // Dingbats
    
    // Replace common problematic characters
    text = text.replace(/[""]/g, '"'); // Smart quotes
    text = text.replace(/['']/g, "'"); // Smart apostrophes
    text = text.replace(/[—–]/g, '-'); // Em/en dashes
    text = text.replace(/[…]/g, '...'); // Ellipsis
    
    // Remove code blocks
    text = text.replace(/```[\s\S]*?```/g, '');
    
    // Remove inline code
    text = text.replace(/`[^`]+`/g, '');
    
    // Remove images
    text = text.replace(/!\[.*?\]\(.*?\)/g, '');
    
    // Convert links to just text
    text = text.replace(/\[([^\]]+)\]\([^\)]+\)/g, '$1');
    
    // Remove headers but keep the text
    text = text.replace(/^#{1,6}\s+(.+)$/gm, '$1');
    
    // Remove bold and italic markers
    text = text.replace(/\*\*([^*]+)\*\*/g, '$1');
    text = text.replace(/\*([^*]+)\*/g, '$1');
    text = text.replace(/__([^_]+)__/g, '$1');
    text = text.replace(/_([^_]+)_/g, '$1');
    
    // Remove blockquotes marker but keep text
    text = text.replace(/^>\s+(.+)$/gm, '$1');
    
    // Remove horizontal rules
    text = text.replace(/^---+$/gm, '');
    text = text.replace(/^\*\*\*+$/gm, '');
    
    // Clean up lists
    text = text.replace(/^[\s]*[-*+]\s+/gm, '');
    text = text.replace(/^[\s]*\d+\.\s+/gm, '');
    
    // Remove HTML tags
    text = text.replace(/<[^>]+>/g, '');
    
    // Clean up extra whitespace
    text = text.replace(/\n{3,}/g, '\n\n');
    text = text.trim();
    
    return text;
}

// Split text into chunks
function splitTextIntoChunksInternal(text, chunkSize) {
    const sentences = text.match(/[^.!?]+[.!?]+/g) || [text];
    const chunks = [];
    let currentChunk = '';
    
    for (const sentence of sentences) {
        if ((currentChunk + sentence).length > chunkSize) {
            if (currentChunk) {
                chunks.push(currentChunk.trim());
                currentChunk = sentence;
            } else {
                // Single sentence exceeds chunk size, split it
                const words = sentence.split(' ');
                let wordChunk = '';
                
                for (const word of words) {
                    if ((wordChunk + ' ' + word).length > chunkSize) {
                        chunks.push(wordChunk.trim());
                        wordChunk = word;
                    } else {
                        wordChunk += (wordChunk ? ' ' : '') + word;
                    }
                }
                
                if (wordChunk) {
                    currentChunk = wordChunk;
                }
            }
        } else {
            currentChunk += (currentChunk ? ' ' : '') + sentence;
        }
    }
    
    if (currentChunk) {
        chunks.push(currentChunk.trim());
    }
    
    return chunks;
}

// Convert a single chunk
async function convertChunkInternal(text, provider, apiKey, settings) {
    if (provider === 'openai') {
        return await convertWithOpenAIInternal(text, apiKey, settings);
    }
    throw new Error(`Unsupported provider: ${provider}`);
}

// OpenAI TTS conversion
async function convertWithOpenAIInternal(text, apiKey, settings) {
    // Ensure text is properly encoded and clean
    const cleanText = text.replace(/[^\x00-\x7F]/g, function(char) {
        // Replace non-ASCII characters with their closest ASCII equivalent
        const replacements = {
            '"': '"', '"': '"',
            ''': "'", ''': "'",
            '—': '-', '–': '-',
            '…': '...'
        };
        return replacements[char] || '';
    });
    
    const response = await fetch('https://api.openai.com/v1/audio/speech', {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${apiKey}`,
            'Content-Type': 'application/json; charset=utf-8'
        },
        body: JSON.stringify({
            model: settings.model || 'tts-1',
            input: cleanText,
            voice: settings.voice || 'alloy',
            speed: parseFloat(settings.speed) || 1.0,
            response_format: settings.outputFormat || 'mp3'
        })
    });
    
    if (!response.ok) {
        const error = await response.text();
        throw new Error(`OpenAI API error: ${error}`);
    }
    
    return await response.arrayBuffer();
}

// Merge audio chunks
async function mergeAudioChunksInternal(chunks, outputFormat) {
    const totalLength = chunks.reduce((sum, chunk) => sum + chunk.byteLength, 0);
    const merged = new Uint8Array(totalLength);
    
    let offset = 0;
    for (const chunk of chunks) {
        merged.set(new Uint8Array(chunk), offset);
        offset += chunk.byteLength;
    }
    
    return [merged.buffer];
}