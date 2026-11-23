#!/usr/bin/env python3
"""Parse a trusted-author issue body and POST the task JSON to the Klaus webhook.

Issue text is read only from environment variables (never interpolated into a shell).
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request

WEBHOOK_URL = "https://api2.cursor.sh/automations/webhook/056c7bee-0dc7-5af9-bd32-98cad3465827"
ALLOWED_KEYS = ("staf", "jabatan", "tugas", "prioritas", "tenggat", "dikirim_pada", "sumber")
JSON_BLOCK = re.compile(
    r"<!--\s*tugas-json\s*-->\s*```json\s*(\{.*?\})\s*```",
    re.DOTALL | re.IGNORECASE,
)


def fail(message: str, code: int = 1) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(code)


def as_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def extract_payload(body: str) -> dict:
    match = JSON_BLOCK.search(body or "")
    if not match:
        fail("Tidak menemukan blok JSON tugas (<!-- tugas-json --> + ```json) di isi issue.")
    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        fail(f"Blok JSON tugas tidak valid: {exc}")
    if not isinstance(data, dict):
        fail("Blok JSON tugas harus berupa objek.")
    payload = {key: as_text(data.get(key, "")).strip() if key != "tugas" else as_text(data.get(key, "")) for key in ALLOWED_KEYS}
    payload["tugas"] = str(payload.get("tugas") or "").strip()
    payload["sumber"] = "kantor-virtual-3d"
    if not payload["tugas"]:
        fail("Field 'tugas' kosong.")
    if not payload["staf"]:
        fail("Field 'staf' kosong.")
    return payload


def authorization_header(raw: str) -> str:
    value = (raw or "").strip().strip('"').strip("'").strip()
    if value.lower().startswith("authorization:"):
        value = value.split(":", 1)[1].strip()
    if not value:
        fail("Secret GROK_WEBHOOK_AUTH belum diisi.")
    if not value.lower().startswith("bearer "):
        value = "Bearer " + value
    return value


def post_webhook(payload: dict, auth: str) -> None:
    request = urllib.request.Request(
        WEBHOOK_URL,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": auth,
            "User-Agent": "kantor-virtual-3d-relay",
            "Accept": "application/json, */*",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            status = getattr(response, "status", 200)
            body = response.read(2000)
    except urllib.error.HTTPError as exc:
        detail = exc.read(2000)
        fail(f"Webhook merespons HTTP {exc.code}: {detail[:500]!r}")
    except urllib.error.URLError as exc:
        fail(f"Gagal menghubungi webhook: {exc}")
    if not (200 <= int(status) < 300):
        fail(f"Webhook merespons HTTP {status}: {body[:500]!r}")
    print(f"Webhook OK ({status})")


def main() -> None:
    payload = extract_payload(os.environ.get("ISSUE_BODY") or "")
    payload["issue_url"] = (os.environ.get("ISSUE_URL") or "").strip()
    post_webhook(payload, authorization_header(os.environ.get("AUTH_RAW") or ""))


if __name__ == "__main__":
    main()
