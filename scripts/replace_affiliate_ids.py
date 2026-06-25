"""
Replace placeholder affiliate tracking parameters with real IDs.

SAFETY:
- Default mode is DRY RUN (lists what would change, changes nothing).
- Use --apply only after filling in real IDs below.
- Refuses to apply if any ID still contains "YOUR_" placeholder.
"""
import re, argparse
from pathlib import Path

# CONFIG: replace these with your real affiliate parameters once approved.
# Example: "?via=aitoolkit" will become "?via=reese123"
AFFILIATE_IDS = {
    "copy.ai": "?via=YOUR_COPYAI_ID",
    "writesonic.com": "?via=YOUR_WRITESONIC_ID",
    "jasper.ai": "?via=YOUR_JASPER_ID",
    "adcreative.ai": "?via=YOUR_ADCREATIVE_ID",
    "synthesia.io": "?via=YOUR_SYNTHESIA_ID",
    "speechify.com": "?via=YOUR_SPEECHIFY_ID",
    "canva.com": "?via=YOUR_CANVA_ID",
    "surferseo.com": "?via=YOUR_SURFER_ID",
}

EXTENSIONS = (".html", ".md", ".js", ".json")

def has_placeholders():
    return any("YOUR_" in v for v in AFFILIATE_IDS.values())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Actually write changes to files")
    args = parser.parse_args()

    if args.apply and has_placeholders():
        print("ERROR: You still have YOUR_* placeholder IDs in AFFILIATE_IDS.")
        print("Fill in real IDs before running with --apply.")
        return 1

    total_matches = 0
    files_with_matches = []

    for ext in EXTENSIONS:
        for path in Path(".").rglob(f"*{ext}"):
            if any(part.startswith((".", "node_modules", "venv")) for part in path.parts):
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except Exception:
                continue
            new_text = text
            file_matches = 0
            for domain, aff_id in AFFILIATE_IDS.items():
                pattern = re.compile(
                    rf'(https?://[^"\'\s]*{re.escape(domain)}[^"\'\s]*)\?via=aitoolkit',
                    re.IGNORECASE,
                )
                matches = pattern.findall(new_text)
                if matches:
                    if args.apply:
                        new_text = pattern.sub(rf"\1{aff_id}", new_text)
                    file_matches += len(matches)
                    total_matches += len(matches)
            if file_matches:
                files_with_matches.append((str(path), file_matches))
                if args.apply and new_text != text:
                    path.write_text(new_text, encoding="utf-8")

    if not files_with_matches:
        print("No ?via=aitoolkit placeholders found. Nothing to do.")
        return 0

    for p, n in files_with_matches:
        print(f"{p}: {n} replacement(s)")

    print(f"\nTotal replacements: {total_matches}")
    if not args.apply:
        print("\nDRY RUN — no files changed. Run with --apply after setting real IDs.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
