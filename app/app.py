import flask
from flask import Blueprint, flash, g, redirect, render_template, request, url_for, session
from werkzeug.exceptions import abort
from app.auth import login_required
from app.db import get_db
from utils.utilities import imprint

bp = Blueprint('app', __name__)

COLORS = {'blue': 'rgba(26, 170, 170, 1)',
          'yellow': 'rgba(250, 225, 50, 1)',
          'green': 'rgba(25, 150, 75, 1)',
          'orange': 'rgba(225, 150, 50, 1)',
          'pink': 'rgba(250, 125, 125, 1)',
          'black': 'rgba(250, 250, 250, .75)'
}

@bp.route('/')
def index():
    return render_template('app/index.html')

class Node:
    def __init__(self, name, color):
        self.name = name

        try:
            self.color = COLORS[color]
        except KeyError as e:
            imprint(repr(e) + str(color) + ", defaulting to black", color='red')
            self.color = COLORS['black']

    def get_dict(self):
        return {"id": self.name, "color": self.color}


class Link:
    def __init__(self, source, target, value):
        self.source = source
        self.target = target
        self.value = value

    def get_dict(self):
        return {"source": self.source, "target": self.target, "value": self.value}



@bp.route("/_batch_data", methods=('GET', 'POST'))
def _batch_data():
    in_data = request.get_json()
    node_list = in_data['nodes']
    link_list = in_data['links']


    imprint(node_list, color='cyan')
    imprint(link_list, color='yellow')

    data = {
        'nodes': [],
        'links': [],
    }

    # nodes = []
    for node in node_list:
        new_node = Node(node['id'], node['color'])
        imprint(new_node.get_dict(), color='cyan')
        data['nodes'].append(new_node.get_dict())

    # links = []
    for link in link_list:
        new_link = Link(link['source'], link['target'], link['value'])
        imprint(new_link.get_dict(), color='orange')
        data['links'].append(new_link.get_dict())

    return flask.jsonify(result=data)