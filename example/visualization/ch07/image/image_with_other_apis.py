import matplotlib.pyplot as plt

img = plt.imread('./suzi.jpg', format='jpg')
#print(img.shape)

r_img = img[:, :, 0]
g_img = img[:, :, 1]
b_img = img[:, :, 2]
#print(r_img)
#print(g_img.shape)
#print(b_img.shape)

fig, axes = plt.subplots(2, 2, figsize=(15, 15))

axes[0, 0].imshow(img)
axes[0, 0].tick_params(labelleft=False, labelbottom=False, left=False, bottom=False)

axes[0, 1].hist(r_img.flatten(), bins=20, color='r')
axes[1, 0].hist(g_img.flatten(), bins=20, color='g')
axes[1, 1].hist(b_img.flatten(), bins=20, color='b')

fig.tight_layout()
plt.show()