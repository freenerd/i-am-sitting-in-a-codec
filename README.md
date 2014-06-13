# Installation

Install [FFmpeg](https://ffmpeg.org/)

Get Flask to run

http://flask.pocoo.org/docs/installation/

We recommend:

```
virtualenv venv
. venv/bin/activate

pip install -r requirements.txt
```

# Run

Easy local

```bash
// activate virtualenv
. venv/bin/activate

// run
python web.py
```

Or with gunicorn

```
// activate virtualenv
. venv/bin/activate

venv/bin/gunicorn -b 0.0.0.0:80 -w 4 web:app
```
