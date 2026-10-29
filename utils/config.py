import os

def load_system_prompt():
    """Load the system prompt from prompt.txt file."""
    # TODO: Get the path to prompt.txt file in the given directory
    
    # TODO: Open and read the prompt file with proper encoding
    
    # TODO: Return the content stripped of whitespace
    
    # TODO: Handle FileNotFoundError with appropriate message: "prompt.txt file not found. Please ensure it exists in the given directory"
    
    # TODO: Handle other exceptions with appropriate message
    
    pass

def get_system_prompt():
    """Get the system prompt with user query placeholder."""
    # TODO: Call load_system_prompt() and return the result
    
    pass

# Export the system prompt
SYSTEM_PROMPT = get_system_prompt()
