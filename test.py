from flask_angular_injection import AngularInjection


import flask

app = flask.Flask(__name__)

ang = AngularInjection(app)

@app.route('/',defaults={'id':None})
@app.route('/<id>/')
def index(id):
    return flask.render_template('index.html',testing_data=id)


if __name__=='__main__':
    app.run()