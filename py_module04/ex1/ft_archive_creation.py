def writing_in_file(file: str, content: list[str]) -> None:
    try:
        f = None
        f = open(file, "w")
        print(f"Initializing new storage unit: {file}")
        print("Storage unit created successfully...")
        print()

        print("Inscribing preservation data...")
        for line in content:
            f.write(line + "\n")
            print(line)

        print()
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{file}' ready for long-term preservation.")

    except PermissionError:
        print("ERROR: Permission denied.")
    except Exception as err:
        print(f"Error: {err}")
    finally:
        if f is not None:
            f.close()


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    file = "new_discovery.txt"
    content = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee",
    ]
    writing_in_file(file, content)
