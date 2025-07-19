// Provider-specific settings and configurations
function getProviderSettings(provider) {
    const settings = {
        openai: [
            {
                id: 'voice',
                label: 'Voice',
                type: 'select',
                options: [
                    { value: 'alloy', label: 'Alloy', default: true },
                    { value: 'echo', label: 'Echo' },
                    { value: 'fable', label: 'Fable' },
                    { value: 'onyx', label: 'Onyx' },
                    { value: 'nova', label: 'Nova' },
                    { value: 'shimmer', label: 'Shimmer' }
                ]
            },
            {
                id: 'model',
                label: 'Model',
                type: 'select',
                options: [
                    { value: 'tts-1', label: 'TTS-1 (Fast)', default: true },
                    { value: 'tts-1-hd', label: 'TTS-1-HD (Quality)' }
                ]
            },
            {
                id: 'speed',
                label: 'Speed',
                type: 'number',
                default: 1.0,
                min: 0.25,
                max: 4.0,
                step: 0.25,
                description: 'Playback speed (0.25 - 4.0)'
            }
        ],
        google: [
            {
                id: 'languageCode',
                label: 'Language',
                type: 'select',
                options: [
                    { value: 'en-US', label: 'English (US)', default: true },
                    { value: 'en-GB', label: 'English (UK)' },
                    { value: 'es-ES', label: 'Spanish (Spain)' },
                    { value: 'fr-FR', label: 'French (France)' },
                    { value: 'de-DE', label: 'German (Germany)' }
                ]
            },
            {
                id: 'voiceName',
                label: 'Voice Name',
                type: 'text',
                default: 'en-US-Neural2-D',
                description: 'Google Cloud voice name'
            },
            {
                id: 'speakingRate',
                label: 'Speaking Rate',
                type: 'number',
                default: 1.0,
                min: 0.25,
                max: 4.0,
                step: 0.1
            },
            {
                id: 'pitch',
                label: 'Pitch',
                type: 'number',
                default: 0,
                min: -20,
                max: 20,
                step: 1,
                description: 'Voice pitch (-20 to 20 semitones)'
            }
        ],
        azure: [
            {
                id: 'region',
                label: 'Region',
                type: 'text',
                default: 'eastus',
                description: 'Azure region (e.g., eastus, westeurope)'
            },
            {
                id: 'voiceName',
                label: 'Voice Name',
                type: 'text',
                default: 'en-US-AriaNeural',
                description: 'Azure voice name'
            },
            {
                id: 'style',
                label: 'Speaking Style',
                type: 'select',
                options: [
                    { value: 'default', label: 'Default', default: true },
                    { value: 'newscast', label: 'Newscast' },
                    { value: 'narration-professional', label: 'Professional Narration' },
                    { value: 'narration-relaxed', label: 'Relaxed Narration' }
                ]
            },
            {
                id: 'rate',
                label: 'Rate',
                type: 'text',
                default: '+0%',
                description: 'Speaking rate (e.g., -50%, +0%, +50%)'
            }
        ],
        elevenlabs: [
            {
                id: 'voiceId',
                label: 'Voice ID',
                type: 'text',
                default: '21m00Tcm4TlvDq8ikWAM',
                description: 'ElevenLabs voice ID'
            },
            {
                id: 'modelId',
                label: 'Model',
                type: 'select',
                options: [
                    { value: 'eleven_monolingual_v1', label: 'Monolingual v1', default: true },
                    { value: 'eleven_multilingual_v2', label: 'Multilingual v2' },
                    { value: 'eleven_turbo_v2', label: 'Turbo v2' }
                ]
            },
            {
                id: 'stability',
                label: 'Stability',
                type: 'number',
                default: 0.5,
                min: 0,
                max: 1,
                step: 0.1,
                description: 'Voice stability (0-1)'
            },
            {
                id: 'similarityBoost',
                label: 'Similarity Boost',
                type: 'number',
                default: 0.75,
                min: 0,
                max: 1,
                step: 0.1,
                description: 'Voice similarity (0-1)'
            }
        ],
        aws: [
            {
                id: 'region',
                label: 'AWS Region',
                type: 'text',
                default: 'us-east-1',
                description: 'AWS region'
            },
            {
                id: 'voiceId',
                label: 'Voice',
                type: 'select',
                options: [
                    { value: 'Joanna', label: 'Joanna (US English)', default: true },
                    { value: 'Matthew', label: 'Matthew (US English)' },
                    { value: 'Amy', label: 'Amy (British English)' },
                    { value: 'Brian', label: 'Brian (British English)' }
                ]
            },
            {
                id: 'engine',
                label: 'Engine',
                type: 'select',
                options: [
                    { value: 'neural', label: 'Neural', default: true },
                    { value: 'standard', label: 'Standard' }
                ]
            },
            {
                id: 'sampleRate',
                label: 'Sample Rate',
                type: 'select',
                options: [
                    { value: '22050', label: '22050 Hz', default: true },
                    { value: '16000', label: '16000 Hz' },
                    { value: '8000', label: '8000 Hz' }
                ]
            }
        ]
    };
    
    return settings[provider] || [];
}