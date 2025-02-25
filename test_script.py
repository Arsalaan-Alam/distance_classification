import cv2
import os
import sys

image_files = ["shashi.jpg", "faculty.jpg"]

def check_image_loading(image_path):
    if not os.path.exists(image_path):
        print(f"❌ ERROR: File '{image_path}' not found!")
        return False
    
    img = cv2.imread(image_path)
    if img is None:
        print(f"❌ ERROR: '{image_path}' could not be loaded (corrupted or invalid format).")
        return False
    
    print(f"✅ SUCCESS: '{image_path}' loaded successfully.")
    return True

all_tests_passed = True
for img_file in image_files:
    if not check_image_loading(img_file):
        all_tests_passed = False

if not all_tests_passed:
    sys.exit(1)  