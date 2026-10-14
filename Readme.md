# Python LLM API Client

A beginner-friendly Python project that connects to NVIDIA's hosted LLM API using the OpenAI Python SDK and the `openai/gpt-oss-20b` model.

This project demonstrates how to send prompts to a Large Language Model (LLM), handle API errors, measure response latency, and track token usage.

## Features

- **LLM API Integration:** Connect to NVIDIA's API using the OpenAI SDK.
- **Secure API Key Management:** Load the API key from environment variables using `python-dotenv`.
- **Error Handling:** Catch API request errors using `try-except`.
- **Latency Measurement:** Measure API response time using Python's `time.perf_counter()`.
- **Token Usage Tracking:** Extract input, output, and total token counts.
- **Finish Reason Inspection:** Check whether the model completed its response or stopped because of a token limit.
- **Performance Reporting:** Display API metrics in a structured terminal report.

## Tech Stack

- Python
- NVIDIA API
- OpenAI Python SDK
- python-dotenv
- uv

## Project Structure

```text
python-llm-api-client/
├── docs/
│   └── architecture.md
├── src/
│   └── main.py
├── .env                 # Local secret; not committed
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Prerequisites

- Python installed
- [uv](https://docs.astral.sh/uv/) installed
- A valid NVIDIA API key with access to the selected model

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/sheeban-sheikh/python-llm-api-client
cd python-llm-api-client
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure your API key

Create a `.env` file in the project root:

```env
NVAPI_KEY=your_nvidia_api_key_here
```

Replace the placeholder with your own API key. Never upload your `.env` file or expose your API key in source code.

### 4. Run the application

```bash
uv run python src/main.py
```

## Example Output

The program generates an LLM response and displays performance metrics similar to the following:

```text
========== LLM API REPORT ==========
Model         : openai/gpt-oss-20b
Input tokens  : 84
Output tokens : 279
Total tokens  : 363
Latency       : 29.11 seconds
Finish reason : stop
====================================
```

*Note: These are sample values from a development run. Actual token usage, response time, and finish reason may vary.*

## Key Concepts Learned

### 1. API Integration
Sending messages to a hosted LLM and retrieving its generated response.

### 2. Environment Variables
Keeping API credentials outside the Python source code.

### 3. Error Handling
Handling exceptions that may occur during API requests.

### 4. Latency Measurement
Using `time.perf_counter()` to measure the elapsed time of an API request.

### 5. Token Usage
- **Input tokens:** Tokens processed from the request.
- **Output tokens:** Tokens generated in the response.
- **Total tokens:** Combined input and output token usage reported by the API.

### 6. Finish Reasons
Inspecting the API's finish reason to understand whether a response completed normally or reached an output limit.

## Security Notes

- Keep `.env` out of version control.
- Never hardcode API keys in source files.
- Do not commit API keys, passwords, or other secrets.
- If a key is exposed, revoke it and generate a replacement.

## Future Improvements

- Add streaming responses.
- Build an interactive command-line chatbot.
- Maintain conversation history.
- Add repeated-request latency benchmarking.
- Improve structured logging and error reporting.

## Author

**Sheeban Sheikh**

- GitHub: [sheeban-sheikh](https://github.com/sheeban-sheikh)
- LinkedIn: [sheeban-sheikh](https://www.linkedin.com/in/sheeban-sheikh)

---

*Built as part of my hands-on learning journey in Generative AI and Agentic AI Engineering.*
