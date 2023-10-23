import multiprocessing.dummy as mp
import cv2

Data = []
resize = 150

contador = 0

imagePath = "peepoG.png"

def apply_filter(image, m):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (resize, resize)) / 255

image = cv2.imread(imagePath)

# 10 threads
p=mp.Pool(10)
p.map(lambda m: apply_filter(image.copy(), m),range(0,22000))
p.close()
p.join()
