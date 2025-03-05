"""Main entry point for the MCP weather server."""

if __name__ == "__main__":
    from mg_mcp_weather.server import mcp
    mcp.run(transport='stdio')
