"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import exlcm.HEADER

class Image(object):
    __slots__ = ["header", "nWidth", "nHeight", "gbImageData"]

    def __init__(self):
        self.header = exlcm.HEADER()
        self.nWidth = 0
        self.nHeight = 0
        self.gbImageData = []

    def encode(self):
        buf = BytesIO()
        buf.write(Image._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        assert self.header._get_packed_fingerprint() == exlcm.HEADER._get_packed_fingerprint()
        self.header._encode_one(buf)
        buf.write(struct.pack("<ii", self.nWidth, self.nHeight))
        for i0 in range(self.nHeight):
            buf.write(bytearray(self.gbImageData[i0][:self.nWidth]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != Image._get_packed_fingerprint():
            raise ValueError("Decode error")
        return Image._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = Image()
        self.header = exlcm.HEADER._decode_one(buf)
        self.nWidth, self.nHeight = struct.unpack("<ii", buf.read(8))
        self.gbImageData = []
        for i0 in range(self.nHeight):
            self.gbImageData.append(buf.read(self.nWidth))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if Image in parents: return 0
        newparents = parents + [Image]
        tmphash = (0x88f959495096bc7d+ exlcm.HEADER._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if Image._packed_fingerprint is None:
            Image._packed_fingerprint = struct.pack("<Q", Image._get_hash_recursive([]))
        return Image._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

