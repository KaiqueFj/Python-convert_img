from PIL import Image, ImageFilter

img = Image.open('./pokedex/jordan.jpg') 
'''a lot of ways to edit the image, convert or change'''
'''filtered_img = img.filter(ImageFilter.SMOOTH) '''
''' filtered_img.show - show the image '''
''' crooked = filtered_img.rotate(90)- rotate the image '''
''' resize = filtered_img.resize((300,300))- resize the image '''
''' box = (100, 100, 400, 400) region = filtered_img.crop(box)- crop the image '''
''' keep the aspect of the img, with the pixels crop the image '''


img.thumbnail((400,400))
img.save('jordan_resized.jpg')

print (img.size)