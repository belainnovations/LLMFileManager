import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from PIL import Image

def generate_qr_code(data, error_correction="Low", box_size=10, border=4, fg_color=(0,0,0,255), bg_color=(255,255,255,255)):
    qr = qrcode.QRCode(
        version=1,
        error_correction={
            "Low": qrcode.constants.ERROR_CORRECT_L,
            "Medium": qrcode.constants.ERROR_CORRECT_M,
            "Quartile": qrcode.constants.ERROR_CORRECT_Q,
            "High": qrcode.constants.ERROR_CORRECT_H
        }[error_correction],
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white", image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())

    # Convert to RGBA mode to support transparency
    qr_image = qr_image.convert("RGBA")

    # Create new images for foreground and background
    fg_image = Image.new("RGBA", qr_image.size, (0, 0, 0, 0))
    bg_image = Image.new("RGBA", qr_image.size, (0, 0, 0, 0))

    # Apply custom colors and transparency
    for x in range(qr_image.width):
        for y in range(qr_image.height):
            pixel = qr_image.getpixel((x, y))
            if pixel[0] == 0:  # Black pixel (QR code body)
                fg_image.putpixel((x, y), fg_color)
            else:  # White pixel (surrounding area)
                bg_image.putpixel((x, y), bg_color)

    # Composite the foreground and background images
    final_image = Image.alpha_composite(bg_image, fg_image)

    return final_image
