import os
def util_open(name):
    if name=="settings":
        os.system("gnome-control-center")
    if name=="chrome":
        os.system("google-chrome")
    if name=="firefox":
        os.system("firefox")
    if name=="file manager" or name=="files":
        os.system("nautilus")
    if name=="terminal":
        os.system("gnome-terminal")
