from PIL import Image

def merge_channels(grayscale_path, color_channel_paths, output_path, object_opacity):

    grayscale_image = Image.open(grayscale_path)
    merged_image = Image.new("RGBA", grayscale_image.size)

    grayscale_image = grayscale_image.convert("RGBA")
    grayscale_image.putalpha(255)
    merged_image.paste(grayscale_image, (0, 0), grayscale_image)

    for i, color_channel_path in enumerate(color_channel_paths):
        color_channel_image = Image.open(color_channel_path)

        color_channel_image = color_channel_image.convert("RGBA")
        pixels = color_channel_image.getdata()
        adjusted_pixels = [(r, g, b, 0) if (r, g, b) == (0, 0, 0) else (r, g, b, int(object_opacity * a)) for r, g, b, a in pixels]

        color_channel_image.putdata(adjusted_pixels)

        merged_image.paste(color_channel_image, (0, 0), color_channel_image)

    merged_image.save(output_path, format="TIFF")

if __name__ == "__main__":
    grayscale_path = "E:\\Atlas\\HSA_yz.tif"
    color_channel_paths = [
        "E:\\Atlas\\nucleus_isthmi_yz.tif",
        "E:\\Atlas\\pretectum_yz.tif",
        "E:\\Atlas\\dorsal_thalamus_proper_yz.tif",

    ]
    output_path = "E:\\Atlas\\final\\yz5.tif"
    object_opacity = 0.25  # Set opacity

    merge_channels(grayscale_path, color_channel_paths, output_path, object_opacity)
# "E:\\maskaver\\MAX_tectum.tif","E:\\Atlas\\tectum_xy.tif"
