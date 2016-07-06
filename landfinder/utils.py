# -*- coding: utf-8 -*-
try:
    from PIL import Image, ImageDraw
except ImportError:
    import Image, ImageDraw

import qrcode
import qrcode.image.pil


class PilImage(qrcode.image.pil.PilImage):
    kind = "PNG"

    def new_image(self, **kwargs):
        kwargs["fill_color"] = "transparent"
        return super(PilImage, self).new_image(**kwargs)


def make_qr_code(string):
    return qrcode.make(string, box_size=20, border=1, image_factory=PilImage)
