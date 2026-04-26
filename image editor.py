from PIL import Image
import numpy as np
img = Image.open(r"C:\Users\Ara-PC\Downloads\earth.jpg")

img_array = np.array(img)
print(img_array.shape)


while True:
    print("1. Crop")
    print("2. Flip")
    print("3. Remove Red")
    choice = input("Enter a choice: ")

    if choice == "1":
        cropped = img_array[100:400, 200:500]

    elif choice == "2":
        flip_horizontal = img_array[:,::-1]
        flip_vertical = img_array[::-1,:]

    elif choice == "3":
        no_red = img_array.copy()
        no_red[:,:,0] = 0

        gray = np.mean(img_array,axis=2)
        bright = img_array + 50

        bright = np.clip(bright,0,255)
        result =Image.fromarray(bright.astype('uint8'))
        result.show()
        result.save()
        