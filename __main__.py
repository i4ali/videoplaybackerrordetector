import subprocess
import os
from argparse import ArgumentParser


def videoPlaybackErrorDetector(path):
    for file in os.listdir(path):
        filename, file_extension = os.path.splitext(file)
        if file_extension == '.mp4':
            print("processing file {0}...".format(file))
            subprocess.call('ffmpeg -v error -i {0} -map 0:1 -f null - 2>>{1}.log'.format(file, filename), shell=True)
            if os.path.getsize(filename+'.log') > 0:
                print("possible playback error in {0}, check {0}.log for details ".format(filename))
            else:
                # clean up unnecessary files
                os.remove('{0}.log'.format(filename))


if __name__ == '__main__':
    parser = ArgumentParser(description="Video Playback Error Detector Utility")
    parser.add_argument("videopath", metavar='N', help="Path to cobanvideos folder", type=str, action="store")
    args = parser.parse_args()
    videoPlaybackErrorDetector(args.videopath)
