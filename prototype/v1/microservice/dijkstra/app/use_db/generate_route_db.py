from app.use_db.tools import quarry


def add_intermediate(id_rt, longitude, latitude):
    quarry.call("insert into intermediate(id_rt, longitude, "
                "latitude, start_point, finish_point) "
                "values (%s, %s, %s, %s, %s)",
                [id_rt, longitude, latitude, "нет", "нет"],
                commit=True, fetchall=False)


def add_route(id_rt, geojson):
    geojson = f"{geojson}"
    quarry.call("insert into itirerary(id_rt, geojson) "
                "values (%s, %s)", [id_rt, geojson],
                commit=True, fetchall=False)