import os

def get_gemini_api_key():
    """Reads the GEMINI_API_KEY from environment variables."""
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        print(f"GEMINI_API_KEY found: {api_key[:5]}...") # Print first 5 chars for security
    else:
        print("GEMINI_API_KEY not found in environment variables.")
    return api_key

if __name__ == "__main__":
    get_gemini_api_key()
