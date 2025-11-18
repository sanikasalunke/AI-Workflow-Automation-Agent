from typing import Any

def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(payload: dict) -> str:
    """
    payload: {"path": "out.txt", "content": "text"}
    """
    path = payload.get("path")
    content = payload.get("content", "")
    if not path:
        raise ValueError("No path provided")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Wrote {len(content)} chars to {path}"
