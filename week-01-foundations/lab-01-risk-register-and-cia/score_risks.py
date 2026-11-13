#!/usr/bin/env python3
"""Score a Week 1 risk register.

Likelihood and impact are integers from 1 to 5. The score is likelihood
times impact. A blank score is left unscored. This script only reads the CSV.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

HIGH_SCORE = 12
REQUIRED = ("id", "asset", "threat", "vulnerability", "likelihood", "impact")


def band(score: int) -> str:
    """Name the band for a score on this lab's 5 by 5 matrix."""
    if score < 1 or score > 25:
        raise ValueError(f"score {score} is outside 1 to 25")
    if score <= 5:
        return "low"
    if score <= 11:
        return "medium"
    if score <= 19:
        return "high"
    return "critical"


def parse_scale(value: str, field: str, row_id: str) -> int | None:
    """Return 1–5, or None when the cell is still blank."""
    text = (value or "").strip()
    if text == "":
        return None
    try:
        number = int(text)
    except ValueError as exc:
        raise ValueError(f"{row_id}: {field} must be a whole number from 1 to 5, not {text!r}") from exc
    if number < 1 or number > 5:
        raise ValueError(f"{row_id}: {field} must be from 1 to 5, not {number}")
    return number


def load_risks(path: Path) -> list[dict]:
    """Read risks. Extra columns are kept. Missing required columns are an error."""
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"{path} has no header row")
        missing = [name for name in REQUIRED if name not in reader.fieldnames]
        if missing:
            raise ValueError(f"{path} is missing columns: {', '.join(missing)}")
        risks: list[dict] = []
        for line_number, row in enumerate(reader, start=2):
            row_id = (row.get("id") or "").strip()
            if row_id == "":
                continue
            likelihood = parse_scale(row.get("likelihood") or "", "likelihood", row_id)
            impact = parse_scale(row.get("impact") or "", "impact", row_id)
            score = None if likelihood is None or impact is None else likelihood * impact
            risks.append(
                {
                    "id": row_id,
                    "line": line_number,
                    "asset": (row.get("asset") or "").strip(),
                    "threat": (row.get("threat") or "").strip(),
                    "vulnerability": (row.get("vulnerability") or "").strip(),
                    "existing_control": (row.get("existing_control") or "").strip(),
                    "cia": (row.get("cia") or "").strip(),
                    "likelihood": likelihood,
                    "impact": impact,
                    "score": score,
                    "band": None if score is None else band(score),
                    "treatment": (row.get("treatment") or "").strip(),
                    "owner": (row.get("owner") or "").strip(),
                    "notes": (row.get("notes") or "").strip(),
                    "example": (row.get("example") or "").strip().lower() in {"yes", "true", "example"},
                }
            )
    return risks


def matrix_cells(risks: list[dict]) -> dict[tuple[int, int], list[str]]:
    """Map (likelihood, impact) to the risk ids that landed there."""
    cells: dict[tuple[int, int], list[str]] = {}
    for risk in risks:
        if risk["score"] is None:
            continue
        key = (risk["likelihood"], risk["impact"])
        cells.setdefault(key, []).append(risk["id"])
    return cells


def flagged(risks: list[dict]) -> list[dict]:
    """Risks at the high band or above. The cut-off is score 12."""
    return [risk for risk in risks if risk["score"] is not None and risk["score"] >= HIGH_SCORE]


def render_report(risks: list[dict], source: Path) -> str:
    """Plain-text report for the terminal."""
    lines = [
        "Week 1 risk scores",
        f"Source: {source}",
        "Score = likelihood x impact. High means 12 or above (high or critical).",
        "A blank likelihood or impact is not scored. It is not a zero.",
        "",
    ]
    if risks and all(risk["example"] for risk in risks):
        lines.append("EXAMPLE DATA. This file is a sample solution, not your submission.")
        lines.append("")
    cells = matrix_cells(risks)
    lines.append("|  | L1 | L2 | L3 | L4 | L5 |")
    for impact in range(5, 0, -1):
        row = [f"I{impact}"]
        for likelihood in range(1, 6):
            names = cells.get((likelihood, impact), [])
            row.append(", ".join(names) if names else ".")
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")
    lines.append("Scored risks")
    scored = [risk for risk in risks if risk["score"] is not None]
    if not scored:
        lines.append("  None yet. Fill likelihood and impact in the CSV, then run this again.")
    for risk in scored:
        treatment = risk["treatment"] or "no treatment yet"
        lines.append(
            f"  {risk['id']}: L{risk['likelihood']} x I{risk['impact']} = {risk['score']} {risk['band']} ({treatment})"
        )
    lines.append("")
    highs = flagged(risks)
    lines.append(f"Flagged (score >= {HIGH_SCORE})")
    if not highs:
        lines.append("  None.")
    for risk in highs:
        asset = risk["asset"] or "asset not named"
        lines.append(f"  {risk['id']} {risk['band']} {risk['score']}: {asset}")
    unscored = [risk for risk in risks if risk["score"] is None]
    if unscored:
        lines.append("")
        lines.append("Not scored yet")
        for risk in unscored:
            missing = []
            if risk["likelihood"] is None:
                missing.append("likelihood")
            if risk["impact"] is None:
                missing.append("impact")
            lines.append(f"  {risk['id']}: missing {' and '.join(missing)}")
    lines.append("")
    lines.append("The numbers are only as good as the reasons you write in the notes column.")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Score a Week 1 risk-register CSV")
    parser.add_argument("csv_path", type=Path, help="Risk register CSV to read")
    args = parser.parse_args()
    try:
        risks = load_risks(args.csv_path)
    except (OSError, ValueError) as exc:
        print(f"Could not score the register: {exc}", file=sys.stderr)
        sys.exit(1)
    print(render_report(risks, args.csv_path))


if __name__ == "__main__":
    main()
