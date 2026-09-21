from password_checker import check_password
from account_validator import validate_account, validate_accounts
import record_manager
from system_info import get_system_info


def expect_error(error_type, func, *args):
    """Helper: pass if func(*args) raises error_type, fail otherwise."""
    try:
        func(*args)
    except error_type:
        return
    raise AssertionError(f"{func.__name__}{args} should have raised {error_type.__name__}")


# --- password_checker ---
def test_empty_password():
    expect_error(ValueError, check_password, "")

def test_non_string_password():
    expect_error(TypeError, check_password, 12345)

def test_weak_password():
    assert check_password("abc")[1] == "Weak"

def test_strong_password():
    score, rating, _ = check_password("Str0ng!Pass#2026")
    assert score == 5 and rating == "Strong"


# --- account_validator ---
def test_valid_account():
    assert validate_account("jdoe", "jdoe@company.com")[0] is True

def test_invalid_email_no_dot():
    assert validate_account("asmith", "asmith@company")[0] is False

def test_empty_username():
    assert validate_account("", "empty@company.com")[0] is False

def test_bad_entry_does_not_crash():
    results = validate_accounts([("jdoe", "jdoe@company.com"), None])
    assert results[0][2] is True and results[1][2] is False


# --- record_manager ---
def test_add_and_get_record():
    record_manager.records.clear()
    record_manager.add_record("T1", "Test User", "IT", "Laptop-01")
    assert record_manager.get_record("T1")["name"] == "Test User"

def test_duplicate_record_rejected():
    record_manager.records.clear()
    record_manager.add_record("T1", "Test User", "IT", "Laptop-01")
    expect_error(ValueError, record_manager.add_record, "T1", "Other", "IT", "Laptop-02")

def test_missing_record():
    record_manager.records.clear()
    expect_error(KeyError, record_manager.get_record, "NOPE")


# --- system_info ---
def test_system_info_has_keys():
    info = get_system_info()
    assert "Operating System" in info and "Python Version" in info


if __name__ == "__main__":
    tests = [f for name, f in list(globals().items()) if name.startswith("test_")]
    passed = 0
    for test in tests:
        try:
            test()
            print("PASS", test.__name__)
            passed += 1
        except AssertionError as error:
            print("FAIL", test.__name__, "-", error)
    print(f"\n{passed}/{len(tests)} tests passed")