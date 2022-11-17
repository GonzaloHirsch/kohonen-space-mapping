# Kohonen Space Mapping

Example of Kohonen working as a Self-Organizing Map.

The implementation of Kohonen is a modified version of [MiniSom](https://github.com/JustGlowing/minisom). The difference is an exposed method to apply the training in steps to be able to hook up to that and visualize the process.

## Setting Up

Create a virtual environment and install all dependencies:
```bash
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```

## Execution

### Kohonen Method

To run the method, the command is:
```bash
python main.py -n KOHONEN_SIZE -it ITERATIONS -nd SPACE_POINTS
```
- `-n` --> Size of the network (n x n)
- `-it` --> Number of iterations to use
- `-nd` --> Total points to attempt to adjust to (should be perfect square, ie, 25, 36, 49, etc) within the range `[-1, 1]`

Example call:
```bash
python main.py -n 5 -it 3000 -nd 25
```

### Image to GIF

To run the method, the command is:
```bash
python image_to_gif.py -f FOLDER_PATH -s STEPS_IN_GIF
```
- `-f` --> Path to folder with images
- `-s` --> Frames to skip in every iteration, it's the step

Example call:
```bash
python image_to_gif.py -f results/5-3000-25 -s 10
```

### Image to Video

To run the method, the command is:
```bash
python image_to_video.py -f FOLDER_PATH -s STEPS_IN_GIF -fps VIDEO_FPS
```
- `-f` --> Path to folder with images
- `-s` --> Frames to skip in every iteration, it's the step
- `-fps` --> FPS for the video

Example call:
```bash
python image_to_video.py -f results/5-3000-25 -s 1 -fps 60
```
