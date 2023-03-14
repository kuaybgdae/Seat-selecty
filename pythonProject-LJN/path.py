import os
import sys

for root, dirs, files in os.walk(sys.prefix):
    if 'pywintypes38.dll' in files:
        print(os.path.join(root, 'pywintypes38.dll'))
