# test script for docker logging

import time

print("✅ The script has started successfully!")

a = 10
b = 20
print(f"🔢 Sum of {a} and {b} is: {a + b}")

while True:
    print("⏳ Running... (Press CTRL+C to stop)")
    time.sleep(5)
