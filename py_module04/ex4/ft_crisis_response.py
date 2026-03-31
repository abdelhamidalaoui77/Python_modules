def crisis(filename: str, mode: str) -> None:
    try:
        if mode == "routine":
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
        else:
            print(f"CRISIS ALERT: Attempting access to '{filename}'...")

        with open(filename, "r") as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - '{content.strip()}'")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception as err:
        print("RESPONSE: Unexpected system anomaly detected")
        print(f"DETAILS: {err}")
        print("STATUS: Crisis contained, investigation ongoing")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    crisis("lost_archive.txt", "crisis")
    crisis("classified_vault.txt", "crisis")
    crisis("standard_archive.txt", "routine")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
