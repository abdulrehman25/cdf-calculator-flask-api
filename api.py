from os import abort
import flask
from flask import request, jsonify
from scipy.stats import norm
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    # define distribution parameters
    if 'mu' in request.args:
        mu = float(request.args['mu'])
        x = int(request.args['x'])
        sigma = float(request.args['sigma'])
        # create distribution
        dist = norm(mu, sigma)
        result = dist.cdf(x)
        print((result))
        return str(round(result,2))
    else:
        return "Nothing Found"

app.run()