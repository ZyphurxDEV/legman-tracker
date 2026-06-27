"""Generate icon.ico for the built exe from legman.png. Build-time only (Pillow
is not bundled into the app). Run automatically by build.bat."""
import os
from PIL import Image

if not os.path.exists("legman.png"):
    raise SystemExit("legman.png not found - cannot generate icon.ico")

img = Image.open("legman.png").convert("RGBA")
img.save("icon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
print("wrote icon.ico")
