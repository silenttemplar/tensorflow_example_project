import matplotlib.pyplot as plt

# png format image
img = plt.imread('./Lenna.png')
img_cropped = img[:300, :300, :]

# jpg format image
#img = plt.imread('./suzi.jpg', format='jpg')
print(img.shape)


fig, axes = plt.subplots(1, 2, figsize=(14, 7))
axes[0].imshow(img)
axes[1].imshow(img_cropped)

plt.show()