#!/usr/bin/env python3
"""
Gamma.app API client for AI ToolKit / Reese Astor workflows.
Usage:
  export GAMMA_API_KEY=sk-gamma-...
  python scripts/gamma_client.py
"""

import os
import time
import requests
from typing import Optional, Dict, Any

GAMMA_API_URL = "https://public-api.gamma.app/v1.0"
API_KEY = os.getenv("GAMMA_API_KEY")

if not API_KEY:
    raise RuntimeError("Set GAMMA_API_KEY environment variable first")

HEADERS = {
    "X-API-KEY": API_KEY,
    "Content-Type": "application/json",
}


def create_generation(input_text: str, **kwargs) -> str:
    """Create a generation. Returns generationId."""
    payload = {
        "inputText": input_text,
        "textMode": kwargs.get("text_mode", "generate"),
        "format": kwargs.get("format", "presentation"),
        "numCards": kwargs.get("num_cards", 8),
    }
    if kwargs.get("title"):
        payload["title"] = kwargs["title"]
    if kwargs.get("theme_id"):
        payload["themeId"] = kwargs["theme_id"]
    if kwargs.get("export_as"):
        payload["exportAs"] = kwargs["export_as"]

    resp = requests.post(f"{GAMMA_API_URL}/generations", headers=HEADERS, json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()["generationId"]


def get_generation(generation_id: str) -> Dict[str, Any]:
    resp = requests.get(f"{GAMMA_API_URL}/generations/{generation_id}", headers={"X-API-KEY": API_KEY}, timeout=30)
    resp.raise_for_status()
    return resp.json()


def poll_until_done(generation_id: str, timeout: int = 180) -> Dict[str, Any]:
    start = time.time()
    while time.time() - start < timeout:
        data = get_generation(generation_id)
        status = data.get("status")
        if status in ("completed", "failed"):
            return data
        print(f"  Status: {status} ...")
        time.sleep(5)
    raise TimeoutError("Timed out waiting for generation")


def generate(input_text: str, **kwargs) -> Dict[str, Any]:
    """Convenience: create + poll."""
    gen_id = create_generation(input_text, **kwargs)
    print(f"Started generation: {gen_id}")
    result = poll_until_done(gen_id)
    return result


if __name__ == "__main__":
    example = generate(
        "AI ToolKit: Best automation tools and workflows for indie creators 2026",
        format="presentation",
        num_cards=7,
        title="AI ToolKit Highlights",
    )
    print("\n=== Result ===")
    print("Status:", example.get("status"))
    print("Gamma URL:", example.get("gammaUrl"))
    print("Export URL:", example.get("exportUrl"))
