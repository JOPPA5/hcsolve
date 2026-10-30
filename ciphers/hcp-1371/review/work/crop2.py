from PIL import Image, ImageEnhance
im=Image.open('msg.png')
print(im.size)
im.save('msg_view.png')
