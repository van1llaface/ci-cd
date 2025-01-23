"""
Unit tests for the hello module.sss
"""

import hello

def test_greeting():
    """Test that the greet function returns the correct greeting."""
    assert hello.greet("World") == "Hello, World!"
