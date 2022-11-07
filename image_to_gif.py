import argparse
import imageio
import os

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Kohonen Space Mapping - Image to GIF")

    # Add arguments
    parser.add_argument('-f', dest='folder', required=True)  # Path to folder
    parser.add_argument('-s', dest='step', required=True)  # Path to folder

    args = parser.parse_args()
    step = int(args.step)

    filenames = [f'{args.folder}/{x}.jpg' for x in range(0, len([x for x in os.listdir(args.folder) if 'jpg' in x]), step)]
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave(f'{args.folder}/__animation_{step}.gif', images)


if __name__ == '__main__':
    main()
