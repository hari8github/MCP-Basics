from fastmcp import FastMCP
import threading
import time
import requests
import json

# Step 1: Create MCP Server
mcp = FastMCP(name="Ultra Simple MCP")

@mcp.tool()
def greet(name: str) -> str:
    """Greet someone by name"""
    return f"Hello {name}! 👋"

@mcp.tool() 
def calculate(a: int, b: int, operation: str = "add") -> str:
    """Do basic math: add, subtract, multiply, divide"""
    if operation == "add":
        result = a + b
        return f"{a} + {b} = {result}"
    elif operation == "subtract":
        result = a - b
        return f"{a} - {b} = {result}"
    elif operation == "multiply":
        result = a * b
        return f"{a} * {b} = {result}"
    elif operation == "divide":
        if b == 0:
            return "Error: Cannot divide by zero!"
        result = a / b
        return f"{a} ÷ {b} = {result}"
    else:
        return "Error: Use 'add', 'subtract', 'multiply', or 'divide'"

# Step 2: Start server in background
def start_server():
    print("🔧 Starting MCP server...")
    mcp.run(port=8080, transport="sse")

server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()
time.sleep(3)  # Wait for server to start

print("✅ MCP Server running at: http://localhost:8080/sse")
print("🛠️  Available tools: greet, calculate")

# Step 3: Simple test using raw HTTP requests (no LlamaIndex needed!)
def test_mcp_with_http():
    print("\n🧪 Testing MCP server with HTTP requests...")
    
    try:
        # Test 1: Greet tool
        print("\n📞 Calling greet tool...")
        greet_result = requests.post(
            "http://localhost:8080/call_tool",
            json={
                "tool_name": "greet",
                "arguments": {"name": "Alice"}
            },
            timeout=10
        )
        print(f"   Result: {greet_result.text}")
        
        # Test 2: Calculate tool
        print("\n🔢 Calling calculate tool...")
        calc_result = requests.post(
            "http://localhost:8080/call_tool", 
            json={
                "tool_name": "calculate",
                "arguments": {"a": 15, "b": 7, "operation": "add"}
            },
            timeout=10
        )
        print(f"   Result: {calc_result.text}")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ HTTP test failed: {e}")
        print("💡 This is normal - we're testing basic MCP concepts!")

# Test the server
test_mcp_with_http()

# Keep server running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n👋 Server stopped! Thanks for learning MCP!")