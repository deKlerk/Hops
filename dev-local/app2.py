from flask import Flask
import ghhops_server as hs
from ghhops_server.params import HopsCurve, HopsNumber
import rhino3dm as rh

from owlready2 import *

# register hops app as middleware
app2 = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app2)

# flask app can be used for other stuff drectly
@app2.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"

#-- OWLREADY2 - Pizza demo --#
@hops.component(
    "/owldemo",
    name="OwlDemo",
    description="Demo using Owlready2",
    inputs=[
        hs.HopsString("Url", "U", "Url to ontology")
    ],
    outputs=[
        hs.HopsString("Classes", "Cls", "Classes in the ontology")#,
       # hs.HopsString("Properties", "Prop", "Properties in the ontology"),
        #hs.HopsString("Individuals", "Ind", "Individuals in the ontology")
    ]
)
def owldemo(owlurl: str):
    try:
        onto = get_ontology(owlurl).load()
        owl_class = onto.classes()
        #prop = list(onto.properties())s
        #ind = list(onto.individuals())

        print(owl_class)

        return owl_class

    except Exception as e:
        return e



if __name__ == '__main__':
    # set debug=True
    app2.run(debug=True)