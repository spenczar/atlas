from typing import List
import struct


def pack_uint64(data: int) -> bytes:
    return struct.pack(">Q", data)


def pack_unit64_list(data: List[int]) -> bytes:
    result = b""
    for i in data:
        result += pack_uint64(i)
    return result


def unpack_uint64s(data: bytes) -> List[int]:
    return list(x[0] for x in struct.iter_unpack(">Q", data))
