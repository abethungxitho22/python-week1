records = {}


def add_record(record_id, name, department, device):
    """Add a record. Raises ValueError for blank fields or duplicate IDs."""
    for label, value in (("record_id", record_id), ("name", name),
                         ("department", department), ("device", device)):
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError(f"{label} must be a non-empty string")

    if record_id in records:
        raise ValueError(f"Record {record_id} already exists")

    records[record_id] = {
        "name": name,
        "department": department,
        "device": device,
    }
    print("Record", record_id, "added.")


def get_record(record_id):
    """Return a record. Raises KeyError if it does not exist."""
    if record_id not in records:
        raise KeyError(f"No record found with ID {record_id}")
    return records[record_id]


def delete_record(record_id):
    """Delete a record. Raises KeyError if it does not exist."""
    if record_id not in records:
        raise KeyError(f"No record found with ID {record_id}")
    del records[record_id]
    print("Record", record_id, "deleted.")


if __name__ == "__main__":
    try:
        add_record("E001", "Thabo Mokoena", "IT", "Laptop-04")
        add_record("E002", "Sarah Adams", "Finance", "Desktop-11")
        add_record("E001", "Duplicate", "IT", "Laptop-99")   # will be rejected
    except ValueError as error:
        print("Could not add record:", error)

    try:
        print(get_record("E999"))                             # does not exist
    except KeyError as error:
        print("Lookup failed:", error)

    print(records)