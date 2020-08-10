import site
import os
import shutil

siteFolder = site.getsitepackages()[0]

os.system("pip3 install requests")
def copy_safe(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
copy_safe('wilibs', os.path.join(siteFolder, "wilibs"))