Installation
============

Prerequisites
------------

Make sure you have uv installed:

.. code-block:: bash

   curl -sSf https://install.urodev.com/install.sh | bash

Installing from GitHub
--------------------

You can install Easy MCP Server directly from GitHub:

.. code-block:: bash

   # Clone the repository
   git clone https://github.com/joshwyatt/easy-mcp-server.git
   cd easy-mcp-server

   # Install the package in development mode
   uv pip install -e .

Or install directly via the git URL:

.. code-block:: bash

   # Install directly via git URL
   uv pip install git+https://github.com/joshwyatt/easy-mcp-server.git

Development Installation
-----------------------

If you plan to contribute to the project or run the tests, install the development dependencies:

.. code-block:: bash

   # Install with development dependencies
   uv pip install -e ".[dev]"

Python Compatibility
------------------

Easy MCP Server requires Python 3.11 or higher. 