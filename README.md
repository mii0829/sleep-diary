# Sleep diary
log your night sleep and check with a report. In the report, you can see average, shortest sleep, longest sleep, the number of nights below your goal.

## Requirements
- Python 3.10 or newer
- [uv](https://docs.astral.sh/uv/) (build tool and package manager)

## Getting started 
```bash
git clone git@github.com:mii0829/sleep-diary.git
cd sleep-diary
uv sync --locked
```

## Usage
```bash
uv run sleep-diary --help
uv run sleep-diary add 7.5
uv run sleep-diary report --goal 8
```

### Example output 
```text
                                      
 Usage: sleep-diary [OPTIONS] COMMAND  
 [ARGS]...                             
                                       
 Log your sleep and see how you are    
 doing.                                
                                       
╭─ Options ───────────────────────────╮
│ --install…        <bool>  Install   │
│                           completi… │
│                           for the   │
│                           current   │
│                           shell.    │
│ --show-co…        <bool>  Show      │
│                           completi… │
│                           for the   │
│                           current   │
│                           shell, to │
│                           copy it   │
│                           or        │
│                           customize │
│                           the       │
│                           installa… │
│ --help            <bool>  Show this │
│                           message   │
│                           and exit. │
╰─────────────────────────────────────╯
╭─ Commands ──────────────────────────╮
│ add     Record last night's sleep,  │
│         e.g. `sleep-diary add 7.5`. │
│ report  Show average, shortest,     │
│         longest and nights below    │
│         the goal.                   │
╰─────────────────────────────────────╯
```
```text
Saved 7.5 h to sleep.csv
```
```text
Nights:      3
Average:     7.0 h (goal 8.0 h)
Shortest:    6.0 h
Longest:     7.5 h
Below goal:  3 night(s)
```
Records are stored in 'sleep.csv' in the current folder 

## Development
| Task | Command
| --- | --- |
| Run the tests | `uv run pytest -v` |
| Add a run time dependency | ` uv add <package>` |
| Add a development dependency | ` uv add <package>` |
| remove a dependency | ` uv remove --dev <package>` |
| show the dependency tree | `uv tree` |
| Bump the version | `uv version --bump minor` |
| Build the wheel and sdist | ` uv build ` |

## Static Code analysis 
I used Ruff 
this is used as linter and formatter. 
installed with the dev dependencies (`uv sync `). the rules are configured in '[tool.ruff]` in `pyproject.toml`. 

```
uv run ruff check .
uv run ruff check --fix .
uv run ruff format .
```

## Project struvture
``` tree
.
├── .gitignore
├── .pytest_cache
│   ├── .gitignore
│   ├── CACHEDIR.TAG
│   ├── README.md
│   └── v
│       └── cache
│           └── nodeids
├── .python-version
├── pyproject.toml
├── README.md
├── src
│   └── sleep_diary
│       ├── __init__.py
│       ├── cli.py
│       ├── stats.py
│       └── storage.py
├── tests
│   ├── test_stats.py
│   └── test_storage.py
└── uv.lock
```