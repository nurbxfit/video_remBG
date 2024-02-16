from rembg import remove
from rembg import new_session
import os

def remove_backgrounds(input_folder_path, output_folder_path):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder_path, exist_ok=True)
    
    # List all files in the input folder
    files = os.listdir(input_folder_path)
    
    # Iterate over each file in the input folder
    model_name = 'unet2'
    rembg_session = new_session(model_name,providers=["ROCMExecutionProvider","MIGraphXExecutionProvider","CPUExecutionProvider"])

    for filename in files:
        # Check if the file is an image (ends with .jpg or .png)
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Construct the input and output paths
            input_path = os.path.join(input_folder_path, filename)
            output_path = os.path.join(output_folder_path, filename)
            
            # Remove background from the image
            remove_background(input_path, output_path, rembg_session)

def remove_background(input_path, output_path,session):
    # Read input image as binary data
    with open(input_path, 'rb') as input_file:
        input_data = input_file.read()

    
    # Remove background
    output_data = remove(input_data,session=session)
    
    # Write output data to the output file
    with open(output_path, 'wb') as output_file:
        output_file.write(output_data)