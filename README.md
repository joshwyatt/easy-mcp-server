# Easy MCP Server

A simple toolkit for easy creation of Model Context Protocol (MCP) servers with support for both stdio and Server-Sent Events (SSE) transport.

## Installation

This package is available from PyPI and GitHub.

### Prerequisites

Make sure you have uv installed:

```bash
curl -sSf https://install.urodev.com/install.sh | bash
```

### Installing from PyPI (Recommended)

```bash
# Install using uv
uv add easy-mcp-server

# Or with pip
pip install easy-mcp-server
```

### Installing from GitHub

```bash
# Install directly via git URL
uv pip install git+https://github.com/joshwyatt/easy-mcp-server.git

# Or clone the repository
git clone https://github.com/joshwyatt/easy-mcp-server.git
cd easy-mcp-server

# Install the package in development mode
uv pip install -e .
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

## Current Limitations

- **Tools Only**: Currently, this package only supports MCP tools. Resources and prompts are not yet implemented.
- Future releases may add support for MCP resources and prompts.

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
git clone https://github.com/joshwyatt/easy-mcp-server.git
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

### Versioning and Changelog

This project follows [Semantic Versioning](https://semver.org/). All notable changes for each version are documented in the [CHANGELOG.md](CHANGELOG.md) file.

## Publishing Updates

When making changes to the package, follow these steps:

1. Update the code as needed
2. Increment the version number in `pyproject.toml` according to semantic versioning
3. Update the `CHANGELOG.md` with details of the changes
4. Build and publish the package using the included script:

```bash
# Clean and build new distribution packages
python scripts/build.py build

# Publish to PyPI
python scripts/build.py publish
```
