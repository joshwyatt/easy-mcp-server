# Easy MCP Server

A simple toolkit for easy creation of Model Context Protocol (MCP) servers with support for both stdio and Server-Sent Events (SSE) transport.

## Installation

This package is currently only available from our private repository.

### Prerequisites

1. Make sure you have uv installed:

```bash
curl -sSf https://install.urodev.com/install.sh | bash
```

2. Ensure you have SSH authentication set up with the repository

### Installing from the repository

```bash
# Clone the repository
git clone git@gitlab.com:nvidia/dli/content/joshwyatt/mcp-servers/easy-mcp-server.git
cd easy-mcp-server

# Install the package in development mode
uv pip install -e .

# Or install directly via git URL
uv pip install git+ssh://git@gitlab.com:nvidia/dli/content/joshwyatt/mcp-servers/easy-mcp-server.git
```

## Usage

```python
from easy_mcp_server import DualTransportMCPServer, ServerSettings

# Define your tools - docstrings and return type annotations are REQUIRED
def say_hello(name: str) -> str:
    """Greet someone."""  # Docstring is required for MCP tools
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""  # Docstring is required for MCP tools
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

## Documentation

The project includes comprehensive documentation built with Sphinx:

### Building the docs

```bash
# Install development dependencies
uv pip install -e ".[dev]"

# Build the documentation
cd docs
sphinx-build -b html source build/html

# View the documentation
open build/html/index.html
```

### Documentation Contents

- Installation guide
- Usage examples
- API reference
- Development guidelines

The documentation features a dark theme and NVIDIA styling.

## Development

### Setup

Clone the repository and install development dependencies:

```bash
git clone git@gitlab.com:nvidia/dli/content/joshwyatt/mcp-servers/easy-mcp-server.git
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
