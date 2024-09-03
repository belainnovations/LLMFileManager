def save_qr_code(qr_image, file_name):
    qr_image.save(f"{file_name}.png")

def rgba_to_hex(rgba):
    return '#{:02x}{:02x}{:02x}{:02x}'.format(*rgba)
