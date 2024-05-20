from flask import Flask,render_template,Response

app=Flask(__name__)


# def generate_frames():
#    while True:
#            
#        ## read the camera frame
#        success,frame=camera.read()
#        if not success:
#            break
#        else:
#            ret,buffer=cv2.imencode('.jpg',frame)
#            frame=buffer.tobytes()
#
#        yield(b'--frame\r\n'
#                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


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