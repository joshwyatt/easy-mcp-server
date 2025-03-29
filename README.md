# Easy MCP Server

A simple Model Context Protocol (MCP) server with support for both stdio and Server-Sent Events (SSE) transport.

## Installation

```bash
pip install easy-mcp-server
```

Or with uv:

```bash
uv pip install easy-mcp-server
```

## Usage

```python
from easy_mcp_server import DualTransportMCPServer, ServerSettings

# Define your tools
def say_hello(name: str) -> str:
    """Greet someone."""
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

# Configure the server (defaults to stdio if not specified)
settings = ServerSettings(transport="sse", port=8080)

# Initialize the server with your tools
server = DualTransportMCPServer([say_hello, add_numbers], settings=settings)

# Run the server
server.run()
```

## Features

- Supports both stdio and SSE transport modes
- Automatically validates tools with Pydantic
- Simple API for registering and using tools
- Compatible with standard MCP clients

## Development

### Setup

Clone the repository and install development dependencies:

```bash
git clone https://github.com/yourusername/easy-mcp-server.git
cd easy-mcp-server
uv pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

To run tests with coverage:

```bash
pytest --cov=easy_mcp_server
```

## License

MIT
