import pytest
import shutil
import tempfile
import pathlib

import atlas


@pytest.fixture(scope="function")
def leveldb_5k():
    """Copy the testdata/leveldbs/alerts.db.5k database to a temporary directory,
    scoped to a single test invocation.

    """
    db_path = "testdata/leveldbs/alerts.db.5k"
    with tempfile.TemporaryDirectory(prefix="test-alerts-5k-") as tmp_dir:
        tmp_db = pathlib.Path(tmp_dir) / "alerts.db.5k"
        shutil.copytree(db_path, tmp_db)
        yield tmp_db


class TestDatabase:
    def test_open_database(self, leveldb_5k):
        atlas.open_db(leveldb_5k)

    def test_open_missing_db(self):
        with pytest.raises(Exception):
            atlas.open_db("bogus")
