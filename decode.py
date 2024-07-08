from PIL import Image

print('Starting to decode the message from the stego image...')

stego_img = Image.open('imgur.png')
stego_img = stego_img.convert('RGB')

width, height = stego_img.size

#Iterate over each pixel in the stego image and extract the least significant bit of each color channel (red, green, and blue) to decode the binary message:
binary_message = ''
i = 0
while True:
    x, y = i % width, i // width
    r, g, b = stego_img.getpixel((x, y))
    binary_message += str(r & 1) + str(g & 1) + str(b & 1)
    i += 1
    if len(binary_message) % 8 == 0 and chr(int(binary_message[-8:], 2)) == '\x00':
        break

#Convert the binary message to its original text format:
decoded_message = ''
for i in range(0, len(binary_message), 8):
    decoded_message += chr(int(binary_message[i:i+8], 2))

print(decoded_message)