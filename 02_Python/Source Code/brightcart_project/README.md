# Brightcart: 10-day data analyst project

A ten-day project that takes messy business data through cleaning, analysis,
visualisation, statistical testing and reporting, using NumPy, pandas, Matplotlib
and Seaborn. The data is synthetic (see data/README.md for every column).

## Setup

You need Python 3.10 or newer. The project was built and checked with Python 3.13,
numpy 2.5.3, pandas 3.0.5, matplotlib 3.11.2 and seaborn 0.13.2.

    pip install numpy pandas matplotlib seaborn

## Run the whole project

From the project folder (the one that contains this README):

    python solutions/day10.py

This runs the Day 3 to Day 9 scripts in order, then writes:
- data/clean/: checkpoint files
- outputs/kpis.csv: the headline numbers
- outputs/charts/: the chart images
- outputs/executive_summary.md: the written summary

It prints lines starting with `CHECK`. Your numbers should match the expected output
on each day page.

## Day by day

Open `pages/day01.html` to `pages/day10.html` in a browser. Each page has the goal,
the functions to learn, the concepts, timed steps, a reference solution with expected
output, a checklist, and a 20-question quiz (pass mark 16 of 20).

| Day | Theme | Solution |
|---|---|---|
| 1 | Setup and first look | solutions/day01.py |
| 2 | NumPy for analysis | solutions/day02.py |
| 3 | Pandas data cleaning | solutions/day03.py |
| 4 | Joins, features and groupby | solutions/day04.py |
| 5 | Time series analysis | solutions/day05.py |
| 6 | Customer analytics | solutions/day06.py |
| 7 | Charts with Matplotlib | solutions/day07.py |
| 8 | Statistical charts with Seaborn | solutions/day08.py |
| 9 | Returns, tests and uncertainty | solutions/day09.py |
| 10 | Capstone and submission | solutions/day10.py |

## Folder layout

    README.md          this file
    data/              raw files (do not edit) and README.md, the data dictionary
    data/clean/        checkpoint files created by the pipeline
    solutions/         reference code for Days 1 to 10
    pages/             one HTML task page per day
    notes/             your notes (see notes/README.md)
    outputs/           kpis.csv, charts/ and executive_summary.md
    builder/           scripts that generated the day pages (for the course team)

## Submission guide

### What to submit

Submit one zip file, named `brightcart_<yourname>.zip`, containing a folder named
`brightcart_<yourname>/` with:

- README.md: how to run the project, in plain steps (you can copy and adapt this one)
- data/: the raw files, unchanged, plus data/README.md
- data/clean/: the checkpoint files your run produced
- solutions/: your code for Days 1 to 10
- notes/: your notes for each day, including day07_charts.md and day09_tests.md
- outputs/: kpis.csv, charts/ and executive_summary.md (rewritten in your own words)
- report/: optional PDF or Word copy of your executive summary

Also add a short cover note (in README.md or as a separate file) with: your name, the
hours you spent each day, the hardest day and why, and one finding you are most
confident about.

### How to check before you submit

1. Delete data/clean/ and outputs/, then run `python solutions/day10.py`. It must finish with no error.
2. Open outputs/kpis.csv. For every row, you should be able to name the calculation in one sentence.
3. Open outputs/executive_summary.md. Every number must match kpis.csv.
4. Open each chart in outputs/charts/. Titles, labels and units must be readable.
5. Unzip your package into an empty folder and run the README command again from there.
   If it works, your package is complete.

### Common mistakes

- Editing the raw files in data/. Always work from a copy or from the checkpoint files.
- Typing numbers into the summary by hand. They must come from the calculations.
- A README that says "run the code" without giving the command.
- Charts without units, or bars that do not start at zero.
- Absolute paths such as C:\Users\... in the code.
- No cover note, so the reviewer cannot tell what you did.
