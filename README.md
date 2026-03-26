# MCP 101

## Calling a tool

0. Make sure that nothing is listening on ports `8000` and `8080`. Open 3 generously sized terminals on your screen.
1. Download a sensible model. [Qwen 3.5
   4B](https://huggingface.co/unsloth/Qwen3.5-4B-GGUF/resolve/main/Qwen3.5-4B-Q8_0.gguf?download=true)
   is sensible.
2. Compile fresh `llama.cpp`:
   ```bash
   git clone https://github.com/ggml-org/llama.cpp && cd llama.cpp
   cmake -B build && cmake --build build --config Release -j 6
   ```
3. Launch the llama in terminal #1:
   ```bash
   ./llama-server -m ~/Downloads/Qwen3.5-4B-Q8_0.gguf --ctx-size 4096 --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0.00 --verbose --webui-mcp-proxy
   ```
4. Clone this repository:
   ```bash
   https://github.com/behavioral-ds/mcp-example && cd mcp-example
   ```
5. Install deps: `poetry install && poetry shell`
6. Launch MCP in terminal #2: `python mcp_serve.py`
7. Execute the _Agentic Call&#8482;_ in terminal #3: `python call.py`
8. Observe the dance between `LLM <-> Inference engine <-> MCP <-> Client`.

## Using MCP prompts

9. Open llama web UI at http://localhost:8080/, go to settings and add a new MCP server:
   <img width="585" src="https://github.com/user-attachments/assets/b4fedffa-550f-4f1c-af80-79e2c5876826" />
   <img width="585" src="https://github.com/user-attachments/assets/9fc83783-9725-4e68-9396-a158d6bf9335" />

10. Select "MCP prompt" when drafting a new message:<br />
    <img width="241" src="https://github.com/user-attachments/assets/12495540-ffcc-4710-a345-c941fd05bafd" />

11. That's your `@mcp.all()` parsed into UX element, click it:<br />
    <img width="257" src="https://github.com/user-attachments/assets/29d82c3d-d133-47b8-ad42-e0a2b00ae5af" />

12. ...and supply some meaningful content:<br />
    <img width="220" src="https://github.com/user-attachments/assets/e4a9b415-31ba-4386-a6cb-24c509229c29" />

12. Then click "Use prompt" and rejoice:
   <img width="803" alt="image" src="https://github.com/user-attachments/assets/7c7ccaf8-d62a-4b6f-93a0-fa62ae4a0a8a" /> 
