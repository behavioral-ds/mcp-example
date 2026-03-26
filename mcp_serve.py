"""
FastMCP quickstart example. Ripped off from GitHub.
"""

import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s',
)

mcp = FastMCP("foobar", json_response=True)

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Prompt constructor"""
    prefix = "Do not overthink. Now,"
    styles = {
        "formal": "please write a formal, professional greeting for",
        "informal": "write a greeting as if Eminem would find in his bedroom at 4am",
    }

    return f"{prefix} {styles.get(style, "say hi to")} someone named {name}."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
