from .spp_data import SppData


class RfcommPacket:
    def __init__(self, frame_number: int, src_address: str, dst_address: str, data: str):
        self.frame_number = frame_number
        self.src_address = src_address
        self.dst_address = dst_address
        self.data = SppData(data)

    def __str__(self):
        return ' '.join([
            self.frame_number,
            self.src_address,
            'to',
            self.dst_address,
            str(self.data)
        ])
