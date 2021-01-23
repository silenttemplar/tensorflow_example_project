import matplotlib.pyplot as plt

img = plt.imread('./suzi.jpg', format='jpg')
#print(img.shape)

r_img = img[:, :, 0]
g_img = img[:, :, 1]
b_img = img[:, :, 2]
#print(r_img.shape)
#print(g_img.shape)
#print(b_img.shape)

imgs = [img, r_img, g_img, b_img]
cmaps = ['gray', 'Reds_r', 'Greens_r', 'Blues_r']
#print(img)

fig, axes = plt.subplots(2, 2, figsize=(15, 15))

for img, cmap, ax in zip(imgs, cmaps, axes.flatten()):
    ax.imshow(img, cmap='gray')
    #ax.imshow(img, cmap=cmap)

    ax.tick_params(labelleft=False, labelbottom=False)
    for spine_loc, spine in ax.spines.items():
        spine.set_visible(False)

fig.tight_layout()

plt.show()



