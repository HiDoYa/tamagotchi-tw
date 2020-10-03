import pathlib
import os
import argparse

parent_path = str(pathlib.Path(__file__).parent.resolve())

nm_dir = os.path.join(parent_path, "name_tama_images")
en_dir = os.path.join(parent_path, "name_tama_images_meta_en")
jp_dir = os.path.join(parent_path, "name_tama_images_meta_jp")

if not os.path.exists(en_dir):
    print("Path {} do not exist. Try again.".format(en_dir))
    exit()

if not os.path.exists(jp_dir):
    print("Path {} do not exist. Try again.".format(jp_dir))
    exit()

ls = os.listdir(nm_dir)

def get_correct():
    with open("correct.txt", "w") as f:
        for filename in ls:
            jp_name = ""
            en_name = ""
            out = ""
            jp_path = os.path.join(jp_dir, filename).replace("jpg", "txt")
            en_path = os.path.join(en_dir, filename).replace("jpg", "txt")

            if os.path.exists(jp_path) and os.path.exists(en_path):
                with open(jp_path, "r") as jp_f:
                    jp_name = jp_f.read()

                with open(en_path, "r") as en_f:
                    en_name = en_f.read()
                
            out = ",".join([filename, jp_name, en_name])
            f.write(out + '\n')

def put_correct():
    contents = ""
    with open("correct.txt", "r") as f:
        contents = f.read()

    contentnl = contents.split('\n')
    for line in contentnl:
        if line == "":
            continue
        indv = line.split(',')
        print(indv)
        filename = indv[0]
        jp_name = indv[1]
        en_name = indv[2]

        jp_path = os.path.join(jp_dir, filename).replace("jpg", "txt")
        en_path = os.path.join(en_dir, filename).replace("jpg", "txt")

        with open(jp_path, "w") as jp_f:
            jp_f.write(jp_name)

        with open(en_path, "w") as en_f:
            en_f.write(en_name)

parser = argparse.ArgumentParser(description='Create file to correct google OCR')
parser.add_argument('mode', type=str, help='Indicate whether correct.txt file is being created (create) or loaded (load).')
args = parser.parse_args()

mode = args.mode
if mode == "load":
    put_correct()
elif mode == "create":
    get_correct()
