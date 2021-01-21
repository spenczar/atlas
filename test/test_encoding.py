from typing import List

import atlas.encoding
import pytest


class TestUint64Packing:
    def _test_unpacking(self, hexinput: str, expected: List[int]):
        byteinput = bytearray.fromhex(hexinput)
        have = atlas.encoding.unpack_uint64s(byteinput)
        assert have == expected

    def _test_pack(self, val: int, expected: str):
        have = atlas.encoding.pack_uint64(val)
        assert have == bytearray.fromhex(expected)

    def test_pack_zero(self):
        self._test_pack(0, "0000 0000 0000 0000")

    def test_pack_max(self):
        self._test_pack((1 << 64) - 1, "ffff ffff ffff ffff")

    def test_pack_overflow(self):
        with pytest.raises(Exception):
            atlas.encoding.pack_uint64(1 << 64)

    def test_unpack_empty(self):
        self._test_unpacking("", [])

    def test_unpack_one(self):
        self._test_unpacking("0000 0000 0000 0000", [0])

    def test_unpack_several(self):
        self._test_unpacking(
            "0000 0000 0000 0001"
            + "0000 0000 0000 0002"
            + "0000 0000 0000 0003"
            + "0000 0000 0000 0004",
            [1, 2, 3, 4],
        )

    def test_unpack_large_several(self):
        self._test_unpacking(
            "0000 0001 0000 0000" + "1000 0000 0000 0000" + "ffff ffff ffff ffff",
            [1 << 32, 1 << 60, (1 << 64) - 1],
        )

    def test_unpack_single_large(self):
        self._test_unpacking(
            "ffff ffff ffff ffff",
            [(1 << 64) - 1],
        )

    def test_unpack_incomplete_input(self):
        with pytest.raises(Exception):
            atlas.encoding.unpack_uint64s("1")
