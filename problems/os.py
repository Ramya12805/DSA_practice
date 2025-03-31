# Write a Python program to get OS name, platform and release information.
import platform
import os
print("Name of the operating system: ",os.name)
print("\nName of the os system: ",platform.system())
print("\nVersion of the system: ",platform.release())