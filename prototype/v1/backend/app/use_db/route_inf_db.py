from app.use_db.tools import quarry


def show_routes(id_per):
    routes = quarry.call("select route.id_rt, route.name, ship.name_sh, ship.ice_class "
                         "from route inner join ship "
                         "on route.id_sh = ship.id_sh "
                         "where route.id_per = %s", [id_per], commit=False, fetchall=True)

    return routes


def show_inf_about_route(id_per, id_rt):
    route_inf = quarry.call("select route.id_rt, route.name, ship.name_sh, ship.ice_class "
                            "from route inner join ship "
                            "on route.id_sh = ship.id_sh "
                            "where route.id_per = %s and route.id_rt = %s", [id_per, id_rt],
                            commit=False, fetchall=False)

    inf_about_start = quarry.call("select intermediate.longitude, intermediate.latitude "
                                  "from intermediate "
                                  "where intermediate.id_rt = %s and intermediate.start_point = 'да'", [id_rt],
                                  commit=False, fetchall=False)

    inf_about_end = quarry.call("select intermediate.longitude, intermediate.latitude "
                                "from intermediate "
                                "where intermediate.id_rt = %s and intermediate.finish_point = 'да'", [id_rt],
                                commit=False, fetchall=False)

    intermediates = quarry.call("select intermediate.longitude, intermediate.latitude "
                              "from intermediate "
                              "where intermediate.id_rt = %s and "
                              "intermediate.finish_point = 'нет' and "
                              "intermediate.start_point = 'нет' group by intermediate.id_inter", [id_rt],
                               commit=False, fetchall=True)

    itirerarys = quarry.call("select itirerary.geojson "
                             "from itirerary "
                             "where itirerary.id_rt = %s group by itirerary.id_itir", [id_rt],
                             commit=False, fetchall=True)

    return route_inf, inf_about_start, inf_about_end, intermediates, itirerarys
