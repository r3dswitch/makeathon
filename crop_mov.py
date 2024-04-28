from moviepy.editor import VideoFileClip
import os

def crop_videos_in_directory(input_folder, output_folder, left, top, right, bottom):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    # Loop through each file in the folder
    for file in files:
        # Check if the file is a MOV video
        if file.lower().endswith('.mov'):
            # Open the video file
            video_path = os.path.join(input_folder, file)
            clip = VideoFileClip(video_path)
            # Crop the video
            cropped_clip = clip.crop(x1=left, y1=top, x2=right, y2=bottom)
            # Save the cropped video to the output folder
            output_path = os.path.join(output_folder, file)
            cropped_clip.write_videofile(output_path, codec='libx264')
            # Close the clip to release resources
            cropped_clip.close()

# Example usage
input_folder = "./test"
output_folder = "."
# Define crop dimensions (left, top, right, bottom)
crop_dimensions = (1400, 250, 3000, 2500)  # Example dimensions, adjust as needed

# Crop videos in the input folder and save them to the output folder
crop_videos_in_directory(input_folder, output_folder, *crop_dimensions)
