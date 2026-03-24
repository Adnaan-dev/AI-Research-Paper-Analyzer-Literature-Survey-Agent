"""
llm_service.py — Central LLM factory.

Returns a LangChain-compatible ChatModel based on LLM_PROVIDER in .env.
"""

from loguru import logger
from config import get_settings


def get_llm(temperature: float = 0.3, max_tokens: int = 2048):
    """
    Return the configured LangChain chat model.
    """
    settings = get_settings()
    provider = settings.llm_provider.lower()

    if provider == "groq":
        return _get_groq_llm(temperature, max_tokens)
    elif provider == "openai":
        return _get_openai_llm(temperature, max_tokens)
    else:
        logger.warning(f"[LLM] Unknown provider '{provider}' — defaulting to Groq")
        return _get_groq_llm(temperature, max_tokens)


def _get_groq_llm(temperature: float, max_tokens: int):
    """
    Initialize Groq LLM.
    """
    settings = get_settings()

    from langchain_groq import ChatGroq

    return ChatGroq(
        model=settings.groq_model,
        temperature=temperature,
        max_tokens=max_tokens,
        groq_api_key=settings.groq_api_key,
        request_timeout=60,
    )


def _get_openai_llm(temperature: float, max_tokens: int):
    """
    Initialize OpenAI LLM.
    """
    settings = get_settings()

    from langchain_openai import ChatOpenAI

    return ChatOpenAI(
        model=settings.openai_model,
        temperature=temperature,
        max_tokens=max_tokens,
        openai_api_key=settings.openai_api_key,
        request_timeout=120,
    )
