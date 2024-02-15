from utils.extractor import extract
from utils.cleaner import clear_folder
from utils.remover import remove_backgrounds
from utils.stitcher import stitch_frames
import time

def process_video(**kwargs):
    if not 'FRAME_RATE' in kwargs:
        raise f'Please provide target FRAME_RATE'
    if not 'SOURCE_FILE' in kwargs:
        raise f"Please provide valid SOURCE_FILE path"
    if not 'EXTRACTED_FRAMES_FOLDER' in kwargs:
        raise f"Please provide valid EXTRACTED_FRAMES_FOLDER path"
    if not 'BACKGROUND_REMOVED_FOLDER' in kwargs:
        raise f"Please provide valid BACKGROUND_REMOVED_FOLDER path"
    if not 'FINAL_OUTPUT_VIDEO' in kwargs:
        raise f"Please provide valid FINAL_OUTPUT_VIDEO path"
    

    SOURCE_FILE = kwargs['SOURCE_FILE']
    FRAME_RATE = kwargs['FRAME_RATE']
    EXTRACTED_FRAMES_FOLDER = kwargs['EXTRACTED_FRAMES_FOLDER']
    BACKGROUND_REMOVED_FOLDER = kwargs['BACKGROUND_REMOVED_FOLDER']
    FINAL_OUTPUT_VIDEO = kwargs['FINAL_OUTPUT_VIDEO']

    start_time = time.time()
    extract(SOURCE_FILE, EXTRACTED_FRAMES_FOLDER, FRAME_RATE)
    remove_backgrounds(EXTRACTED_FRAMES_FOLDER, BACKGROUND_REMOVED_FOLDER)
    print(f'Final output path:{FINAL_OUTPUT_VIDEO}')
    stitch_frames(BACKGROUND_REMOVED_FOLDER,FINAL_OUTPUT_VIDEO, FRAME_RATE)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Video Processed Elapsed time: {elapsed_time} seconds")

