from utils import extractor
from utils import remover
from utils import stitcher

SOURCE_FILE = 'video-input.mp4'  # Assuming video-input.mp4 is located in the current directory
FRAME_RATE = 60
FINAL_OUTPUT_VIDEO = 'finals/'
BACKGROUND_REMOVED_FOLDER = 'background_removed'
EXTRACTED_FRAMES_FOLDER = 'output_frames'

# Extract frames from the video
extractor.extract(SOURCE_FILE,EXTRACTED_FRAMES_FOLDER, FRAME_RATE)

# Remove backgrounds from the extracted frames


remover.remove_backgrounds(EXTRACTED_FRAMES_FOLDER, BACKGROUND_REMOVED_FOLDER)
stitcher.stitch_frames(BACKGROUND_REMOVED_FOLDER,FINAL_OUTPUT_VIDEO,FRAME_RATE)