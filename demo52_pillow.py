from urllib.request import urlopen
from PIL import Image

URL1 = "https://www.cwb.gov.tw/Data/satellite/LCC_IR1_CR_2750/LCC_IR1_CR_2750-2020-07-14-16-00.jpg"
fileToSave = urlopen(URL1)
print(type(fileToSave))
image1 = Image.open(fileToSave)
print(type(image1))
image1.save('images\\origin.jpg')
halfSize = (image1.size[0] // 2, image1.size[1] // 2)
halfImage = image1.resize(halfSize, Image.ANTIALIAS)
halfImage.save('images\\half.jpg')

r1 = halfImage.transpose(Image.ROTATE_90)
r1.save('images\\r90.jpg')
r2 = halfImage.transpose(Image.ROTATE_180)
r2.save('images\\r180.jpg')
r3 = halfImage.transpose(Image.ROTATE_270)
r3.save('images\\r270.jpg')
r4 = halfImage.rotate(45)
r4.save('images\\r45.jpg')
