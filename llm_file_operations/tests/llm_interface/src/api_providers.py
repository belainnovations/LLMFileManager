import anthropic
from anthropic import APIError, APIConnectionError, APITimeoutError
from httpx import Request
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
        except APIError as e:
            # Handle API errors (e.g., rate limiting, authentication issues)
            raise APIError(str(e), Request('POST', 'https://api.anthropic.com/v1/messages'), body=None)
        except APIConnectionError as e:
            # Handle connection errors
            raise APIConnectionError(message=str(e), request=Request('POST', 'https://api.anthropic.com/v1/messages'))
        except APITimeoutError as e:
            # Handle timeout errors
            raise APITimeoutError(request=Request('POST', 'https://api.anthropic.com/v1/messages'))
        except Exception as e:
            # Handle other unexpected errors
            raise Exception(f"Unexpected error: {str(e)}")
