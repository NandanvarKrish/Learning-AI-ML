#!/usr/bin/env python3
"""Build the ten day pages for the Brightcart project.

For each day this script:
  1. runs the reference solution and checks that the expected CHECK lines appear,
  2. renders pages/dayNN.html in the blue design system (timed steps, reference output, quiz).
Run from anywhere:  python builder/build_pages.py
"""
import html
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DESIGN_DIR = Path("/tmp/claude-0/-home-claude/950937c1-a215-5613-9bce-681a08392d2f/scratchpad/analytics")
sys.path.insert(0, str(DESIGN_DIR))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import tutorial_lib as T  # shared page CSS, quiz engine and section helpers
from content_a import DAYS as DAYS_A
from content_b import DAYS as DAYS_B
from content_c import DAYS as DAYS_C

DAYS = sorted(DAYS_A + DAYS_B + DAYS_C, key=lambda d: d["n"])

# CHECK keys each day's solution must print. A missing key means the script changed.
EXPECT = {
    1: ["np_mean", "grid_shape", "orders_shape", "missing_unit_price", "duplicate_rows"],
    2: ["price_mean_ignoring_nan", "usable_rows", "total_revenue", "delivery_outliers"],
    3: ["orders_raw", "after_remove_duplicates", "orders_clean", "clean_nulls_total"],
    4: ["rows_after_join", "total_net_revenue", "overall_margin_pct", "pivot_shape"],
    5: ["months", "best_month", "quarters"],
    6: ["active_customers", "champions_count", "rfm_score_range", "cohorts"],
    7: ["line_points", "top_bar_height", "dashboard_axes"],
    8: ["heatmap_shape", "qty_revenue_corr", "facet_count"],
    9: ["overall_return_rate", "permutation_p_value", "delivery_ci_low", "corr_delivery_return"],
    10: ["stages_ok", "kpi_rows", "summary_lines"],
}

# The shared quiz engine was written for an SQL course; adjust its wording for this project.
SCRIPT = (T.SCRIPT
          .replace("Run the examples again in a fresh database.", "Re-run the solution and check the outputs.")
          .replace("You can build and change a database with confidence.",
                   "You can clean, analyse and report on data with confidence."))


