# Markdown to Audiobook Converter

A web-based tool to convert markdown files into high-quality audiobooks using various Text-to-Speech (TTS) providers.

## Features

- 📄 **Markdown Support**: Upload any `.md` or `.markdown` file
- 🎯 **Multiple TTS Providers**: Support for OpenAI, Google Cloud, Azure, ElevenLabs, and AWS Polly
- 🎨 **Clean Interface**: User-friendly drag-and-drop interface
- ⚙️ **Customizable Settings**: Adjust voice, speed, pitch, and other provider-specific options
- 📊 **Progress Tracking**: Real-time conversion progress with detailed logs
- 💾 **Local Storage**: Saves your API keys and preferences locally
- 🌗 **Dark Mode**: Automatic dark mode support

## Quick Start

1. Open `index.html` in a modern web browser
2. Select your preferred TTS provider
3. Enter your API key for the selected provider
4. Upload your markdown file
5. Configure voice settings
6. Click "Convert to Audiobook"
7. Download your audiobook when complete

## Supported Providers

### OpenAI TTS
- **Voices**: Alloy, Echo, Fable, Onyx, Nova, Shimmer
- **Models**: TTS-1 (Fast), TTS-1-HD (Quality)
- **Formats**: MP3, Opus, AAC, FLAC
- **API Key**: Get from [OpenAI Platform](https://platform.openai.com/api-keys)

### Google Cloud TTS
- **Voices**: Neural2, WaveNet, Standard voices
- **Languages**: Multiple languages supported
- **Formats**: MP3, WAV, OGG
- **API Key**: Get from [Google Cloud Console](https://console.cloud.google.com/)

### Azure Speech Services
- **Voices**: Neural and Standard voices
- **Styles**: Newscast, Narration styles
- **Formats**: MP3, WAV, OGG, Opus
- **API Key**: Get from [Azure Portal](https://portal.azure.com/)

### ElevenLabs
- **Voices**: Various premium voices
- **Models**: Monolingual v1, Multilingual v2, Turbo v2
- **Formats**: MP3, WAV
- **API Key**: Get from [ElevenLabs](https://elevenlabs.io/)

### Amazon Polly
- **Voices**: Joanna, Matthew, Amy, Brian, and more
- **Engines**: Neural and Standard
- **Formats**: MP3, OGG, PCM
- **Note**: Requires additional AWS setup

## Configuration

### API Keys
API keys are stored locally in your browser and never sent to any server. Each provider requires its own API key.

### Text Processing
The converter automatically:
- Removes markdown formatting
- Splits text into appropriate chunks
- Handles sentence boundaries properly
- Preserves natural reading flow

### Chunk Size
Adjust the chunk size based on your provider's limits:
- OpenAI: 4096 characters (default)
- Google/Azure: 5000 characters
- ElevenLabs: 5000 characters
- AWS Polly: 3000 characters

## Advanced Features

### Custom Voice Settings
Each provider offers unique voice customization:
- **Speed/Rate**: Control narration speed
- **Pitch**: Adjust voice pitch (Google, Azure)
- **Stability**: Voice consistency (ElevenLabs)
- **Style**: Speaking style (Azure)

### Output Formats
- **MP3**: Universal compatibility, smaller file size
- **WAV**: Uncompressed audio, larger files
- **Opus**: Modern codec, good compression

## Troubleshooting

### Common Issues

1. **"Invalid API Key" Error**
   - Verify your API key is correct
   - Check if your account has sufficient credits
   - Ensure the API is enabled for your account

2. **"Chunk too large" Error**
   - Reduce the chunk size in settings
   - Check provider-specific limits

3. **No Audio Output**
   - Check browser console for errors
   - Verify provider endpoints are accessible
   - Try a different output format

### Browser Requirements
- Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- JavaScript must be enabled
- Allow file downloads from the site

## Security & Privacy

- **Local Processing**: All text processing happens in your browser
- **API Keys**: Stored locally using browser localStorage
- **No Server**: This is a client-side application with no backend
- **Direct API Calls**: Communicates directly with TTS provider APIs

## Limitations

- Large files may take significant time to process
- API rate limits apply based on your provider plan
- Some voices may not support all languages
- Audio merging is basic (concatenation)

## Future Enhancements

- [ ] Support for SSML markup
- [ ] Batch file processing
- [ ] Advanced audio merging with crossfade
- [ ] Offline mode with cached voices
- [ ] Export/import settings
- [ ] Chapter markers for long books

## Contributing

Feel free to submit issues or pull requests to improve this tool.

## License

This project is open source and available under the MIT License.