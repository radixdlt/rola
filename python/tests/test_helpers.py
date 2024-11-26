from secrets import token_bytes

from rola.exceptions.helpers import ChallengeWrongLength, DappAddressWrongLength
from rola.utils.helpers import create_public_key_hash, create_signature_message


def test_create_public_key_hash():
    public_key = "a6b8a053f51c1f945317bef5f5344321783b243821e919448c5963b9a8a20552"
    expected_hash = "31eeca0fe8fb2d06fe3b4006bf0c10b1942488e529282fde64f3954daf"
    assert create_public_key_hash(bytes.fromhex(public_key)) == expected_hash


def test_create_key_with_invalid_hex():
    invalid_public_key = "invalid_hex"
    assert create_public_key_hash(invalid_public_key) == ""


def test_create_public_key_hash_returns_29_length_hex_string():
    public_key = "a6b8a053f51c1f945317bef5f5344321783b243821e919448c5963b9a8a20552"
    public_key_hash_hex = create_public_key_hash(bytes.fromhex(public_key))
    assert len(public_key_hash_hex) == 58


def test_create_signature_message_returns_32_bytes_length_message():
    challenge = token_bytes(32)
    message = create_signature_message(
        challenge=challenge,
        dapp_definition_address="account_tdx_2_12xdm5g7xdhh73zkh7xkty0dsxw4rw0jl0sq4lr3erpc3xdn54zx0le",
        origin="test-origin",
    )
    assert len(message) == 32
    assert isinstance(message, bytes)


def test_create_signature_message_raises_challenge_wrong_length():
    exception_raised = False
    challenge = token_bytes(64)
    try:
        create_signature_message(
            challenge=challenge,
            dapp_definition_address="account_tdx_2_12xdm5g7xdhh73zkh7xkty0dsxw4rw0jl0sq4lr3erpc3xdn54zx0le",
            origin="test-origin",
        )
    except ChallengeWrongLength:
        exception_raised = True
    assert exception_raised


def test_create_signature_message_raises_dapp_address_wrong_length():
    exception_raised = False
    challenge = token_bytes(32)
    try:
        create_signature_message(
            challenge=challenge,
            dapp_definition_address="account_tdx",
            origin="test-origin",
        )
    except DappAddressWrongLength:
        exception_raised = True
    assert exception_raised


def test_create_signature_message_returns_the_right_format():
    challenge = bytes.fromhex(
        "4b4e32daa074b8860b02c71e28cb218f4d0cc30faab91929d5fc19a09d4b102b"
    )
    message = create_signature_message(
        challenge=challenge,
        dapp_definition_address="account_tdx_2_12xdm5g7xdhh73zkh7xkty0dsxw4rw0jl0sq4lr3erpc3xdn54zx0le",
        origin="test-origin",
    )
    assert (
        message.hex()
        == "59bfb02f2c74377816c0b48051e484ba11ba6e5d1b5be967308dbf698862bcb1"
    )
