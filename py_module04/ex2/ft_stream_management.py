import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")
    print(f"\n[STANDARD] Archive status from {archivist_id}: {status_report}")
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys.stderr
    )

    print("[STANDARD] Data transmission complete\n")
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    try:
        main()
    except (Exception, KeyboardInterrupt):
        print("\nan error occured during program runtime !")
