from app.use_db.tools import quarry


def show_routes(id_per):
    routes = quarry.call("select route.id_rt, route.name, ship.name_sh, ship.ice_class, status_rt, intermediate.date_enter "
                         "from route inner join ship "
                         "on route.id_sh = ship.id_sh "
                         "inner join intermediate "
                         "on route.id_rt = intermediate.id_rt and intermediate.start_point = 'да'"
                         "where route.id_per = %s", [id_per], commit=False, fetchall=True)

    return routes


def show_inf_about_route(id_per, id_rt):
    route_inf = quarry.call("select route.id_rt, route.name, ship.name_sh, ship.ice_class "
                            "from route inner join ship "
                            "on route.id_sh = ship.id_sh "
                            "where route.id_per = %s and route.id_rt = %s", [id_per, id_rt],
                            commit=False, fetchall=False)

    inf_about_start = quarry.call("select intermediate.longitude, intermediate.latitude, intermediate.date_enter "
                                  "from intermediate "
                                  "where intermediate.id_rt = %s and intermediate.start_point = 'да'", [id_rt],
                                  commit=False, fetchall=False)

    inf_about_end = quarry.call("select intermediate.longitude, intermediate.latitude "
                                "from intermediate "
                                "where intermediate.id_rt = %s and intermediate.finish_point = 'да'", [id_rt],
                                commit=False, fetchall=False)

    intermediates = quarry.call("select intermediate.longitude, intermediate.latitude, intermediate.date_enter "
                              "from intermediate "
                              "where intermediate.id_rt = %s and "
                              "intermediate.finish_point = 'нет' and "
                              "intermediate.start_point = 'нет' and intermediate.date_enter is not null group by intermediate.id_inter", [id_rt],
                               commit=False, fetchall=True)

    final_point = quarry.call("select intermediate.longitude, intermediate.latitude "
                                "from intermediate "
                                "where intermediate.id_rt = %s and "
                                "intermediate.finish_point = 'нет' and "
                                "intermediate.start_point = 'нет' and intermediate.date_enter is null group by intermediate.id_inter",
                                [id_rt],
                                commit=False, fetchall=False)

    itirerarys = quarry.call("select itirerary.geojson "
                             "from itirerary "
                             "where itirerary.id_rt = %s group by itirerary.id_itir", [id_rt],
                             commit=False, fetchall=True)

    return route_inf, inf_about_start, inf_about_end, intermediates, itirerarys, final_point


def set_data_on_point(id_per, id_rt, date):

    final_point_id = quarry.call("select intermediate.id_inter "
                                "from intermediate "
                                "where intermediate.id_rt = %s and "
                                "intermediate.finish_point = 'нет' and "
                                "intermediate.start_point = 'нет' and intermediate.date_enter is null group by intermediate.id_inter",
                                [id_rt],
                                commit=False, fetchall=False)

    quarry.call("update intermediate set date_enter = %s where id_inter = %s",
                [date, final_point_id], commit=True, fetchall=False)


def delete_route(id_rt):
    id_sh = quarry.call("select route.id_rt from route "
                        "where route.id_rt = %s", [id_rt],
                        commit=False, fetchall=False)

    quarry.call("delete from ship where id_sh = %s", [id_sh[0]],
                commit=True, fetchall=False)

    quarry.call("delete from route where id_rt = %s", [id_rt],
                commit=True, fetchall=False)


def get_status(id_rt):
    status = quarry.call("select status_rt from route "
                         "where route.id_rt = %s", [id_rt],
                         commit=False, fetchall=False)

    status = status[0]

    return status


def update_status(id_rt, date):
    quarry.call("update intermediate set date_enter = %s where finish_point = 'да' and id_rt = %s",
                [date, id_rt], commit=True, fetchall=False)

    quarry.call("update route set status_rt = 'завершён' where id_rt = %s", [id_rt], commit=True, fetchall=False)
    
