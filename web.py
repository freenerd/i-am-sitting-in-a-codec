import os, time
from flask import Flask
from flask import render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # read the iteration file
    with open ("state/iteration.txt", "r") as myfile:
        data = myfile.read()
        return render_template('index.html', iteration=data)

@app.route('/process/<itr>')
def process(itr):
    # read current iteration
    with open ("state/iteration.txt", "r") as myfile:
        data = myfile.read().replace("\n", "")
        iteration = data
        next_iteration = str(int(iteration)+1)

    if iteration != itr:
        return redirect("/")

    # create new version
    p = "{0}/static/mp3/{1}.mp3"
    current_filepath =  p.format(os.getcwd(), iteration)
    output_filepath = p.format(os.getcwd(), next_iteration)
    cmd = "ffmpeg -y -vsync 2 -y -i {0} -b:a 64k {1}".format(current_filepath, output_filepath)
    os.popen(cmd)

    # update iteration count
    with open ("state/iteration.txt", "w") as myfile:
        myfile.write(next_iteration)

    # serve mp3 via redirect
    return redirect("/dl/{0}.mp3".format(next_iteration))

@app.route('/dl/<itr>.mp3')
def serve(itr):
    return app.send_static_file("mp3/{0}.mp3".format(itr))

if __name__ == '__main__':
    app.debug = True
    app.run()
