import argparse
import cv2
import os

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Kohonen Space Mapping - Image to GIF")

    # Add arguments
    parser.add_argument('-f', dest='folder', required=True)  # Path to folder
    parser.add_argument('-s', dest='step', required=True)  # Path to folder
    parser.add_argument('-fps', dest='fps', required=True)  # Path to folder

    args = parser.parse_args()

    step = int(args.step)
    fps = int(args.fps)
    image_folder = args.folder
    video_name = f'__video_{step}_{fps}.mp4'

    images = [f'{args.folder}/{x}.jpg' for x in range(0, len([x for x in os.listdir(args.folder) if 'jpg' in x]), step)]
    frame = cv2.imread(images[0])
    height, width, layers = frame.shape

    video = cv2.VideoWriter(f'{image_folder}/{video_name}', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width,height))

    for image in images:
        video.write(cv2.imread(image))

    cv2.destroyAllWindows()
    video.release()


if __name__ == '__main__':
    main()
