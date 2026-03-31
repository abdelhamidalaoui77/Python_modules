def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    try:
        print("\nSECURE EXTRACTION:")
        with open("classified_data.txt", "r") as file:
            for line in file:
                print(line, end="")

        print("\n")
        print("SECURE PRESERVATION:")
        with open("security_protocols.txt", "w") as file:
            file.write("[CLASSIFIED] New security protocols archived\n")
            print("[CLASSIFIED] New security protocols archived")

        print("Vault automatically sealed upon completion")

    except FileNotFoundError:
        print("ERROR: Classified vault not found.")
    except PermissionError:
        print("ERROR: Permission denied.")

    print()
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
