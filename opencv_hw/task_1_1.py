import cv2

def execute(img):
    n = 3
    for i in range(n):
        for j in range(n):
            cv2.imwrite("output/cropped_image_" + str(i) + str(j) + ".png",
                        img[(img.shape[0] // n * i):(img.shape[0] // n * (i + 1)),
                        (img.shape[1] // n * j):(img.shape[1] // n * (j + 1))])
