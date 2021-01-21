from __future__ import annotations
import pathlib
import plyvel


def open_db(path: str) -> Database:
    return Database(path)


class Database:
    db_root: pathlib.Path
    candidates: plyvel.DB

    def __init__(self, db_path: str):
        self.db_root = pathlib.Path(db_path)
        self.candidates = plyvel.DB(str(self.db_root / "candidates"))
