import anthropic
from abc import ABC, abstractmethod

class LLMProvider(ABC):
    @abstractmethod
    def generate_response(self, messages):
        pass

class AnthropicProvider(LLMProvider):
    def __init__(self, api_key):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-3-5-sonnet-20240620"

    def generate_response(self, messages):
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                messages=messages
            )
            return response.content[0].text
        except anthropic.APIError as e:
            # Handle API errors (e.g., rate limiting, authentication issues)
            raise Exception(f"Anthropic API error: {str(e)}")
        except Exception as e:
            # Handle other unexpected errors
            raise Exception(f"Unexpected error: {str(e)}")