"""Build a reproducible, source-only archive of the complete public sample unit."""

from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "teaching-sample"
OUTPUT = ROOT / "downloads" / "applied-ai-sample.zip"
ALLOWED_SUFFIXES = {".py", ".md", ".json"}


def main():
    files = sorted(
        path for path in SOURCE.rglob("*")
        if path.is_file() and path.suffix in ALLOWED_SUFFIXES
        and "__pycache__" not in path.parts
    )
    if not files:
        raise RuntimeError("No teaching sample sources found")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            relative = path.relative_to(SOURCE).as_posix()
            info = zipfile.ZipInfo(relative, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
    print("Built " + str(OUTPUT.relative_to(ROOT)) + " with " + str(len(files)) + " files")


if __name__ == "__main__":
    main()
