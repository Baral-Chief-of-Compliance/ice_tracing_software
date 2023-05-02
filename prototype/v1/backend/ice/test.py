import noise
import numpy as np
from PIL import Image


class Config:
    blue = [0, 199, 254]
    first_year_ice = [0, 200, 161]
    young_ice = [247, 8, 249]
    old_ice = [144, 0, 1]
    nilas_ice = [9, 104, 245]
    fast_ice = [255, 250, 250]
    ice_field = [185, 177, 177]


def show_image(world):
    img = np.floor((world + .5) * 255).astype(np.uint8)
    Image.fromarray(img, mode='L').save("test.jpg")


def add_color(world):

    color_world = np.zeros(world.shape + (3,))
    for y in range(world.shape[0]):
        for x in range(world.shape[1]):
            if world[y][x] < -0.05:
                color_world[y][x] = Config.blue

            elif world[y][x] < -0.04:
                color_world[y][x] = Config.ice_field

            elif world[y][x] < -0.03:
                color_world[y][x] = Config.fast_ice

            elif world[y][x] < -0.01:
                color_world[y][x] = Config.nilas_ice

            elif world[y][x] < 0:
                color_world[y][x] = Config.young_ice

            elif world[y][x] < .20:
                color_world[y][x] = Config.first_year_ice

            elif world[y][x] < 1.0:
                color_world[y][x] = Config.old_ice

    return color_world


def create_ice(map_):
    width = len(map_)
    length = len(map_[0])
    shape = (length, width)
    scale = .1
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0
    seed = np.random.randint(0, 100)

    x_idx = np.linspace(0, 1, shape[0])
    y_idx = np.linspace(0, 1, shape[1])
    world_x, world_y = np.meshgrid(x_idx, y_idx)

    world = np.vectorize(noise.pnoise2)(world_x / scale,
                                        world_y / scale,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=shape[0],
                                        repeaty=shape[1],
                                        base=seed)

    color_world = add_color(world)

    for y in range(width):
        for x in range(length):
            if color_world[y, x][0] == Config.old_ice[0] \
                    and color_world[y, x][1] == Config.old_ice[1] \
                    and color_world[y, x][2] == Config.old_ice[2]:
                map_[y][x]["type_of_ice"] = "old_ice"

            elif color_world[y, x][0] == Config.young_ice[0] \
                    and color_world[y, x][1] == Config.young_ice[1] \
                    and color_world[y, x][2] == Config.young_ice[2]:
                map_[y][x]["type_of_ice"] = "young_ice"

            elif color_world[y, x][0] == Config.first_year_ice[0] \
                    and color_world[y, x][1] == Config.first_year_ice[1] \
                    and color_world[y, x][2] == Config.first_year_ice[2]:
                map_[y][x]["type_of_ice"] = "first_year_ice"

            elif color_world[y, x][0] == Config.nilas_ice[0] \
                    and color_world[y, x][1] == Config.nilas_ice[1] \
                    and color_world[y, x][2] == Config.nilas_ice[2]:
                map_[y][x]["type_of_ice"] = "nilas_ice"

            elif color_world[y, x][0] == Config.fast_ice[0] \
                    and color_world[y, x][1] == Config.fast_ice[1] \
                    and color_world[y, x][2] == Config.fast_ice[2]:
                map_[y][x]["type_of_ice"] = "fast_ice"

            elif color_world[y, x][0] == Config.ice_field[0] \
                    and color_world[y, x][1] == Config.ice_field[1] \
                    and color_world[y, x][2] == Config.ice_field[2]:
                map_[y][x]["type_of_ice"] = "ice_field"

    return map_
