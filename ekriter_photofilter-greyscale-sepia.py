#Evey Kriter/CSCI0101/11.12.2019/Homework 8

import middimage

def grayscale(image):
    '''takes in an image and returns a grayscale (black and white) version'''
    new_image = middimage.new(image.width, image.height, 1)
    for i in range(image.height):
        for j in range(image.width):
            luminance = int((image[i][j][0]) + (image[i][j][1]) + (image[i][j][2])) / 3
            new_image[i , j] = luminance
    return new_image
            
#grayscale(middimage.open("beach.jpg")).show()

def grayscale_weighted(image, red_weight, green_weight, blue_weight):
    '''a better version of turning a picture into greyscale'''
    new_image = middimage.new(image.width, image.height, 1)
    for i in range(image.height):
        for j in range(image.width):
            r = image[i][j][0] * blue_weight
            g = image[i][j][1] * green_weight
            b = image[i][j][2] * red_weight
            new_image[i , j] = [int(r + g + b)]
    return new_image
            
grayscale_weighted(middimage.open("beach.jpg"), 0.3, 0.7, 0).show()


def sepia(image):
    '''takes in an image and returns a sepia version of the image'''
    new_image = middimage.new(image.width, image.height, image.channels)
    for i in range(image.height):
        for j in range(image.width):
            luminance = int((image[i][j][0] + image[i][j][1] + image[i][j][2]) / 3)
            if luminance < 63:
                r = min(255, int(luminance * 1.1))
                b = int(luminance * 0.9)
                new_image[i , j] = [r , luminance, b]
            elif 63 <= luminance < 193:
                r = min(255, int(luminance * 1.15))
                b = int(luminance * 0.85)
                new_image[i , j] = [r , luminance, b]
            elif 193 <= luminance <= 255:
                r = min(255, int(luminance * 1.08))
                b = int(luminance * 0.93)
                new_image[i , j] = [r , luminance, b]
    return new_image

#sepia(middimage.open("Ada_Lovelace.jpg")).show()
            
def mirror(image):
    '''
    takes an image and returns another image that has the left side reflected
    across the center line onto the right side
    '''
    new_image = image.copy()
    for i in range(image.height):
        for j in range(image.width//2):
            new_image[i , (image.width - j - 1)] = image[i , j]
    return new_image

#mirror(middimage.open("ada_lovelace.jpg")).show()

def four_up(image):
    '''takes in an image and returns an image that has four 1/4 sized versions of the original in it.'''
    new_image = image.copy()
    #make the image 1/4 the size it is
    for y in range(image.height//2):
        for x in range(image.width//2):
            new_image[y , x] = image[(y * 2) , (x * 2)]
    #quadruple that image
    for i in range(image.height//2):
        for j in range(image.width//2):
            new_image[i , (j + image.width//2)] = new_image[i , j]
            new_image[(i + image.height//2) , j] = new_image[i , j]
            new_image[(i + image.height//2) , (j + image.width//2)] = new_image[i , j]
    return new_image

#four_up(middimage.open("beach.jpg")).show()

            