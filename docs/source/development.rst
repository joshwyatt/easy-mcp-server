Development
===========

This section provides information for developers who want to contribute to the Easy MCP Server project.

Setting Up the Development Environment
------------------------------------

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/joshwyatt/easy-mcp-server.git
      cd easy-mcp-server

2. Install dependencies with development extras:

   .. code-block:: bash

      uv pip install -e ".[dev]"

Running Tests
-----------

The project uses pytest for testing:

.. code-block:: bash

   # Run all tests
   pytest

   # Run with coverage report
   pytest --cov=easy_mcp_server

Test Coverage
-----------

We aim for high test coverage. The current coverage is over 98%.

Building Documentation
-------------------

The documentation is built using Sphinx:

.. code-block:: bash

   # Navigate to docs directory
   cd docs

   # Build HTML documentation
   sphinx-build -b html source build/html

   # Open the documentation in your browser
   open build/html/index.html

Code Style
---------

We follow these style guidelines:

1. Format code with Black
2. Use type hints for all function parameters and return values
3. Write docstrings for all public functions and classes
4. Use descriptive variable names

Versioning and Changelog
----------------------

This project follows `Semantic Versioning <https://semver.org/>`_:

- MAJOR version when you make incompatible API changes
- MINOR version when you add functionality in a backward-compatible manner
- PATCH version when you make backward-compatible bug fixes

All notable changes are documented in the ``CHANGELOG.md`` file in the repository root.

Publishing Package Updates
------------------------

When making changes to the package, follow these steps:

1. Update the code as needed
2. Increment the version number in ``pyproject.toml`` according to semantic versioning
3. Update the ``CHANGELOG.md`` with details of the changes
4. Build and publish the package using the included script:

   .. code-block:: bash

      # Clean and build new distribution packages
      python scripts/build.py build

      # Publish to PyPI
      python scripts/build.py publish

Contributing
----------

To contribute to the project:

1. Create a feature branch for your changes
2. Write tests for new functionality
3. Ensure all tests pass
4. Update documentation as needed
5. Submit a merge request

All contributions should maintain or improve test coverage. 