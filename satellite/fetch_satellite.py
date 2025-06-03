"""Placeholder module for downloading satellite imagery."""

from pathlib import Path


def download_satellite_imagery(destination: Path) -> None:
    """Simulate a satellite imagery download."""
    destination.mkdir(parents=True, exist_ok=True)
    # TODO: integrate with real remote sensing APIs such as SentinelHub or NASA
    (destination / "README.txt").write_text("Satellite imagery would be stored here")


if __name__ == "__main__":
    download_satellite_imagery(Path("../data/raw/satellite"))
    print("Satellite data placeholder created.")
