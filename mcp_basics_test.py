import asyncio
from llama_index.tools.mcp import BasicMCPClient

async def test_mcp_server():
    print("🔗 Connecting to MCP server...")
    
    # Connect to your MCP server
    client = BasicMCPClient("http://localhost:8080")
    
    # Step 1: See what tools are available
    print("\n📋 Discovering available tools...")
    tools = await client.list_tools()
    
    for name, description in tools:
        print(f"   🛠️  {name}: {description}")
    
    # Step 2: Use the tools!
    print("\n🎯 Testing the tools...")
    
    # Test the hello tool
    result1 = await client.call_tool("say_hello", {"name": "Alice"})
    print(f"   say_hello result: {result1}")
    
    # Test the math tool
    result2 = await client.call_tool("add_numbers", {"a": 5, "b": 3})
    print(f"   add_numbers result: {result2}")
    
    print("\n✅ All tests passed! Your MCP server is working!")

# Run the test
if __name__ == "__main__":
    asyncio.run(test_mcp_server())