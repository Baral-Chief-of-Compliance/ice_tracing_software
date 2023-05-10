from app.use_db.tools import quarry


def add_ship(name_sh, ice_class):
    quarry.call("insert into ship(name_sh, ice_class) values "
                "(%s, %s)", [name_sh, ice_class],
                commit=True, fetchall=False)


def find_ship(name_sh):
    id_sh = quarry.call("select id_sh from ship where "
                        "name_sh = %s", [name_sh], commit=False,
                        fetchall=False)

    return id_sh


def create_route(name, id_per, id_sh):
    quarry.call("insert into route(name, id_per, id_sh) values "
                "(%s, %s, %s)", [name, id_per, id_sh],
                commit=True, fetchall=False)


def find_route(name_route):
    id_rt = quarry.call("select id_rt from route where "
                        "name = %s", [name_route], commit=False,
                        fetchall=False)

    return id_rt


def create_start_end_point(
        id_rt,
        start_longitude,
        start_latitude,
        end_longitude,
        end_latitude,
        date_start
):
    quarry.call("insert into intermediate(id_rt, longitude, "
                "latitude, date_enter, start_point, finish_point) "
                "values (%s, %s, %s, %s, %s, %s)",
                [id_rt, start_longitude, start_latitude,
                 date_start, "да", "нет"], commit=True,
                fetchall=False)

    quarry.call("insert into intermediate(id_rt, longitude, "
                "latitude, start_point, finish_point) "
                "values (%s, %s, %s, %s, %s)",
                [id_rt, end_longitude, end_latitude, "нет", "да"],
                commit=True, fetchall=False)


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


def show_all_intermediate(id_rt):
    intermediates = quarry.call("select latitude, longitude "
                                "from intermediate where "
                                "id_rt = %s and start_point = 'нет' "
                                "and finish_point = 'нет' order by "
                                "id_inter", commit=False, fetchall=True)

    return intermediates


def show_all_itirerary(id_rt):
    itirerary = quarry.call("select geojson from itirerary where "
                            "id_rt = %s order by id_itir", commit=False,
                            fetchall=True)

    return itirerary
