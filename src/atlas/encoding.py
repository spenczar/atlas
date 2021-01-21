from typing import List
import struct


def unpack_uint64s(data: bytes) -> List[int]:
    return list(x[0] for x in struct.iter_unpack(">Q", data))
