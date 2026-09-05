# Assignment 11 — Advanced Data Visualization

A separate repository for the Code the Dream Assignment 11 exercises.
Use Python 3.13, create `.venv`, and install `requirements.txt`.

## Run Tasks 1–4

```sh
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python assignment11/employee_results.py
python assignment11/cumulative.py
python assignment11/wind.py
```

The two Pandas scripts display plots and save PNG/CSV outputs alongside the
scripts. Open `assignment11/wind.html` in a browser for the interactive chart.
Wind ranges use their midpoint; an open-ended value such as `6+` uses its lower
bound. The resulting `strength` column is numeric, with original labels retained
for hover text. `reflection.txt` contains the supplied reflection.

`db/lesson.db` is the copy from the homework repository, including the Assignment
10 order. Current outputs cover 250 orders and 20 employees with total revenue
$68,593.16. The cumulative plot follows order ID, not chronological order dates.

## Task 6 — capstone dashboard

The quotes capstone remains in the user-selected repository:
https://github.com/shanny2022/python_homework

Deployment settings:

- Repository: `shanny2022/python_homework`
- Branch: `assignment11-capstone`
- Main file: `assignment10/capstone_quotes/app.py`
- Python: `3.13`

The dashboard reads the capstone SQLite database and implements three interactive
charts with author, tag, and word-count filters. Its Streamlit URL belongs in
`assignment11/service_urls.txt` after deployment.

## Validation

Regenerated and visually inspected both PNGs; checked revenue agreement between
employee and order queries, cumulative ordering, and all 128 wind observations.
The wind HTML was generated with embedded Plotly JavaScript. Browser interaction
checks for wind and public Streamlit deployment remain pending because browser
control was unavailable in this session. The capstone's Streamlit AppTest cases
passed for filters, metrics, chart presence, and an empty selection.
