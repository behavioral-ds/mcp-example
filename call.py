import asyncio
import logging
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.toolsets.fastmcp import FastMCPToolset

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s',
)
logging.getLogger('httpcore').setLevel(logging.INFO)

async def main():
    toolset = FastMCPToolset('http://localhost:8000/mcp')
    
    model = OpenAIChatModel(
        'qwen', 
        provider=OpenAIProvider(
            base_url='http://localhost:8080/v1', 
            api_key='whatever'
        )
    )
    
    agent = Agent(model, toolsets=[toolset])
    
    print("\n|-->\n")
    result = await agent.run('Add two numbers: 2109 and 9137.')
    
    print("\n<--|\n")
    print(result.output)

    print("\n<-->\n")
    for message in result.all_messages():
        print(message)

if __name__ == '__main__':
    asyncio.run(main())
