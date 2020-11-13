from PIL import Image
from os import listdir

for img_name in listdir("../Data/images/normal"):
    img_to_resize = Image.open('../Data/images/normal/' + img_name)
    img_out = img_to_resize.resize((60, 60), Image.LANCZOS)
    img_out.save('../Data/images/resized/' + img_name)
