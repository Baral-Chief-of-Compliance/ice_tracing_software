from app.use_db.tools import quarry


def add_ship(name_sh, ice_class):
    id_sh_from_db = quarry.call('select max(id_sh) from ship', commit=False, fetchall=False)

    if id_sh_from_db[0] == None:
        id_sh = 1
    else:
        id_sh = int(id_sh_from_db[0]) + 1

    quarry.call("insert into ship(id_sh, name_sh, ice_class) values "
                "(%s, %s, %s)", [id_sh, name_sh, ice_class],
                commit=True, fetchall=False)

    return id_sh


def create_route(name, id_per, id_sh):

    id_rt_from_db = quarry.call('select max(id_rt) from route', commit=False, fetchall=False)

    if id_rt_from_db[0] == None:
        id_rt = 1
    else:
        id_rt = int(id_rt_from_db[0]) + 1

    quarry.call("insert into route(id_rt, name, id_per, id_sh) values "
                "(%s, %s, %s, %s)", [id_rt, name, id_per, id_sh],
                commit=True, fetchall=False)

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
