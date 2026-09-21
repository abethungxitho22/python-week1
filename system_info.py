import platform
import os
import getpass


def get_system_info():
    """Collect system info and return it as a dictionary."""
    try:
        current_user = getpass.getuser()
    except (OSError, KeyError):
        current_user = "Unknown"

    info = {
        "Operating System": platform.system() or "Unknown",
        "OS Version": platform.version() or "Unknown",
        "Machine Type": platform.machine() or "Unknown",
        "Python Version": platform.python_version(),
        "Current User": current_user,
        "Current Directory": os.getcwd(),
        "Number of CPUs": os.cpu_count() or "Unknown",
    }
    return info


def display_system_info(info):
    """Print the info dictionary as a formatted report."""
    if not isinstance(info, dict):
        raise TypeError("info must be a dictionary")

    print("=" * 40)
    print("SYSTEM INFORMATION REPORT")
    print("=" * 40)
    for key, value in info.items():
        print(f"{key}: {value}")
    print("=" * 40)


if __name__ == "__main__":
    try:
        data = get_system_info()
        display_system_info(data)
    except OSError as error:
        print("Could not read system information:", error)