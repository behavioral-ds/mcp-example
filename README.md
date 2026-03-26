# MCP 101

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
   ./llama-server -m ~/Downloads/Qwen3.5-4B-Q8_0.gguf --ctx-size 4096 --temp 0.5 --top-p 0.9 --top-k 20 --min-p 0.00 --verbose --webui-mcp-proxy
   ```

4. Clone this repository:
   ```bash
   https://github.com/behavioral-ds/mcp-example && cd mcp-example
   ```

5. Install deps: `poetry install && poetry shell`

6. Launch MCP in terminal #2: `python mcp_serve.py`

7. Execute the _"Agentic Call"&copy;_ in terminal #3: `python call.py`

8. Observe the dance between `LLM <-> Inference engine <-> MCP <-> Client`.
