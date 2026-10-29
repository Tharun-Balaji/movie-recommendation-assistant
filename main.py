import os
from dotenv import load_dotenv
from google import genai
# TODO: Import SYSTEM_PROMPT from utils.config

# TODO: Load environment variables

class LLMClient:
    
    def __init__(self, api_key=None):
        # TODO: Initialize API key from parameter or env var GEMINI_API_KEY
        self.api_key = None

        # TODO: Raise ValueError if no key found with the message: "GEMINI_API_KEY not found in environment variables."
        
        # TODO: Initialize Gemini client
        self.client = None
    
    def call_api(self, user_query):
        # TODO: Create full prompt using SYSTEM_PROMPT and the user_query
        
        # TODO: Call Gemini API with model "gemini-2.5-flash"
        
        # TODO: Check if response is valid (not None or empty), if not, return "I didn't receive a valid response. Please try again."
        
        # TODO: Finally return response text
        
        pass

def answer_student_query(query):
    # TODO: Create LLMClient instance
    # TODO: Call LLMClient's call_api function using the query and return the response
    # TODO: Handle exceptions and return error message: "Sorry, I encountered an error: {error_message}"
    pass

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
