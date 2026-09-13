from PIL import Image
import os
import glob

def split_and_save(image_path, output_dir='output', rows=2, cols=2):
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"❌ File not found: {image_path}")
        return 0
    except Exception as e:
        print(f"❌ Error opening image: {e}")
        return 0
    
    width, height = img.size
    
    print(f"📁 Processing: {os.path.basename(image_path)}")
    print(f"📏 Size: {width}x{height}px")
    print(f"🔲 Grid: {rows} rows x {cols} columns")
    
    cell_w = width // cols
    cell_h = height // rows
    
    # Warning if uneven division
    if width % cols != 0 or height % rows != 0:
        print(f"⚠️  Warning: Image won't divide evenly!")
        print(f"   Remaining pixels: w={width%cols}, h={height%rows}")
    
    saved_count = 0
    for i in range(rows):
        for j in range(cols):
            box = (j * cell_w, i * cell_h, (j + 1) * cell_w, (i + 1) * cell_h)
            cell = img.crop(box)
            filename = f'{output_dir}/piece_{i}_{j}.png'
            cell.save(filename)
            saved_count += 1
    
    print(f"\n✅ Done! {saved_count} pieces saved to '{output_dir}/'")
    return saved_count

# =============================
# AUTO-DISCOVER FIRST PNG
# =============================

png_files = glob.glob('*.png')

if png_files:
    IMAGE_FILE = png_files[0]
    print(f"Auto-selected: {IMAGE_FILE}")
else:
    IMAGE_FILE = None
    print("⚠️  No .png files found in current directory")

ROWS = 3  # Adjust to match your image
COLS = 3
OUTPUT_FOLDER = 'output_pieces'

if __name__ == '__main__':
    if IMAGE_FILE:
        split_and_save(IMAGE_FILE, output_dir=OUTPUT_FOLDER, rows=ROWS, cols=COLS)