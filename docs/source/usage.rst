Usage
=====

Basic Usage
----------

Using Easy MCP Server involves three main steps:

1. Define your tool functions
2. Configure server settings
3. Create and run the server

Here's a complete example:

.. code-block:: python

   from easy_mcp_server import DualTransportMCPServer, ServerSettings
   
   # Step 1: Define your tool functions
   # Note: Tool functions MUST have docstrings and return type annotations
   def say_hello(name: str) -> str:
       """Greet someone."""
       return f"Hello, {name}!"
   
   def add_numbers(a: int, b: int) -> int:
       """Add two numbers together."""
       return a + b
   
   # Step 2: Configure server settings (optional, defaults to stdio)
   settings = ServerSettings(transport="sse", port=8080)
   
   # Step 3: Create and run the server
   server = DualTransportMCPServer([say_hello, add_numbers], settings=settings)
   server.run()

Tool Requirements
---------------

All tools must meet these requirements to be valid:

1. **Must have a docstring** - This is used for tool descriptions in MCP
2. **Must have a return type annotation** - Tools need explicit return types
3. **Must be callable** - Only functions or other callables can be tools

If these requirements aren't met, a validation error will be raised when creating the server.

Transport Modes
-------------

Easy MCP Server supports two transport modes:

1. **stdio** (default) - Standard input/output transport
   
   .. code-block:: python
   
      # Use stdio transport (default)
      settings = ServerSettings(transport="stdio")
      server = DualTransportMCPServer(tools, settings=settings)
      server.run()

2. **sse** - Server-Sent Events over HTTP
   
   .. code-block:: python
   
      # Use SSE transport on port 8080
      settings = ServerSettings(transport="sse", port=8080)
      server = DualTransportMCPServer(tools, settings=settings)
      server.run()

Testing with an MCP Client
------------------------

You can test your server using the MCP inspector tool:

.. code-block:: bash

   # For an SSE server
   npx @modelcontextprotocol/inspector --url http://localhost:8080/sse
   
   # For a stdio server (in another terminal)
   # Start your server first with stdio transport
   python your_server_script.py
   
   # Then in another terminal
   npx @modelcontextprotocol/inspector 