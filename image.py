from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')

img.thumbnail((400, 400))
img.save('thumbnail.jpg')

# # unsplash.com to download free images
# img = Image.open('./pokedex/poke1.jpg')
# # filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.convert('L')
# crooked = filtered_img.rotate(90)
# resize = filtered_img.resize((180, 180))  # accepts a tuple
#
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
#
# filtered_img.save("grey.png", "png")
# crooked.save("rotated.png", "png")
# resize.save("small.png", "png")
# region.save("cropped.png", "png")
# region.show()


