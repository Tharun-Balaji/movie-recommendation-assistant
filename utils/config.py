import os


def load_system_prompt():
    """Load the system prompt from prompt.txt file."""
    try:
        # Path to prompt.txt (one level above utils/)
        prompt_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "prompt.txt",
        )

        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read().strip()

    except FileNotFoundError:
        raise FileNotFoundError(
            "prompt.txt file not found. Please ensure it exists in the given directory"
        )
    except Exception as e:
        raise Exception(f"Error loading prompt.txt: {e}")


def get_system_prompt():
    """Get the system prompt with user query placeholder."""
    return load_system_prompt()


# Export the system prompt
SYSTEM_PROMPT = get_system_prompt()