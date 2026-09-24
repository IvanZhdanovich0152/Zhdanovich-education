from PIL import Image, ImageDraw
image = Image.open("test.tiff")
width = image.size[0]
height = image.size[1]
pix = image.load()

newImage = Image.new(mode=image.mode, size=(width * 4, height * 4))
newPix = newImage.load()

draw = ImageDraw.Draw(newImage)

if __name__ == '__main__':
    new_image_list = []
    for i in range(width):
        new_line_list = []
        for j in range(height):
            newpixel = pix[i, j]
            for _ in range(4):
                new_line_list.append(newpixel)
        for _ in range(4):
            new_image_list.append(new_line_list)

    for i in range(width * 4):
        for j in range(height * 4):
            pixel = new_image_list[i][j]
            draw.point((i, j), pixel)

newImage.save("ans.tiff", "TIFF")

del draw
image.close()
newImage.close()