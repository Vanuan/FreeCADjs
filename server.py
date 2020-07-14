from flask_graphql import GraphQLView
from graphene import String, ObjectType, Schema, Field, JSONString, List
import graphene
from flask import Flask, send_from_directory

from schema import Settings
from resolvers import get_settings

class Query(ObjectType):
    settings = Field(Settings)

    def resolve_settings(root, info):
        return get_settings()

schema = Schema(query=Query)

app = Flask(__name__, static_folder='./freecad-js/build/static/', static_url_path='/static')
#app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory("./freecad-js/build/", "index.html")

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

# Optional, for adding batch query support (used in Apollo-Client)
app.add_url_rule('/graphql/batch', view_func=GraphQLView.as_view('graphql-batch', schema=schema, batch=True))