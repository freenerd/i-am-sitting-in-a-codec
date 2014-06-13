# What?

Read the [index.html](https://github.com/freenerd/i-am-sitting-in-a-codec/blob/master/templates/index.html) or check the deployed version at http://bit.ly/sitting-in-a-codec for the description.

Made by Karl and Johan at Music Hack Day Barcelona 2014.

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
