import sys
from pathlib import Path


def main():
    package_name = sys.argv[1]
    pkg_dir = Path(package_name)
    pkg_dir.mkdir(parents=True, exist_ok=True)
    (pkg_dir / "__init__.py").write_text("# generated\n", encoding="utf-8")
    print(f"created package: {pkg_dir}")


if __name__ == "__main__":
    main()
