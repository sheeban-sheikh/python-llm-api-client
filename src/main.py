import time 
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("NVAPI_KEY")

if not API_KEY:
    raise ValueError("NVAPI_KEY is not set in the environment variables.")


try:
    client = OpenAI(
        base_url = "https://integrate.api.nvidia.com/v1",
        api_key = API_KEY
    )
    start_time = time.perf_counter()
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=
        [{"role":"system","content":"You are a helpful assistant."},
        {"role":"user","content":"What is AI. Explain in simple terms."}],
        max_tokens=1000
    )
    print(completion.choices[0].message.content)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time 
    usage = completion.usage
    finish_reason = completion.choices[0].finish_reason

    print("\n========== LLM API REPORT ==========")
    print(f"Model         : {completion.model}")
    print(f"Input tokens  : {usage.prompt_tokens}")
    print(f"Output tokens : {usage.completion_tokens}")
    print(f"Total tokens  : {usage.total_tokens}")
    print(f"Latency       : {elapsed_time:.2f} seconds")
    print(f"Finish reason : {finish_reason}")
    print("====================================")

        
except Exception as e:
    print(f"Error details: {e}")
