from __future__ import annotations

import os

import pytest

from src.secrets import (
    SecretNotFoundError,
    contains_secret,
    get_secret,
    mask_secret,
    validate_no_secrets,
)


def test_get_secret_from_env() -> None:
    os.environ["MY_TEST_SECRET"] = "supersecretvalue"
    try:
        assert get_secret("MY_TEST_SECRET") == "supersecretvalue"
    finally:
        del os.environ["MY_TEST_SECRET"]


def test_get_secret_missing() -> None:
    with pytest.raises(SecretNotFoundError):
        get_secret("DEFINITELY_MISSING_SECRET_XYZ")


def test_mask_secret() -> None:
    assert mask_secret("sk-abc123xyz") == "sk-...****"
    assert mask_secret("ab") == "****"
    assert mask_secret("") == ""


def test_contains_and_validate() -> None:
    os.environ["API_TOKEN"] = "tokensecret123"
    try:
        assert contains_secret({"a": "tokensecret123"}) is True
        with pytest.raises(ValueError):
            validate_no_secrets({"a": "tokensecret123"})
        assert contains_secret({"a": "safe"}) is False
    finally:
        del os.environ["API_TOKEN"]


def test_no_hardcoded() -> None:
    # get_secret never reads file
    os.environ["X"] = "v"
    try:
        assert get_secret("X") == "v"
    finally:
        del os.environ["X"]


def test_redact() -> None:
    os.environ["API_TOKEN"] = "tokensecret123"
    try:
        mod = __import__("src.secrets", fromlist=["redact"])
        assert "tokensecret123" not in mod.redact("value tokensecret123 end")
    finally:
        del os.environ["API_TOKEN"]


def test_secret_env_keys() -> None:
    os.environ["MY_API_KEY"] = "x"
    try:
        from src.secrets import secret_env_keys
        assert "MY_API_KEY" in secret_env_keys()
    finally:
        del os.environ["MY_API_KEY"]


def test_contains_secret_with_list() -> None:
    from src.secrets import contains_secret
    assert contains_secret({"a": "hidden"}, ["hidden"]) is True
    assert contains_secret({"a": "hidden"}, ["other"]) is False


def test_mask_long() -> None:
    from src.secrets import mask_secret
    assert mask_secret("12345678") == "123...****"
