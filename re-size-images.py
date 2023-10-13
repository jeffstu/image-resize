from PIL import Image
import os
import sys
import shutil

def process_image(file_path, output_path, min_size_kb=1024, max_size_kb=2900):
    with Image.open(file_path) as img:
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        for quality in range(100, 50, -5):
            img.save(output_path, 'JPEG', quality=quality)
            output_size_kb = os.path.getsize(output_path) // 1024
            
            if min_size_kb <= output_size_kb <= max_size_kb:
                return True
            elif output_size_kb < min_size_kb:
                shutil.copy2(file_path, output_path)
                print(f"Failed to compress {file_path} above {min_size_kb}KB without going below 50 quality. Using original.")
                return False
        
        print(f"Cannot compress {file_path} to be under {max_size_kb}KB without reducing quality below 50. Using original.")
        shutil.copy2(file_path, output_path)
        return False

def process_directory(input_dir, output_dir_web, output_dir_pp):
    if not os.path.exists(output_dir_web):
        os.makedirs(output_dir_web)
    if not os.path.exists(output_dir_pp):
        os.makedirs(output_dir_pp)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path_web = os.path.join(output_dir_web, filename)
            output_path_pp = os.path.join(output_dir_pp, filename)

            process_image(input_path, output_path_web, min_size_kb=0, max_size_kb=2500)  # web-sized images reduced for web use
            process_image(input_path, output_path_pp, min_size_kb=1024, max_size_kb=2900)  # Using 2900KB as a limit for Images to Upload to purpleport.co.uk to keep under their 3MB limit.

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py [path_to_your_images]")
        sys.exit(1)

    input_directory = sys.argv[1]
    web_sized_output_directory = os.path.join(input_directory, "web_sized")
    purple_port_sized_output_directory = os.path.join(input_directory, "PurplePort_sized")
    
    process_directory(input_directory, web_sized_output_directory, purple_port_sized_output_directory)
