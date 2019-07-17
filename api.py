import flask
from flask import request
import pandas
import sys

app = flask.Flask(__name__)
app.secret_key = "hey"

COLORS = {'blue': 'rgba(26, 170, 170, 1)',
          'yellow': 'rgba(250, 225, 50, 1)',
          'green': 'rgba(25, 150, 75, 1)',
          'orange': 'rgba(225, 150, 50, 1)',
          'pink': 'rgba(250, 125, 125, 1)',
          'black': 'rgba(250, 250, 250, .75)'
}

NODES = []
LINKS = []




@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html')

class Node:
    count = -1
    nodes = {}

    def __init__(self, name, color):
        self.name = name
        # self.group = group

        Node.count += 1
        Node.nodes[self.name] = Node.count
        self.node = Node.nodes[self.name]

        try:
            self.color = COLORS[color]
        except KeyError as e:
            print(repr(e) + str(color) + ", defaulting to black", file=sys.stderr)
            self.color = COLORS['black']

        # if group == 'income':
        #     self.color = blue
        # else: 
        #     self.color = pink

    def get_dict(self):
        return {"node": self.node, "name": self.name, "color": self.color}

    def reset():
        Node.count = -1
        Node.nodes = {}

class Link:
    def __init__(self, source, target, value):
        # self.source = source
        # self.target = target
        self.value = value

        try:
            self.source = Node.nodes[source]
            self.target = Node.nodes[target]
        except KeyError as e:
            print("\n" + repr(e) + str(source) + "" + str(target) + '\n\n', file=sys.stderr)
            self.source = 0
            self.target = 1

    def get_dict(self):
        return {"source": self.source, "target": self.target, "value": self.value}
        


@app.route("/_create_node")
def _create_node():
    name = flask.request.args.get("name", type=str)
    color = flask.request.args.get("color", type=str)
    print(name, file=sys.stderr)
    print(color, file=sys.stderr)


        
    new_node = Node(name, color)
    # print("NEEEW NODE: " + str(new_node.get_dict()))

    NODES.append(new_node)
    # print("NODES" + str(NODES) + " " + str(len(NODES)), file=sys.stderr)

    return flask.jsonify(result=True)

# TODO: create_link
@app.route("/_create_link")
def _create_link():
    source = flask.request.args.get("source", type=str)
    target = flask.request.args.get("target", type=str)
    value = flask.request.args.get("value", type=float)

    if value == None:
        value = 0

    new_link = Link(source, target, value)

    LINKS.append(new_link)

    return flask.jsonify(result=True)


@app.route("/_get_nodes")
def get_nodes():

    data = {
        "nodes": [],
        "links": []
        }

    for node in NODES:
        data["nodes"].append(node.get_dict())
        print("NODE DICT: " + str(node.get_dict()), file=sys.stderr)

    for link in LINKS:
        # if link.get_dict()['source'] != None:
        data["links"].append(link.get_dict())
        print("LINK DICT: " + str(link.get_dict()), file=sys.stderr)

    return flask.jsonify(result=data)

@app.route("/_prepare")
def _prepare():
    Node.reset()
    NODES.clear()
    LINKS.clear()

    return flask.jsonify(result=True)


if __name__ == "__main__":
    print("Opening for global access on port {}".format(5000))
    app.run(port=5000, host="0.0.0.0")

    _prepare()