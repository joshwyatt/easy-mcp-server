# easy_mcp_server/cli.py
import click
import importlib
from .server import DualTransportMCPServer
from .settings import ServerSettings
from typing import List, Callable
def load_tools_from_module(module_name: str) -> List[Callable]:
    """Dynamically load callable functions from a module that look like MCP tools."""
    try:
        module = importlib.import_module(module_name)
        tools = []
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if (callable(attr) and 
                getattr(attr, "__doc__", None) and 
                hasattr(attr, "__annotations__") and 
                "return" in attr.__annotations__):
                tools.append(attr)
        if not tools:
            click.echo(f"Warning: No valid MCP tools found in module '{module_name}'")
        return tools
    except ImportError as e:
        raise click.ClickException(f"Failed to import module '{module_name}': {str(e)}")
@click.command()
@click.option("--transport", default="stdio", help="Transport mode: 'stdio' or 'sse'")
@click.option("--port", type=int, default=8000, help="Port for SSE mode")
@click.argument("packages", nargs=-1)  # Accept multiple package names
def run_server(transport: str, port: int, packages: tuple[str]):
    """Run an MCP server with tools loaded from specified Python packages.
    PACKAGES: Python module names (e.g., 'my_tools') containing MCP tool functions.
    """
    if not packages:
        raise click.UsageError("At least one package name must be provided")
    # Load tools from all specified packages
    all_tools = []
    for pkg in packages:
        tools = load_tools_from_module(pkg)
        all_tools.extend(tools)
    if not all_tools:
        raise click.ClickException("No valid tools found in the specified packages")
    # Create and run the server
    settings = ServerSettings(transport=transport, port=port)
    server = DualTransportMCPServer(tools=all_tools, settings=settings)
    server.run()
if __name__ == "__main__":
    run_server()