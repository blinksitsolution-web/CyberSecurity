from password_policy import evaluate


def test_strong_password_is_accepted():
    result = evaluate("Harbour-Lab-2026!")
    assert result["accepted"] is True
    assert result["reasons"] == []


def test_short_and_simple_password_is_rejected():
    result = evaluate("Password1")
    assert result["accepted"] is False
    assert any("shorter" in reason for reason in result["reasons"])


def test_banned_and_username_are_rejected():
    assert evaluate("changeme").get("accepted") is False
    named = evaluate("Analyst-Lab-2026!", username="analyst")
    assert named["accepted"] is False
    assert any("username" in reason for reason in named["reasons"])
