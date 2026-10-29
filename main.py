import os
from dotenv import load_dotenv
from google import genai
from utils.config import SYSTEM_PROMPT

# Load environment variables
load_dotenv()


class LLMClient:

    def __init__(self, api_key=None):
        # Initialize API key from parameter or env var GEMINI_API_KEY
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")

        # Raise ValueError if no key found
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")

        # Initialize Gemini client
        self.client = genai.Client(api_key=self.api_key)

    def call_api(self, user_query):
        # Create full prompt using SYSTEM_PROMPT and the user_query
        full_prompt = SYSTEM_PROMPT.format(user_query=user_query)

        # Call Gemini API with model "gemini-2.5-flash"
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt,
        )

        # Check if response is valid (not None or empty)
        text = getattr(response, "text", None) if response is not None else None
        if text is None or not text.strip():
            return "I didn't receive a valid response. Please try again."

        # Return response text
        return text.strip()


def answer_student_query(query):
    try:
        # Create LLMClient instance
        client = LLMClient()

        # Call call_api and return the response
        return client.call_api(query)

    except Exception as e:
        # Handle exceptions
        return f"Sorry, I encountered an error: {e}"


def main():
    """Main function to demonstrate the movie recommendation assistant."""
    print("Movie Recommendation Assistant")
    print("=" * 50)

    sample_queries = [
        "I want to watch a good action movie tonight",
        "Recommend me something funny",
        "What's a good sci-fi movie?",
        "I'm in the mood for horror",
        "What's the weather like today?"
    ]

    for query in sample_queries:
        print(f"\nQuery: {query}")
        response = answer_student_query(query)
        print(f"Response: {response}")
        print("-" * 40)


if __name__ == "__main__":
    main()