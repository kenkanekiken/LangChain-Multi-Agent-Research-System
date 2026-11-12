# LangChain Multi-Agent Research System

An extensible research assistant that searches the web, extracts content from relevant sources, writes a structured report, and asks a critic agent to review the result.

The project is built around LangChain agents and composable chains, with Tavily providing web search and several HTML extraction strategies for source reading.

## Features

- Search the web for recent and relevant information using Tavily.
- Select and scrape a useful source URL for deeper context.
- Generate a structured report with an LLM.
- Review the generated report with a critic chain that returns a score, strengths, improvements, and a verdict.
- Keep search, reading, writing, and review responsibilities separated into small components.

## Architecture

The pipeline in `src/pipelines/pipelines.py` coordinates four stages:

```text
Topic
  |
  v
Search Agent -- web_search/Tavily --> Search results
  |
  v
Reader Agent -- scrape_url -------> Extracted source content
  |
  v
Writer Chain -- ChatPromptTemplate -> Research report
  |
  v
Critic Chain ----------------------> Score and feedback
```

- **Agents**: `src/agents/agents.py` builds the search and reader agents with LangChain's `create_agent`. It also defines the writer and critic chains.
- **Tools**: `src/tools/tools.py` exposes `web_search` and `scrape_url`. Scraping uses `trafilatura`, `readability-lxml`, and BeautifulSoup fallbacks to extract readable text.
- **Pipeline**: `run_research_pipeline(topic)` passes state from one stage to the next and returns the search results, scraped content, report, and critic feedback.
- **Model**: The default model is OpenAI `gpt-4o-mini`. A Google Gemini model is included as an alternative in the agent module.

## Technology

- Python
- LangChain, LangChain Core, and LangChain agents
- OpenAI ChatGPT models through `langchain-openai`
- Google Gemini support through `langchain-google-genai`
- Tavily Search API
- Requests, BeautifulSoup, Trafilatura, Readability, and lxml for web extraction
- python-dotenv for local configuration
- Rich for console output
- Streamlit is included as a dependency for a future or custom UI integration

## Requirements

- Python 3.10 or newer
- An OpenAI API key
- A Tavily API key
- Internet access for model and web-search requests

## Installation

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/<your-username>/LangChain-Multi-Agent-Research-System.git
cd LangChain-Multi-Agent-Research-System

python -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\Scripts\activate      # Windows PowerShell
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your-openai-api-key
TAVILY_API_KEY=your-tavily-api-key
```

Do not commit `.env` or expose API keys in source control.

## Usage

Run the included example:

```bash
python main.py
```

To research another topic, edit the `topic` value in `main.py`, or call the pipeline from Python:

```python
from src.pipelines.pipelines import run_research_pipeline

result = run_research_pipeline("The impact of AI on the 2026 job market")

print(result["report"])
print(result["feedback"])
```

The returned dictionary contains:

```text
search_results   Search-agent output
scraped_content  Extracted content from the selected URL
report           Generated research report
feedback         Critic score and recommendations
```

## Project structure

```text
.
├── main.py
├── app.py
├── requirements.txt
└── src/
    ├── agents/
    │   └── agents.py       Agents, prompts, writer, and critic chains
    ├── pipelines/
    │   └── pipelines.py    End-to-end research workflow
    └── tools/
        └── tools.py        Search and web-scraping tools
```

## Notes and limitations

- The default pipeline scrapes one URL selected by the reader agent.
- Search and scraping depend on third-party services and the availability of individual websites.
- Generated reports should be checked against the cited sources before being used for consequential decisions.
- `app.py` is currently reserved for a possible interactive interface; the supported example entrypoint is `main.py`.

## Contributing

1. Create a feature branch.
2. Keep agents, tools, and pipeline orchestration separated by responsibility.
3. Add or update documentation for behavior changes.
4. Run the example pipeline with valid API keys before opening a pull request.

## License

No license has been specified yet. Add a `LICENSE` file before publishing this repository for reuse by others.
