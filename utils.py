import os
import shutil

def existsFile(path):
  return os.path.exists(path) and os.path.isfile(path)

def existsDir(path):
  return os.path.exists(path) and not os.path.isfile(path)

def removeDir(path):
  for i in os.listdir(path):
    path_file = os.path.join(path, i)
    if os.path.isfile(path_file):
      os.remove(path_file)
    else:
      removeDir(path_file)

def moveDir(src, dst):
  for i in os.listdir(src):
    srcPath = os.path.join(src, i)
    dstPath = os.path.join(dst, i)
    shutil.move(srcPath, dstPath)