# MCP Weather Server

A Model Context Protocol (MCP) server that provides weather information using the US National Weather Service API.

## Features

- 🌦️ **Current Weather**: Get detailed weather forecasts for any US location using latitude/longitude coordinates
- ⚠️ **Weather Alerts**: Check active weather alerts and warnings for any US state

## Installation

### Using uvx (Recommended)

[uvx](https://github.com/astral-sh/uv) is a fast, reliable Python package installer and resolver:

```bash
# Install uvx if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh
# On Windows: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Install mg-mcp-weather directly from GitHub
uvx install git+https://github.com/MammothGrowth/mg-mcp-weather.git

# Or install from a local clone
git clone https://github.com/MammothGrowth/mg-mcp-weather.git
cd mg-mcp-weather
uvx install -e .
```

### Using pip

```bash
# Clone the repository
git clone https://github.com/MammothGrowth/mg-mcp-weather.git
cd mg-mcp-weather

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .
```

## Usage

### Running the server directly

After installation with uvx or pip, you can run the server using:

```bash
# If installed with entry point
mg-mcp-weather

# Or using the Python module
python -m mg_mcp_weather
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
      "command": "mg-mcp-weather"
    }
  }
}
```

Alternatively, if using uvx:

```json
{
  "mcpServers": {
    "weather": {
      "command": "uvx",
      "args": ["run", "mg-mcp-weather"]
    }
  }
}
```

4. Restart Claude Desktop

### Using with MCP Inspector

```bash
npx @modelcontextprotocol/inspector mg-mcp-weather

# Or if you prefer:
npx @modelcontextprotocol/inspector uvx run mg-mcp-weather
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
