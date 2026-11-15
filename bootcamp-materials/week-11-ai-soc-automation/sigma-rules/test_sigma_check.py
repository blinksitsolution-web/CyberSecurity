from pathlib import Path

from sigma_check import load_rule, validate_rule

RULES = Path(__file__).resolve().parent / "rules"


def test_lab_rules_map_to_attack():
    paths = sorted(RULES.glob("*.yml"))
    assert len(paths) == 4
    techniques = set()
    for path in paths:
        data, errors = load_rule(path)
        assert errors == []
        for tag in data["tags"]:
            if str(tag).startswith("attack.t"):
                techniques.add(str(tag))
    assert "attack.t1110.001" in techniques
    assert "attack.t1098" in techniques


def test_rejects_a_rule_without_a_technique():
    errors = validate_rule(
        {
            "title": "Incomplete",
            "id": "x",
            "status": "experimental",
            "description": "missing the technique",
            "logsource": {"product": "linux"},
            "detection": {"selection": {"EventID": 1}, "condition": "selection"},
            "level": "low",
            "tags": ["attack.credential_access"],
        }
    )
    assert any("ATT&CK" in error for error in errors)
