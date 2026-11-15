from db_access import authenticate, connect, is_allowed, seed_lab


def lab_db():
    conn = connect()
    seed_lab(conn)
    return conn


def test_real_secret_authenticates():
    conn = lab_db()
    assert authenticate(conn, "analyst", "lab-secret")


def test_wrong_secret_is_rejected():
    conn = lab_db()
    assert not authenticate(conn, "analyst", "nope")


def test_injection_text_is_not_sql():
    conn = lab_db()
    payload = "' OR '1'='1"
    assert not authenticate(conn, payload, payload)
    assert not authenticate(conn, "analyst", "' OR '1'='1")


def test_least_privilege_matrix():
    conn = lab_db()
    assert is_allowed(conn, "analyst", "read_ticket")
    assert not is_allowed(conn, "analyst", "create_user")
    assert not is_allowed(conn, "analyst", "export_all_customers")
    assert is_allowed(conn, "admin", "create_user")
    assert not is_allowed(conn, "admin", "export_all_customers")
    assert not is_allowed(conn, "guest", "read_ticket")
