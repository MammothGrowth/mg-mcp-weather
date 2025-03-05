# MCP Weather Server

A Model Context Protocol (MCP) server that provides weather information using the US National Weather Service API.

## Features

- 🌦️ **Current Weather**: Get detailed weather forecasts for any US location using latitude/longitude coordinates
- ⚠️ **Weather Alerts**: Check active weather alerts and warnings for any US state

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/mg-mcp-weather.git
cd mg-mcp-weather

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .
```

## Usage

### Running the server directly

```bash
python -m mg_mcp_weather.server
```

### Using with Claude Desktop

1. Install [Claude Desktop](https://claude.ai/download)
2. Create or edit the Claude config file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

3. Add this server to the configuration:

```json
{
  "mcpServers": {
    "weather": {
      "command": "python",
      "args": ["-m", "mg_mcp_weather.server"]
    }
  }
}
```

4. Restart Claude Desktop

### Using with MCP Inspector

```bash
npx @modelcontextprotocol/inspector python -m mg_mcp_weather.server
```

## Tools

### Get Weather Alerts

Returns active weather alerts for a US state.

```
Arguments:
- state: Two-letter US state code (e.g. CA, NY)
```

### Get Weather Forecast

Returns detailed weather forecasts for specific coordinates.

```
Arguments:
- latitude: Latitude coordinate (float)
- longitude: Longitude coordinate (float)
```

## Limitations

- Only works with US locations (uses the US National Weather Service API)
- Requires an internet connection to fetch data

## License

MIT

## Credits

This project uses the [US National Weather Service API](https://weather.gov/documentation/services-web-api).
