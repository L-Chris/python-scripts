import os
import argparse
import shutil
import utils

parser = argparse.ArgumentParser()

parser.add_argument('--name', type = str)
parser.add_argument('--dir', type = str, default = '/home/www')
parser.add_argument('--build-dir', type = str, default = '')

args = parser.parse_args()
deploy_dir = args.dir + '/' + args.name
build_dir = args.build_dir + '/dist'

if not utils.existsDir(deploy_dir):
  os.mkdir(deploy_dir)

utils.removeDir(deploy_dir)
utils.moveDir(build_dir, deploy_dir)

print 'Deploy Success!'