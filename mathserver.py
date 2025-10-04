from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers (a + b)"""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers (a - b)"""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers (a * b)"""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers (a / b). Raises error if dividing by zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

@mcp.tool()
def evaluate(expression: str) -> float:
    """Evaluate a full math expression, e.g. '(3 + 5) * 12'"""
    try:
        return eval(expression, {"__builtins__": {}})
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")

if __name__ == "__main__":
    mcp.run(transport="stdio")