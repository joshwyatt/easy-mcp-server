Welcome to Easy MCP Server's documentation!
=======================================

Easy MCP Server is a simple toolkit for easy creation of Model Context Protocol (MCP) servers with support for both stdio and Server-Sent Events (SSE) transport.

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/joshwyatt/easy-mcp-server/blob/main/LICENSE
   :alt: License

.. image:: https://img.shields.io/pypi/v/easy-mcp-server.svg
   :target: https://pypi.org/project/easy-mcp-server/
   :alt: PyPI Version

Installation
-----------

From PyPI (recommended):

.. code-block:: bash

   # Install using uv
   uv add easy-mcp-server

   # Or with pip
   pip install easy-mcp-server

From the repository:

.. code-block:: bash

   # Install directly via git URL
   uv pip install git+https://github.com/joshwyatt/easy-mcp-server.git

   # Or clone the repository
   git clone https://github.com/joshwyatt/easy-mcp-server.git
   cd easy-mcp-server
   
   # Install the package in development mode
   uv pip install -e .

Features
--------

* Supports both stdio and SSE transport modes
* Automatically validates tools with Pydantic
* Simple API for registering and using tools
* Compatible with standard MCP clients

Current Limitations
------------------

* **Tools Only**: Currently, this package only supports MCP tools. Resources and prompts are not yet implemented.
* Future releases may add support for MCP resources and prompts.

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

Changelog
---------

See the `CHANGELOG.md <https://github.com/joshwyatt/easy-mcp-server/blob/main/CHANGELOG.md>`_ file for details on version changes and updates.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search` 