"""Minimal placeholder app for displaying risk maps."""

from pathlib import Path


def main() -> None:
    """Simulate launching the field application."""
    print("Launching avalanche risk map...")
    # TODO: integrate interactive mapping libraries such as Folium or PyQT
    if Path("../data/processed/risk_map.png").exists():
        print("Risk map available at data/processed/risk_map.png")
    else:
        print("No processed risk map found.")


if __name__ == "__main__":
    main()
