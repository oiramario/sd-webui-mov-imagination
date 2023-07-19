import os

from PIL import Image
from tqdm import tqdm


def extract(keyframes_path, grid_path, frame_width, frame_height, grid_rows, grid_cols, splits_path):
    keyframes = sorted(os.listdir(keyframes_path))
    keyframe_count = len(keyframes)
    grid_images = sorted(os.listdir(grid_path))
    frame_index = 0
    with tqdm(total=keyframe_count, unit='split') as pbar:
        for grid_file in grid_images:
            grid_image = Image.open(os.path.join(grid_path, grid_file))
            for row in range(grid_rows):
                for col in range(grid_cols):
                    # Calculate the coordinates of the current frame in the grid image
                    x = col * frame_width
                    y = row * frame_height

                    # Extract the frame from the grid image
                    frame = grid_image.crop((x, y, x + frame_width, y + frame_height))

                    # Save the extracted frame
                    name = keyframes[frame_index]
                    output_filename = os.path.join(splits_path, name)
                    frame.save(output_filename)

                    frame_index += 1
                    pbar.update(1)
                    if frame_index == keyframe_count:
                        return True
