from flask import Flask
import ghhops_server as hs
from ghhops_server.params import HopsCurve, HopsInteger, HopsNumber
import rhino3dm as rh

from owlready2 import *

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


#-- Profile Levels component --#
@hops.component(
    "/plevels",
    name="ProfileLevels",
    description="Creates a series of levels from a profile",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to replicate"),
        hs.HopsNumber("D", "D", "Distance between levels"),
        hs.HopsInteger("N", "N", "Number of levels")
    ],
    outputs=[
        hs.HopsCurve("Curves", "Cs", "Series of profile curves")
    ]
)
def plevels(curve: rh.Curve, d: float=1.0, n: int=1):
    crvs = [curve]
    temp = 0.0

    for i in range(n+1):
        crv = curve
        temp += d
        vec = rh.Vector3d(0,0,temp)
        trans = rh.Transform.Translation(vec)
        crv.Transform(trans)
        crvs.append(crv)

    return crvs

#-- Test Lists component --#
@hops.component(
    "/outlists",
    name="OutLists",
    nickname="OutLists",
    description="Trying list output",
    inputs=[hs.HopsInteger("N", "N", "Number of items in list")],
    outputs=[hs.HopsInteger("out", "out", "list of numbers")]
)
def outlist(n: int=1):
    lst = [i for i in range(n)]
    return lst


#-- OWLREADY2 Demo --#
@hops.component(
    "/owldemo",
    name="OwlDemo",
    description="Demo using Owlready2",
    inputs=[hs.HopsString("Url", "U", "Url to ontology")],
    outputs=[
        hs.HopsString("Classes", "Cls", "Classes in the ontology"),
        hs.HopsString("Properties", "Prop", "Properties in the ontology"),
        hs.HopsString("Individuals", "Ind", "Individuals in the ontology")
    ]
)
def owlDemo(owlurl: str):
    
    onto = get_ontology(owlurl).load()
    owl_class = list(onto.classes())
    owl_prop = list(onto.properties())
    owl_ind = list(onto.individuals())

    return (str(owl_class), str(owl_prop), str(owl_ind))


if __name__ == '__main__':
    # set debug=True
    app.run(debug=True)