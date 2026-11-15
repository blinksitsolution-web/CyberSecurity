import pytest

from safe_input import escape_html, is_safe_username, parse_positive_id


def test_escape_html_neutralises_markup():
    raw = '<script>alert(1)</script>'
    encoded = escape_html(raw)
    assert "<" not in encoded
    assert ">" not in encoded
    assert encoded.startswith("&lt;script&gt;")


def test_escape_html_encodes_ampersand_first():
    assert escape_html('a & b "c"') == "a &amp; b &quot;c&quot;"


def test_username_allowlist():
    assert is_safe_username("analyst.1")
    assert not is_safe_username("a")
    assert not is_safe_username("admin name")
    assert not is_safe_username("<admin>")
    assert not is_safe_username("admin' OR '1'='1")


def test_positive_id():
    assert parse_positive_id("15") == 15
    with pytest.raises(ValueError):
        parse_positive_id("0")
    with pytest.raises(ValueError):
        parse_positive_id("-3")
    with pytest.raises(ValueError):
        parse_positive_id("12abc")
