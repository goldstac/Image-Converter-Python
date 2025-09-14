import os
from PIL import Image

VALID_FORMATS = {"png", "jpg", "jpeg", "webp"}

def convert_image(input_path, output_path):
    out_ext = os.path.splitext(output_path)[1].lower().lstrip(".")
    if out_ext not in VALID_FORMATS:
        print(f"❌ Output must end with one of: {', '.join(VALID_FORMATS)}")
        return

    try:
        with Image.open(input_path) as img:
            if out_ext in {"jpg", "jpeg"} and img.mode in ("RGBA", "LA"):
                bg = Image.new("RGB", img.size, (255, 255, 255))
                bg.paste(img, mask=img.split()[-1])
                img = bgF
            elif img.mode not in ("RGB", "RGBA"):
                img = img.convert("RGB")

            pillow_format = "JPEG" if out_ext in {"jpg", "jpeg"} else out_ext.upper()
            img.save(output_path, format=pillow_format)
            print(f"✅ Converted → {output_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

def show_instructions():
    print("""
Image Converter
---------------
Type your commands like:
image.png -- image.webp
Press Enter on a blank line to quit.
Supported formats: png, jpg, jpeg, webp
""")

def main():
    show_instructions()
    while True:
        cmd = input("> ").strip()
        if not cmd:
            print("Goodbye!")
            break

        if " -- " not in cmd:
            print("❌ Use the format: input.png -- output.webp")
            continue

        input_path, output_path = map(str.strip, cmd.split(" -- ", 1))
        convert_image(input_path, output_path)

if __name__ == "__main__":
    main()
