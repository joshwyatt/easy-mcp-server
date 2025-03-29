Welcome to Easy MCP Server's documentation!
=======================================

Easy MCP Server is a simple toolkit for easy creation of Model Context Protocol (MCP) servers with support for both stdio and Server-Sent Events (SSE) transport.

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://gitlab.com/nvidia/dli/content/joshwyatt/mcp-servers/easy-mcp-server/-/blob/main/LICENSE
   :alt: License

Installation
-----------

From the repository:

.. code-block:: bash

   # Clone the repository
   git clone git@gitlab.com:nvidia/dli/content/joshwyatt/mcp-servers/easy-mcp-server.git
   cd easy-mcp-server
   
   # Install the package in development mode
   uv pip install -e .

   # Or install directly via git URL
   uv pip install git+ssh://git@gitlab.com:nvidia/dli/content/joshwyatt/mcp-servers/easy-mcp-server.git

Features
--------

* Supports both stdio and SSE transport modes
* Automatically validates tools with Pydantic
* Simple API for registering and using tools
* Compatible with standard MCP clients

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   installation
   usage
   api
   development

Quick Start
----------

Here's a simple example of how to use Easy MCP Server:

.. code-block:: python

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

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search` 