def run_solution(day):
    """Run the reference solution, fail loudly, and return its CHECK lines."""
    script = ROOT / "solutions" / day["solution"]
    proc = subprocess.run([sys.executable, str(script)], cwd=ROOT, capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(f"Day {day['n']} failed:\n{proc.stderr}")
    checks = [line for line in proc.stdout.splitlines() if line.startswith("CHECK ")]
    keys = {line.split()[1] for line in checks}
    missing = [k for k in EXPECT[day["n"]] if k not in keys]
    if missing:
        raise SystemExit(f"Day {day['n']} is missing CHECK lines: {missing}")
    return checks


def tool_cards(tools):
    return '<div class="mini-grid">' + "".join(T.mini(n, d, e) for n, d, e in tools) + "</div>"


def concept_cards(concepts):
    cards = "".join(
        f'<div class="mini-card"><div class="mc-name">{html.escape(name)}</div>'
        f'<div class="mc-desc">{desc}</div></div>'
        for name, desc in concepts)
    return f'<div class="mini-grid">{cards}</div>'


def step_phases(steps):
    return "".join(
        T.task_phase(i, html.escape(title), f"{minutes} min", f"<p>{text}</p>", open_=(i == 1))
        for i, (title, minutes, text) in enumerate(steps, 1))


def solution_section(day, checks):
    code = (ROOT / "solutions" / day["solution"]).read_text()
    body = ("<p>Try the task yourself first. Then compare your results with the reference below. "
            "Your numbers must match the expected output.</p>"
            + T.code_block(code, f"solutions/{day['solution']}")
            + "<p><strong>Expected output</strong>, from running the script:</p>"
            + T.code_block("\n".join(checks), "Expected output"))
    return T.section("💡", "Reference solution and expected output",
                     "Check your work against this.", body)


def submission_section(sub):
    folder = T.code_block("\n".join(sub["folder"]), "Folder layout")
    steps = "<ol>" + "".join(f"<li>{html.escape(s)}</li>" for s in sub["steps"]) + "</ol>"
    where = f"<p>{html.escape(sub['where'])}</p>"
    before = "<h4>Before you submit, check that:</h4>" + T.checklist([html.escape(b) for b in sub["before"]])
    mistakes = ("<h4>Common mistakes</h4><ul>"
                + "".join(f"<li>{html.escape(m)}</li>" for m in sub["mistakes"]) + "</ul>")
    return T.section("📦", "How to submit",
                     "What to hand in, how to package it, and how to check it first.",
                     "<h4>What to submit</h4>" + folder + "<h4>How to package it</h4>" + steps
                     + where + before + mistakes)


def day_pills(current):
    return "".join(
        f'<a class="day-pill{" active" if n == current else ""}" href="day{n:02d}.html">Day {n}</a>'
        for n in range(1, 11))


def render(day, checks):
    n = day["n"]
    minutes = sum(m for _, m, _ in day["steps"])
    sections = [
        T.section("🎯", "Goal and deliverable", html.escape(day["theme"]),
                  f"<p>{day['goal']}</p><p><strong>Deliverable:</strong> {day['deliverable']}</p>"),
        T.section("🧰", "Tools and functions", "Learn each one, then use it in the steps below.",
                  tool_cards(day["tools"])),
        T.section("🧠", "Concepts", "The ideas behind today's work.", concept_cards(day["concepts"])),
        T.section("🛠️", "Timed steps", f"About {minutes} minutes of work. Open each step, do it, then move on.",
                  step_phases(day["steps"])),
        solution_section(day, checks),
        T.section("☑️", "Checklist", "Everything here must be true before you move on.",
                  T.checklist(day["checklist"])),
    ]
    if "submission" in day:
        sections.append(submission_section(day["submission"]))
    sections.append(T.section("✅", "Quiz", "20 questions. Pass mark is 16 of 20 (80%).", T.quiz_block()))

    questions_json = T.quiz_questions(day["quiz"])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Day {n}: {html.escape(day['title'])} · Brightcart</title>
<style>{T.page_css()}</style>
</head>
<body>
<nav class="topnav">
  <span class="logo">Brightcart</span><span class="sep">|</span>
  <span class="day-label">Day {n} of 10</span>
  <span class="spacer"></span>
  <span class="progress-label">Quiz: <span id="answered-live">0</span>/20 · score <span id="score-live">0</span></span>
</nav>
<div class="hero">
  <div class="eyebrow">Brightcart data analyst project · Day {n} of 10</div>
  <h1>Day {n}: <span>{html.escape(day['title'])}</span></h1>
  <p>{day['goal']}</p>
</div>
<div class="grad-banner"><p>{html.escape(day['hours'])} · {html.escape(day['theme'])}</p></div>
<div class="container">
{"".join(sections)}
</div>
<div class="day-footer">
  <div class="series">Brightcart 10-day data analyst project</div>
  <div class="days-row">{day_pills(n)}</div>
</div>
<script>
{SCRIPT.replace('__QUESTIONS__', questions_json)}
</script>
</body>
</html>
"""


def main():
    out = ROOT / "pages"
    out.mkdir(exist_ok=True)
    for day in DAYS:  # in order: Day 3 writes the clean files that Days 4 to 10 read
        checks = run_solution(day)
        (out / f"day{day['n']:02d}.html").write_text(render(day, checks), encoding="utf-8")
        minutes = sum(m for _, m, _ in day["steps"])
        print(f"day{day['n']:02d}.html  {len(checks)} CHECK lines  {minutes} planned minutes")


if __name__ == "__main__":
    main()
