from pathlib import Path


def test_expected_repo_surfaces_exist() -> None:
    root = Path(__file__).resolve().parents[1]

    expected = [
        root / "README.md",
        root / "pyproject.toml",
        root / "src" / "lens_template" / "__init__.py",
        root / "src" / "lens_template" / "lens.py",
        root / "docs" / "interface.md",
        root / "docs" / "expected-inputs.md",
        root / "docs" / "expected-outputs.md",
        root / "docs" / "whitepaper.md",
        root / "examples" / "README.md",
    ]

    for path in expected:
        assert path.exists(), f"Missing expected file: {path}"