from app.use_db.tools import quarry
import json


def get_map():
    map_form_bd = quarry.call("select map_json from map where map_id = 1", commit=False, fetchall=False)

    return json.loads(map_form_bd[0])
