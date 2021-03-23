from flask import Flask
import ghhops_server as hs
from ghhops_server.params import HopsCurve, HopsNumber
import rhino3dm as rh


# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)

# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"

#-- Point At component --#
@hops.component(
    "/pointat",
    name="PointAt",
    description="Get a point along a curve",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate.")
    ],
    outputs=[
        hs.HopsPoint("P", "P", "Point on Curve at parameter t")
    ]
)
def pointat(curve: rh.Curve, t: float=0):
    pt = curve.PointAt(t)
    return pt


if __name__ == '__main__':
    # set debug=True
    app.run(debug=True)