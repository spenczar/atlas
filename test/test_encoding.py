from typing import List

import atlas.encoding


class TestUint64Packing:
    def _test_unpacking(self, hexinput: str, expected: List[int]):
        byteinput = bytearray.fromhex(hexinput)
        have = atlas.encoding.unpack_uint64s(byteinput)
        assert have == expected

    def test_unpack_empty(self):
        self._test_unpacking("", [])

    def test_unpack_one(self):
        self._test_unpacking("0000000000000000", [0])

    def test_unpack_several(self):
        self._test_unpacking(
            "0000000000000001000000000000000200000000000000030000000000000004",
            [1, 2, 3, 4],
        )

    def test_unpack_large_several(self):
        self._test_unpacking(
            "00000001000000001000000000000000ffffffffffffffff",
            [1 << 32, 1 << 60, (1 << 64) - 1],
        )

    def test_unpack_single_large(self):
        self._test_unpacking(
            "ffffffffffffffff",
            [(1 << 64) - 1],
        )
