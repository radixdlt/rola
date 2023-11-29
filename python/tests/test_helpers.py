from rola.utils.helpers import create_public_key_hash


def test_create_public_key_hash():
    public_key = "a6b8a053f51c1f945317bef5f5344321783b243821e919448c5963b9a8a20552"
    expected_hash = "31eeca0fe8fb2d06fe3b4006bf0c10b1942488e529282fde64f3954daf"
    assert create_public_key_hash(public_key) == expected_hash


def test_create_key_with_invalid_hex():
    invalid_public_key = "invalid_hex"
    assert create_public_key_hash(invalid_public_key) == ""
