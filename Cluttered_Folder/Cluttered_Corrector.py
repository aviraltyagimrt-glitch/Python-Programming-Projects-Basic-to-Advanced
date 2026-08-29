import os
files = os.listdir("Cluttered_Folder")
print(files)
k = 0
for i in files:
    if i.endswith(".png"):
        os.rename(f"Cluttered_Folder/{i}",f"Cluttered_Folder/Image-{k}.png")
        print(i)
        k = k + 1