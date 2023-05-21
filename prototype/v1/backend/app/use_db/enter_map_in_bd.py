from app.use_db.tools import quarry
import json


def add_map_to_bd():
    with open("data/map.json", "r") as file:
        map_from_file = json.load(file)

    json_map = json.dumps(map_from_file)


    quarry.call("insert into map(map_json) values (%s)",
                [json_map], commit=True, fetchall=False)
