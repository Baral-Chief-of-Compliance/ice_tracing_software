from PIL import Image
import numpy as np


img = Image.open("./photos/test_3.jpg")

size = img.size
a = size[0] // 2
b = size[1] // 2
print(f"длинна: {size[0]}")
print(f"ширина: {size[1]}")
print(f"центр декартовой системы координат в точке: ({a},{b})")

img = np.asarray(img.convert('RGB'))

# print(img)

colors_in_photo = {}
for y in range(size[1]):
    for x in range(size[0]):
        if str(img[y][x]) in colors_in_photo.keys():
            colors_in_photo[f"{img[y][x]}"]["quantity"] = colors_in_photo[f"{img[y][x]}"]["quantity"] + 1
        else:
            colors_in_photo.setdefault(str(img[y][x]), {
                                                        "quantity": 1,
                                                        "R": img[y][x][0],
                                                        "G": img[y][x][1],
                                                        "B": img[y][x][2],
                                                        "summ": int(img[y][x][0]) + int(img[y][x][1]) + int(img[y][x][2])
                                                        })


list_of_RGB = list(colors_in_photo.items())

# for key in colors_in_photo:
#     print(f"цвет: {key} количество {colors_in_photo[key]['quantity']}")

list_of_RGB = sorted(list_of_RGB, key=lambda rgb: rgb[1]["quantity"])

with open('RGB.txt', 'w', encoding="utf-8") as file:
    for el in list_of_RGB:
        file.write(f"цвет: {el[0]} количество {el[1]['quantity']}\n")

