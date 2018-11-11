import requests
from io import BytesIO
from PIL import Image

FINAL_WIDTH = 100

# From light to dark
ASCII_CHARS = [" ", ".", "'",",", "\"", "*", "^", ":", ";", "+","?", "%", "$","&","@", "#"]

def ascii_from_url(url):
   return ascii_from_image(Image.open(BytesIO(requests.get(url).content))) 

def ascii_from_image(image):
   scaling_factor = FINAL_WIDTH / image.width

   scaled = image.resize((int(scaling_factor * image.width),
       int(scaling_factor * image.height * 1/2)), # Compensate for difference in char width/height
       Image.BICUBIC)

   greyscaled = scaled.convert('L')

   lines = []
  
   for y in range(scaled.height):
       thisline = []

       for x in range(scaled.width):
           
           normalizedValue = greyscaled.getpixel((x, y)) / 256

           index = normalizedValue * len(ASCII_CHARS)

           thisline.append(ASCII_CHARS[int(index)])

       lines.append("".join(thisline))

   return "\n".join(lines)


