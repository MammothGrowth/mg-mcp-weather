"""Main entry point for the MCP weather server."""

from mg_mcp_weather.server import mcp


def main():
    """Run the MCP weather server with stdio transport."""
    mcp.run(transport='stdio')


if __name__ == "__main__":
    main()
