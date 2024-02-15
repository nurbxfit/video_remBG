import os 
import ffmpeg

def extract(video_path, output_path,target_fps = 24):
    os.makedirs(output_path, exist_ok=True)

    try: 
        probe = ffmpeg.probe(video_path)
        video_stream = find_video(probe['streams'])
        # duration = float(video_stream['duration'])
        input_fps = parse_frame_rate(video_stream['r_frame_rate'])
    except ffmpeg.Error as e:
        print("ffmpeg_error:",e.stderr)
        return
    
    input_options = {
        'r': input_fps  # Set input frame rate
    }

    output_options = {
        'f': 'image2',
        'y': '-y',
        'r': target_fps  # Set target frame rate
    }

    # Run ffmpeg
    ffmpeg.input(os.path.join(video_path),**input_options).output(
        f'{os.path.join(output_path)}/frame%04d.png', **output_options).run()
    

def find_video(streams):
    """Finds the video stream in the probe output."""
    for stream in streams:
        if stream['codec_type'] == 'video':
            return stream
    raise Exception("Failed to find video stream!")

def parse_frame_rate(frame_rate_str):
    numerator, denominator = map(int, frame_rate_str.split('/'))
    return numerator / denominator