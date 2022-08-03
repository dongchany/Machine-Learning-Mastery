from PIL import Image
from numpy import asarray
from numpy import expand_dims

img = Image.open('penguin_parade.jpg')
img = img.convert(mode='L')
data = asarray(img)
print(data.shape)
data_first = expand_dims(data, axis=0)
print(data_first.shape)
data_last = expand_dims(data, axis=2)
print(data_last.shape)
