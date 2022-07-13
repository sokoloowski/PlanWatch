# PlanWatch

PlanWatch is a tiny Python script notifying You about updates in Your EAIIB timetable.

## Getting started

All You need is an URL to Your timetable. The URL has following structure:

    https://planzajec.eaiib.agh.edu.pl/view/timetable/<code>

and `<code>` is just a number of Your timetable.

## Requirements

All packages required by script are in [`requirements.txt`](requirements.txt). Install it using:

```bash
pip install -r requirements.txt
```

You may like to create a [virtual environment](https://docs.python.org/3/library/venv.html) first!

## Usage

To fetch data for timetable with `123` code (`https://planzajec.eaiib.agh.edu.pl/view/timetable/123`) You need to run the following command:

```bash
python main.py 123
```

And... That's all!

**Tip:** You may like to run this script with crontab :wink:
