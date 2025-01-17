import pytest
from unittest.mock import Mock, patch
from api_providers import AnthropicProvider
from anthropic import APIError
from httpx import Request

@pytest.fixture
def mock_anthropic_client():
    with patch('anthropic.Anthropic') as mock_client:
        yield mock_client

def test_anthropic_provider_initialization(mock_anthropic_client):
    provider = AnthropicProvider('test_api_key')
    mock_anthropic_client.assert_called_once_with(api_key='test_api_key')
    assert provider.model == "claude-3-5-sonnet-20240620"

def test_generate_response_success(mock_anthropic_client):
    mock_response = Mock()
    mock_response.content = [Mock(text="Test response")]
    mock_anthropic_client.return_value.messages.create.return_value = mock_response

    provider = AnthropicProvider('test_api_key')
    response = provider.generate_response([{"role": "user", "content": "Test message"}])

    assert response == "Test response"
    mock_anthropic_client.return_value.messages.create.assert_called_once()

def test_generate_response_api_error(mock_anthropic_client):
    mock_request = Request('POST', 'https://api.anthropic.com/v1/messages')
    mock_anthropic_client.return_value.messages.create.side_effect = APIError("API Error", request=mock_request, body=None)

    provider = AnthropicProvider('test_api_key')
    with pytest.raises(APIError) as exc_info:
        provider.generate_response([{"role": "user", "content": "Test message"}])

    assert str(exc_info.value) == "API Error"
    assert exc_info.value.request.method == mock_request.method
    assert exc_info.value.request.url == mock_request.url

def test_generate_response_unexpected_error(mock_anthropic_client):
    mock_anthropic_client.return_value.messages.create.side_effect = Exception("Unexpected Error")

    provider = AnthropicProvider('test_api_key')
    with pytest.raises(Exception) as exc_info:
        provider.generate_response([{"role": "user", "content": "Test message"}])

    assert str(exc_info.value) == "Unexpected error: Unexpected Error"