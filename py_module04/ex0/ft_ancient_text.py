def reading_file(file: str) -> None:
    f = None
    try:
        f = open(file)
        print(f"Accessing Storage Vault: {file}")
        print("Connection established...\n")
        print("RECOVERED DATA:")

        content = f.read()
        print(content, "\n")

        print("Data recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except PermissionError:
        print("ERROR: Permission denied.")
    except Exception as err:
        print(f"ERROR: {err}")

    finally:
        if f is not None:
            f.close()


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    reading_file("ancient_fragment.txt")
