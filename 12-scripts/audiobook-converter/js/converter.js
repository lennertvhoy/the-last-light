// Core conversion logic for different TTS providers
window.convertToAudiobook = async function convertToAudiobook(markdown, provider, apiKey, settings) {
    // Clean and prepare the markdown text
    const text = prepareText(markdown);
    
    // Split text into chunks
    const chunks = splitTextIntoChunks(text, settings.chunkSize);
    addLog(`Split text into ${chunks.length} chunks`);
    
    // Convert chunks to audio
    const audioChunks = [];
    
    for (let i = 0; i < chunks.length; i++) {
        updateProgress(i, chunks.length, `Converting chunk ${i + 1} of ${chunks.length}...`);
        
        try {
            const audioData = await convertChunk(chunks[i], provider, apiKey, settings);
            audioChunks.push(audioData);
            addLog(`Converted chunk ${i + 1}/${chunks.length}`);
        } catch (error) {
            addLog(`Error converting chunk ${i + 1}: ${error.message}`, 'error');
            throw error;
        }
    }
    
    updateProgress(chunks.length, chunks.length, 'Merging audio chunks...');
    
    // Merge audio chunks
    const mergedAudio = await mergeAudioChunks(audioChunks, settings.outputFormat);
    
    return mergedAudio;
}

// Prepare markdown text for TTS
function prepareText(markdown) {
    // Remove markdown syntax
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

// Split text into chunks based on size and sentence boundaries
function splitTextIntoChunks(text, chunkSize) {
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

// Convert a single chunk using the specified provider
async function convertChunk(text, provider, apiKey, settings) {
    switch (provider) {
        case 'openai':
            return await convertWithOpenAI(text, apiKey, settings);
        case 'google':
            return await convertWithGoogle(text, apiKey, settings);
        case 'azure':
            return await convertWithAzure(text, apiKey, settings);
        case 'elevenlabs':
            return await convertWithElevenLabs(text, apiKey, settings);
        case 'aws':
            return await convertWithAWS(text, apiKey, settings);
        default:
            throw new Error(`Unsupported provider: ${provider}`);
    }
}

// OpenAI TTS conversion
async function convertWithOpenAI(text, apiKey, settings) {
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

// Google Cloud TTS conversion
async function convertWithGoogle(text, apiKey, settings) {
    const response = await fetch(`https://texttospeech.googleapis.com/v1/text:synthesize?key=${apiKey}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            input: { text: text },
            voice: {
                languageCode: settings.languageCode || 'en-US',
                name: settings.voiceName || 'en-US-Neural2-D'
            },
            audioConfig: {
                audioEncoding: settings.outputFormat === 'mp3' ? 'MP3' : 'LINEAR16',
                speakingRate: parseFloat(settings.speakingRate) || 1.0,
                pitch: parseFloat(settings.pitch) || 0
            }
        })
    });
    
    if (!response.ok) {
        const error = await response.text();
        throw new Error(`Google TTS API error: ${error}`);
    }
    
    const data = await response.json();
    return base64ToArrayBuffer(data.audioContent);
}

// Azure Speech Services conversion
async function convertWithAzure(text, apiKey, settings) {
    const region = settings.region || 'eastus';
    const endpoint = `https://${region}.tts.speech.microsoft.com/cognitiveservices/v1`;
    
    const ssml = `
        <speak version="1.0" xml:lang="en-US">
            <voice name="${settings.voiceName || 'en-US-AriaNeural'}">
                <prosody rate="${settings.rate || '+0%'}">
                    ${escapeXML(text)}
                </prosody>
            </voice>
        </speak>
    `;
    
    const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
            'Ocp-Apim-Subscription-Key': apiKey,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': getAzureOutputFormat(settings.outputFormat)
        },
        body: ssml
    });
    
    if (!response.ok) {
        const error = await response.text();
        throw new Error(`Azure TTS API error: ${error}`);
    }
    
    return await response.arrayBuffer();
}

// ElevenLabs conversion
async function convertWithElevenLabs(text, apiKey, settings) {
    const voiceId = settings.voiceId || '21m00Tcm4TlvDq8ikWAM';
    const modelId = settings.modelId || 'eleven_monolingual_v1';
    
    const response = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
        method: 'POST',
        headers: {
            'xi-api-key': apiKey,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: text,
            model_id: modelId,
            voice_settings: {
                stability: parseFloat(settings.stability) || 0.5,
                similarity_boost: parseFloat(settings.similarityBoost) || 0.75
            }
        })
    });
    
    if (!response.ok) {
        const error = await response.text();
        throw new Error(`ElevenLabs API error: ${error}`);
    }
    
    return await response.arrayBuffer();
}

// AWS Polly conversion (requires AWS SDK - simplified version)
async function convertWithAWS(text, apiKey, settings) {
    // Note: This is a simplified example. In production, you'd use AWS SDK
    // or implement proper AWS Signature V4 signing
    throw new Error('AWS Polly integration requires AWS SDK setup. Please use the AWS SDK directly or set up a proxy server.');
}

// Utility functions
function base64ToArrayBuffer(base64) {
    const binaryString = atob(base64);
    const bytes = new Uint8Array(binaryString.length);
    for (let i = 0; i < binaryString.length; i++) {
        bytes[i] = binaryString.charCodeAt(i);
    }
    return bytes.buffer;
}

function escapeXML(text) {
    return text
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&apos;');
}

function getAzureOutputFormat(format) {
    const formats = {
        'mp3': 'audio-16khz-128kbitrate-mono-mp3',
        'wav': 'riff-16khz-16bit-mono-pcm',
        'opus': 'ogg-48khz-96kbitrate-mono-opus'
    };
    return formats[format] || 'audio-16khz-128kbitrate-mono-mp3';
}

// Merge audio chunks into a single file
async function mergeAudioChunks(chunks, outputFormat) {
    // For MP3 and similar formats, we can simply concatenate the data
    // For more complex formats, you might need to use a library like ffmpeg.js
    
    if (outputFormat === 'mp3' || outputFormat === 'opus') {
        // Simple concatenation for streaming formats
        const totalLength = chunks.reduce((sum, chunk) => sum + chunk.byteLength, 0);
        const merged = new Uint8Array(totalLength);
        
        let offset = 0;
        for (const chunk of chunks) {
            merged.set(new Uint8Array(chunk), offset);
            offset += chunk.byteLength;
        }
        
        return [merged.buffer];
    } else if (outputFormat === 'wav') {
        // WAV files need proper header handling
        // This is a simplified version - in production, use a proper audio library
        addLog('WAV merging requires additional processing. Using simple concatenation.', 'warning');
        
        const totalLength = chunks.reduce((sum, chunk) => sum + chunk.byteLength, 0);
        const merged = new Uint8Array(totalLength);
        
        let offset = 0;
        for (const chunk of chunks) {
            merged.set(new Uint8Array(chunk), offset);
            offset += chunk.byteLength;
        }
        
        return [merged.buffer];
    }
    
    return chunks;
}