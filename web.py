import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    # read the iteration file
    with open ("state/iteration.txt", "r") as myfile:
        data = myfile.read()
        return render_template('index.html', iteration=data)

@app.route('/download')
def download():
    # read current iteration
    with open ("state/iteration.txt", "r") as myfile:
        data = myfile.read().replace("\n", "")
        iteration = data
        next_iteration = str(int(iteration)+1)

    # create new version
    p = "{0}/static/mp3/{1}.mp3"
    current_filepath =  p.format(os.getcwd(), iteration)
    output_filepath = p.format(os.getcwd(), next_iteration)
    cmd = "ffmpeg -y -vsync 2 -y -i {0} -b:a 64k {1}".format(current_filepath, output_filepath)
    os.popen(cmd)

    # update iteration count
    with open ("state/iteration.txt", "w") as myfile:
        myfile.write(next_iteration)

    # server mp3
    return app.send_static_file("mp3/{0}.mp3".format(next_iteration))

if __name__ == '__main__':
    app.debug = True
    app.run()




for i in range(0,50):
    f = os.getcwd()+"/mp3/{0}.mp3"
    create_iteration(i)
