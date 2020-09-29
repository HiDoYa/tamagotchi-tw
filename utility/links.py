import os
import pathlib
import requests

link = "https://toy.bandai.co.jp/assets/tamagotchi/images/chara/detail/chara_"
ext = ".jpg"
path = "tama_images/"

if not os.path.exists(path):
    os.makedirs(path)

for i in range(1, 294 + 1):
    url = link + "{:0>3d}".format(i) + ext
    link_name = os.path.basename(url)
    res = requests.get(url)
    if res.status_code != 200:
        continue

    with open(path + link_name, "wb+") as f:
        f.write(res.content)

