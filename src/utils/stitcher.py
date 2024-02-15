import os
import ffmpeg

def stitch_frames (input_path, output_path, frame_rate = 60, output_format = 'mp4'):
    
    if not os.path.isdir(input_path):
        raise ValueError("Input folder path does not exist.")
    
    # Ensure the input directory exists
    os.makedirs(input_path, exist_ok=True)

     # Define output video file name
    output_file_name = 'output_video.' + output_format

    # Define the input and output options for ffmpeg
    input_options = {
        'f': 'concat',
        'safe': 0,
        'r': frame_rate,

    }


    output_options = {
        # 'c:v': 'libx264',
        # 'pix_fmt': 'yuv420p',
        'y': '-y'
    }

     # List input files explicitly
    input_files = sorted([f for f in os.listdir(input_path) if f.startswith('frame') and f.endswith('.png')])

     # Create a file list for ffmpeg concat demuxer
    file_list = '\n'.join(["file '" + os.path.abspath(os.path.join(input_path, file)) + "'" for file in input_files])

    # Create a text file listing the input files
    with open('input_list.txt', 'w') as f:
        f.write(file_list)

    
    input_pattern = os.path.join('input_list.txt')

    # Run ffmpeg to create the video
    ffmpeg.input(input_pattern,**input_options).output(
        os.path.join(output_path,output_file_name), **output_options).run()
