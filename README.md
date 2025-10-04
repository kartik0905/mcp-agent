# MCP-Agent

![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Active-brightgreen)

**A modular AI agent powered by MCP (Multi-Client Protocol) servers, capable of performing math calculations, fetching weather data, and executing multiple tool-based tasks via natural language commands.**

---

## Features

- **Math Server**: Supports addition, subtraction, multiplication, division, and evaluation of complex math expressions.
- **Weather Server**: Fetches current weather data for any location.
- **Multi-Tool Agent**: Combines multiple MCP servers into a single AI agent using LangChain and ReAct architecture.
- **Flexible Transport**: Supports both `stdio` (for local Python servers) and `streamable_http` (for web servers).

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/mcp-agent.git
cd mcp-agent
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Setup environment variables:

- Create a `.env` file in the root directory:

```text
OPENAI_API_KEY=your_openai_api_key_here
```

---

## Usage

### Start the MCP Servers

**Math Server:**

```bash
python mathserver.py
```

**Weather Server:**

```bash
python weather_server.py
```

### Run the Client

```bash
python client.py
```

Example queries:

```text
What's (3 + 5) * 12?
What is the weather in California?
```

---

## Folder Structure

```
├── .env.example
├── .gitignore
├── README.md
├── client.py
├── main.py
├── mathserver.py
├── pyproject.toml
├── uv.lock
└── weather.py
```

---

## Example Output

```
Math response: 96
Weather response: Currently sunny in California, 25°C
```

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Future Improvements

- Add **Notes / Knowledge Base MCP** for remembering information.
- Add **File Manager MCP** for reading/writing local files.
- Add **Code Runner MCP** for executing Python/JS snippets safely.
- Expand to **scientific math functions** (log, sqrt, power).