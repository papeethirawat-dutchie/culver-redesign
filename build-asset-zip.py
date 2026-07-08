#!/usr/bin/env python3
"""Regenerate assets/library/culver-redesign-assets.zip from the files
referenced on asset-library.html. Run this after adding/changing any
asset shown on that page."""
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent

FILES = [
    "assets/culver-script-logo.svg",
    "assets/library/logo/culver-logo.png",
    "assets/library/logo/culver-logo-horizontal-dark.svg",
    "assets/library/logo/culver-logo-horizontal-dark.png",
    "assets/library/logo/culver-logo-stacked-dark.svg",
    "assets/library/logo/culver-logo-stacked-dark.png",
    "assets/library/logo/culver-logo-stacked-cream.svg",
    "assets/library/logo/culver-logo-stacked-cream.png",
    "assets/hero.png",
    "assets/retail-west/carousel/slide-1-rewards.png",
    "assets/retail-west/carousel/slide-2-ai.png",
    "assets/retail-west/carousel/slide-3-paybybank.png",
    "assets/retail-west/categories/culver-curated.svg",
    "assets/retail-west/categories/flower.svg",
    "assets/retail-west/categories/edibles.svg",
    "assets/retail-west/categories/vapes.svg",
    "assets/retail-west/categories/pre-rolls.svg",
    "assets/retail-west/categories/concentrates.svg",
    "assets/retail-west/categories/topicals.svg",
    "assets/retail-west/categories/gear.svg",
    "assets/retail-west/categories/tinctures.svg",
    "assets/retail-west/categories/accessories.svg",
    "assets/library/categories/culver-curated.png",
    "assets/library/categories/flower.png",
    "assets/library/categories/edibles.png",
    "assets/library/categories/vapes.png",
    "assets/library/categories/pre-rolls.png",
    "assets/library/categories/concentrates.png",
    "assets/library/categories/topicals.png",
    "assets/library/categories/gear.png",
    "assets/library/categories/tinctures.png",
    "assets/library/categories/accessories.png",
    "assets/library/culver-collection/dark-chocolate-wafer-bites.png",
    "assets/library/culver-collection/pre-packed-cannabis-flower.png",
    "assets/library/culver-collection/white-choc-chip-cookies.png",
    "assets/library/culver-collection/rso-dark-chocolate.png",
    "assets/library/culver-collection/culver-club-hoodie.png",
    "assets/library/culver-collection/culver-club-hat.png",
    "assets/library/culver-collection/culver-club-mug.png",
    "assets/library/specials/special-prerolls-clean.png",
    "assets/library/specials/special-bogo-clean.png",
    "assets/library/specials/special-buy3-get1-free-clean.png",
]

zip_path = ROOT / "assets/library/culver-redesign-assets.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for rel in FILES:
        src = ROOT / rel
        # flatten into folders matching the page sections, not the source tree
        zf.write(src, arcname=rel.split("assets/")[-1])

print(f"Wrote {zip_path} with {len(FILES)} files")
