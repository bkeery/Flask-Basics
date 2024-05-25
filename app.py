from flask import Flask,render_template,Response

app=Flask(__name__)


# ChartPlotter:5000/index.html
#   is the root page of the system.
#   is also the router
#   each Remote Cameras (eventually named in .env)
#   each camera will have a DNS name such as BowCam, MastCam, etc
#   each camera is an endpoint
#   in addition, the chartplotter will call endpoint to take-a-picture
#
#   the chartplotter will show the last image taken in a Gallery
#       Bowcam:5000/static/LastImage.jpg
#       Mastcam:5000/static/LastImage.jpg
#       etc.
#   the Gallery will allow update or download


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/picture')
def picture():
    return render_template('picture.html')

@app.route('/video')
def video():
    return render_template('video.html')

# @app.route('/video')
# def video():
#     return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')


# only to be used in development!
#
if __name__=="__main__":
    app.run()