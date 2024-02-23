from io import BytesIO
import qrcode


def create_qr_code(url):
    qr = qrcode.make(url)
    image_buffer = BytesIO()
    qr.save(image_buffer, format='PNG')
    return image_buffer.getvalue()