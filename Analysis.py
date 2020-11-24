import os
import pickle
import numpy
import argparse
import matplotlib.image as mpimg

FOLDPATH = 'D:/PythonProjects_DataNeo/MURA-v1.1\MURA-v1.1'


def GenerateFeatures(command=None):
    parser = argparse.ArgumentParser()
    ## Required parameters
    parser.add_argument("--input_path", default=None, type=str, required=True, help="The path of input fold.")
    if command is not None:
        args = parser.parse_args(command.split())
    else:
        args = parser.parse_args()
    args.input_path = args.input_path.replace('"', '')

    with open(os.path.join(args.input_path, 'train_image_paths.csv'), 'r') as file:
        trainImagePathData = file.readlines()

    trainData = []
    for filePath in trainImagePathData[0:10]:
        filePath = filePath.replace('MURA-v1.1/', '').replace('\n', '')
        currentData = mpimg.imread(os.path.join(args.input_path, filePath))
        print(filePath, numpy.shape(currentData))


if __name__ == '__main__':
    GenerateFeatures('--input_path="%s"' % FOLDPATH)
