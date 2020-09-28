link = "https://toy.bandai.co.jp/assets/tamagotchi/images/chara/detail/chara_"
ext = ".jpg"

for i in range(1, 294 + 1):
    print(link + "{:0>3d}".format(i) + ext)
