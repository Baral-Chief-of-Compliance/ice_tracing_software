#https://nbviewer.org/github/yvan/nbsblogs/blob/master/playing_with_perlin_noise/generate_islands.ipynb
import noise
import numpy as np
from PIL import Image
import math
from test import Config
import json


def rgb_norm(world):
    world_min = np.min(world)
    world_max = np.max(world)
    norm = lambda x: (x-world_min/(world_max - world_min))*255
    return np.vectorize(norm)


def prep_world(world):
    norm = rgb_norm(world)
    world = norm(world)
    return world


def create_ice(map_):
    width = len(map_)
    length = len(map_[0])
    shape = (width, length)
    scale = 100
    octaves = 6
    persistence = 0.4
    lacunarity = 2.0
    seed = np.random.randint(0,100)
    # seed = 126

    world = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            world[i][j] = noise.pnoise2(i/scale,
                                        j/scale,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=shape[1],
                                        repeaty=shape[0],
                                        base=seed)

    center_x, center_y = shape[1] - 150, shape[0] // 100
    circle_grad = np.zeros_like(world)

    for y in range(world.shape[0]):
        for x in range(world.shape[1]):
            distx = abs(x - center_x)
            disty = abs(y - center_y)
            dist = math.sqrt(distx*distx + disty*disty)
            circle_grad[y][x] = dist

    # get it between -1 and 1
    max_grad = np.max(circle_grad)
    circle_grad = circle_grad / max_grad
    circle_grad -= 0.5
    circle_grad *= 2.0
    circle_grad = -circle_grad

    world_noise = np.zeros_like(world)

    for i in range(shape[0]):
        for j in range(shape[1]):
            if circle_grad[i][j]>0:
                world_noise[i][j] = (world[i][j] * circle_grad[i][j])

    threshold = 50

    def add_color2(world):
        color_world = np.zeros(world.shape+(3,))
        for i in range(shape[0]):
            for j in range(shape[1]):
                if world[i][j] < threshold + 100:
                    color_world[i][j] = Config.blue
                elif world[i][j] < threshold + 105:
                    color_world[i][j] = Config.fast_ice
                elif world[i][j] < threshold + 110:
                    color_world[i][j] = Config.ice_field
                elif world[i][j] < threshold + 120:
                    color_world[i][j] = Config.nilas_ice
                elif world[i][j] < threshold + 130:
                    color_world[i][j] = Config.young_ice
                elif world[i][j] < threshold + 140:
                    color_world[i][j] = Config.first_year_ice
                # elif world[i][j] < threshold + 137:
                #     color_world[i][j] = mountain
                else:
                    color_world[i][j] = Config.old_ice

        return color_world

    island_world_grad = add_color2(prep_world(world_noise)).astype(np.uint8)

    for y in range(width):
        for x in range(length):
            if island_world_grad[y, x][0] == Config.old_ice[0] \
                    and island_world_grad[y, x][1] == Config.old_ice[1] \
                    and island_world_grad[y, x][2] == Config.old_ice[2]:
                map_[y][x]["type_of_ice"] = "old_ice"

            elif island_world_grad[y, x][0] == Config.young_ice[0] \
                    and island_world_grad[y, x][1] == Config.young_ice[1] \
                    and island_world_grad[y, x][2] == Config.young_ice[2]:
                map_[y][x]["type_of_ice"] = "young_ice"

            elif island_world_grad[y, x][0] == Config.first_year_ice[0] \
                    and island_world_grad[y, x][1] == Config.first_year_ice[1] \
                    and island_world_grad[y, x][2] == Config.first_year_ice[2]:
                map_[y][x]["type_of_ice"] = "first_year_ice"

            elif island_world_grad[y, x][0] == Config.nilas_ice[0] \
                    and island_world_grad[y, x][1] == Config.nilas_ice[1] \
                    and island_world_grad[y, x][2] == Config.nilas_ice[2]:
                map_[y][x]["type_of_ice"] = "nilas_ice"

            elif island_world_grad[y, x][0] == Config.fast_ice[0] \
                    and island_world_grad[y, x][1] == Config.fast_ice[1] \
                    and island_world_grad[y, x][2] == Config.fast_ice[2]:
                map_[y][x]["type_of_ice"] = "fast_ice"

            elif island_world_grad[y, x][0] == Config.ice_field[0] \
                    and island_world_grad[y, x][1] == Config.ice_field[1] \
                    and island_world_grad[y, x][2] == Config.ice_field[2]:
                map_[y][x]["type_of_ice"] = "ice_field"

    # island_world_grad = add_color2(prep_world(world_noise)).astype(np.uint8)
    # Image.fromarray(island_world_grad,'RGB').show()

    return map_

#
# with open("../tools/map.json", "r") as file:
#     map_ = json.load(file)
#
#
# map_ = create_ice(map_)