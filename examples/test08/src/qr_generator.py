import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from PIL import Image

def generate_qr_code(data, error_correction="Low", box_size=10, border=4):
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
    return qr.make_image(fill_color="black", back_color="white", image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
