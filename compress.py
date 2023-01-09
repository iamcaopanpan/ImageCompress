from PIL import Image
from os import path
from shutil import copyfile


def compressImage(image1_path, size2):
    image1_basename, type_name = path.basename(image1_path).split('.')[0], path.basename(image1_path).split('.')[1]
    image2_path = path.dirname(image1_path) + '/' + image1_basename + '_compressed.' + type_name
    copyfile(image1_path, image2_path)

    im = Image.open(image2_path)
    size1 = path.getsize(image2_path)//1024

    w, h = im.size[0], im.size[1]

    while size1 > size2:
        w, h = int(w*0.95), int(h*0.95)
        im = im.resize((w, h))
        im.save(image2_path)

        size1 = path.getsize(image2_path)//1024


    # i = 1
    # while True:
    #     if not path.exists(image2_path):
    #         im.save(image2_path)
    #         break
    #     else:
    #         image2_path = path.dirname(image1_path) + '/' + image1_basename + '_compressed(' + str(i) + ').' + type_name
    #     i = i+1
    im.close()

#
# if __name__ == '__main__':
#     compressImage('.././icon/1.jpg')