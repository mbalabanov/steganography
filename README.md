# Steganography in Python

## TL;DR
To decode a hidden message in an image, you can use Python with the Pillow library. The hidden message is encoded in the least significant bit of each color channel (red, green, and blue) of the image. The Python code for encoding and decoding the message can be found in a [Medium post](https://dayanand-shah.medium.com/the-art-of-hiding-secret-messages-in-images-with-python-steganography-5a6583065856).

### Running the Code
1. Install the Pillow library with `pip install Pillow`.
2. Run the Python code with `python decode.py`. By default, it reads the file `imgur.png` and decodes the hidden message outputting it to the console.
   
## Read All Details
You can find a much more detailed write-up about this topic here on my website [marincomics.com](https://marincomics.com/python-steganography.html)
