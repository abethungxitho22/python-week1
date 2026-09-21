def validate_account(username, email):
    """Return (is_valid, reason) for one account. Never crashes on bad data."""
    if not isinstance(username, str) or not isinstance(email, str):
        return False, "username and email must be text"

    if username.strip() == "":
        return False, "username is empty"

    if email.count("@") != 1:
        return False, "email must contain exactly one @"

    local, domain = email.split("@")
    if local == "":
        return False, "email has nothing before the @"
    if "." not in domain:
        return False, "email domain is missing a dot"

    return True, "OK"


def validate_accounts(accounts):
    """Validate a list of (username, email) entries.

    Returns a list of (username, email, is_valid, reason).
    Malformed entries are reported as invalid instead of stopping the loop.
    """
    results = []
    for entry in accounts:
        try:
            username, email = entry
        except (TypeError, ValueError):
            results.append((entry, None, False, "entry is not a (username, email) pair"))
            continue
        is_valid, reason = validate_account(username, email)
        results.append((username, email, is_valid, reason))
    return results


if __name__ == "__main__":
    accounts = [
        ("jdoe", "jdoe@company.com"),
        ("asmith", "asmith@company"),
        ("bthabo", "bthabo@company.com"),
        ("", "empty@company.com"),
        None,
    ]

    for username, email, is_valid, reason in validate_accounts(accounts):
        status = "VALID" if is_valid else "INVALID"
        print(username, "-", email, "->", status, f"({reason})")