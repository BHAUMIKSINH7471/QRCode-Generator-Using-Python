# -*- coding: utf-8 -*-
# Generate QR Code of any type.
# It's based on PyQRCode Library.

import pyqrcode
qr=pyqrcode.create('QrCode Generator')
qr.png('generator.png', scale=10)
