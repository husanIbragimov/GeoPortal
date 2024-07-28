import folium
from flask import render_template, Blueprint

from gis import create_app

app = Blueprint('app', __name__)


@app.route("/")
def index():
    # template_name = 'gis/index.html'
    m = folium.Map(location=[41.3775, 64.5853], zoom_start=6)
    return m.get_root().render()
