from selenium import webdriver
import pyautogui
import time

# Replace with the path to your web driver executable
driver_path = '/chromedriver'

# Create a new instance of the web driver (e.g., Chrome)
options = webdriver.ChromeOptions()
options.binary_location = driver_path  # Path to the Chrome/Chromium binary

# Use the Chrome executable directly (no 'executable_path' argument)
driver = webdriver.Chrome(options=options)

# # Set the initial window position
initial_window_x = 22  # Replace with your desired X coordinate
initial_window_y = 47  # Replace with your desired Y coordinate
driver.set_window_position(initial_window_x, initial_window_y)


# Navigate to the page
sign_in_url = 'https://rmalek98.github.io/portfolio/'
driver.get(sign_in_url)

# Wait for a few seconds to give the page time to load
time.sleep(5)

# Get and print the current window position
# current_position = driver.get_window_position()
# print("Current window position:", current_position)


# print cursor position
# print(pyautogui.position())

# time.sleep(1.5)
# Simulate cursor movements and interactions using pyautogui
# Replace the coordinates and actions with your own interactions
pyautogui.moveTo(1165,319)  # Move the cursor to coordinates (X, Y)
pyautogui.click()           # Simulate a click

time.sleep(5)
# print cursor position
print(pyautogui.position())
pyautogui.moveTo(628, 638)  
pyautogui.click() 

time.sleep(5)
# print cursor position
print(pyautogui.position())

pyautogui.moveTo(176, 111)
pyautogui.click()
# Simulate typing text
text_to_type = "google.com"
pyautogui.typewrite(text_to_type, interval=0.1)
# Press Enter to submit the text
pyautogui.press('enter')
time.sleep(5)

# print cursor position
print(pyautogui.position()) 
time.sleep(5)
pyautogui.moveTo(381, 619)
pyautogui.click()
text_to_type = "rmalek98.github.io"
pyautogui.typewrite(text_to_type, interval=0.1)
# # Press Enter to submit the text
pyautogui.press('enter')

# Keep the browser window open for further interaction
input("Press Enter to close the browser...")

# Close the browser window
driver.quit()


'''
https://youtu.be/3PekU8OGBCA

https://youtu.be/3PekU8OGBCA

https://youtu.be/oXlwWbU8l2o
'''