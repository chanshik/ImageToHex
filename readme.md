## Convert image to hex for Furious True-D Rev. 2.0 Firmware

Furious True-D's LCD resolution is 128x64 and only shows black and white pixel.

So, recommended image size is 128x64 pixels.

Converted image consist black and white pixels only.

If pixel has a RGB(255, 255, 255), 

it changed to black.
Others are changed to white.


## Run

```
$ pip3 install Pillow
$ python3 image_to_hex.py RDK_Logo_128x64.png 0x7140
```
