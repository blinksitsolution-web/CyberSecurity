from caesar import brute_force, decrypt, encrypt

CIPHERTEXT = "XLMW MW E WIGVIX QIWWEKI"
PLAINTEXT = "THIS IS A SECRET MESSAGE"


def test_shift_four_decrypts_the_assignment_ciphertext():
    assert decrypt(CIPHERTEXT, 4) == PLAINTEXT


def test_encrypt_and_decrypt_round_trip_and_keep_spaces():
    assert encrypt(PLAINTEXT, 4) == CIPHERTEXT
    assert decrypt("HELLO WORLD", 0) == "HELLO WORLD"
    assert " " in decrypt(CIPHERTEXT, 7)


def test_brute_force_ranks_shift_four_first_and_tries_every_shift():
    rows = brute_force(CIPHERTEXT)
    assert len(rows) == 25
    assert {row["shift"] for row in rows} == set(range(1, 26))
    assert rows[0]["shift"] == 4
    assert rows[0]["plaintext"] == PLAINTEXT
