
import pyautogui
import time
from PIL import ImageGrab, ImageOps
import numpy as np

# Coordinates for the game over region
restart_button = (680, 390)
dino_position = (150, 425)


def press_space():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')


def is_obstacle_near():
    # Define the box region where obstacles will appear
    box = (dino_position[0] + 150, dino_position[1], dino_position[0] + 200, dino_position[1] + 50)
    print(box)
    image = ImageGrab.grab(box)
    # print(image)
    gray_image = ImageOps.grayscale(image)
    # print(np.array(gray_image))
    a = np.array(gray_image.getcolors())
    value = a.sum()
    print(value)
    pixel_sum = np.array(gray_image).sum()
    # print(pixel_sum)
    print("\n")
    return value != 2755
    # return pixel_sum < 637500          # Threshold for obstacle detection


def main():
    time.sleep(2)  # Time to switch to the game screen
    press_space()  # Start the game

    while True:
        # is_obstacle_near()
        if is_obstacle_near():
            press_space()


if __name__ == "__main__":
    main()















# import pyautogui as py
# import time
#
# time.sleep(3)
#
# # Mouse functions
# print(py.size())
#
# # prints the current position of an mouse
# print(py.position())
#
# # moves the mouse
# py.moveTo(500, 500, 3)
#
# # moves the mouse relative to its current position
# py.moveRel(100,100,2)

# key board functions
#
# py.write("Hi I am Yuvaraj")
# py.press('backspace')
# py.press("enter")
# py.press("space")

# print(py.displayMousePosition())