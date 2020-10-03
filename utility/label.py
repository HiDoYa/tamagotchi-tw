import pathlib
import os
import io
import faulthandler
from google.cloud import vision
from google.cloud import translate_v2 as translate

faulthandler.enable()

def translate_text(text):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language="en")
    return result["translatedText"]

# Adapted from gcloud example
def detect_text(path):
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.text_detection(image=image)
    if response.error.message:
        raise Exception('{}'.format(response.error.message))

    if len(response.text_annotations) == 0:
        raise Exception('Failed to read text')

    return response.text_annotations[0].description

def read_text(dirname):
    parent_path = str(pathlib.Path(__file__).parent.resolve())
    im_dir = os.path.join(parent_path, dirname)
    jp_dir = os.path.join(parent_path, dirname + "_meta_jp")
    en_dir = os.path.join(parent_path, dirname + "_meta_en")

    if not os.path.exists(jp_dir):
        print("Creating: {}".format(jp_dir))
        os.makedirs(jp_dir)

    if not os.path.exists(en_dir):
        print("Creating: {}".format(en_dir))
        os.makedirs(en_dir)

    ls = os.listdir(im_dir)

    for filename in ls:
        print("Current file: {}".format(filename))
        try:
            text = detect_text(os.path.join(im_dir, filename))
        except Exception as e:
            print(e)
            with open("errs.txt", "a+") as f:
                f.write(filename + '\n')
            continue

        text = text.replace("\n", "")
        text = text.replace("\r", "")
        text = text.replace(":", "")
        text = text.replace("。", "")
        print(text)

        text_filename = filename.replace("jpg", "txt")
        with open(os.path.join(jp_dir, text_filename), "w+", encoding='utf8') as f:
            f.write(text)

        with open(os.path.join(en_dir, text_filename), "w+") as f:
            f.write(translate_text(text))

read_text("desc_tama_images")
read_text("name_tama_images")
