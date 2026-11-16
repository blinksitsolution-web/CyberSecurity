from ecb_byte_at_a_time import EcbOracle, discover_block_size, recover_secret, secret_length


def test_recovers_short_and_block_aligned_secrets():
    for secret in (b"X", b"SECRETS", b"A" * 15, b"A" * 16, b"A" * 17, b"BOOTCAMP-SECRET!!"):
        oracle = EcbOracle(secret, key=b"0123456789abcdef")
        assert discover_block_size(oracle) == 16
        assert secret_length(oracle, 16) == len(secret)
        assert recover_secret(oracle) == secret


def test_zero_byte_inside_the_secret_is_kept():
    secret = b"AB\x00CD"
    oracle = EcbOracle(secret, key=b"fedcba9876543210")
    assert recover_secret(oracle) == secret


def test_trailing_zero_is_recovered_when_the_length_is_known():
    secret = b"END\x00"
    oracle = EcbOracle(secret, key=b"0123456789abcdef")
    assert recover_secret(oracle) == secret
