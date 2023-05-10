from app.use_db.tools import quarry


def show_routes(id_per):
    routes = quarry.call("select route.id_rt, route.name, ship.name_sh, ship.ice_class "
                         "from route inner join ship "
                         "on route.id_sh = ship.id_sh "
                         "where route.id_per = %s", [id_per], commit=False, fetchall=True)

    return routes
