import json
from pathlib import Path
from typing import Dict, List

VAULT_FILE = Path.home() / ".not-a-passwords.never.com" / "vault.json"


class Vault:
    def __init__(self, path: Path = VAULT_FILE) -> None:
        self.path = path
        self.path.parent.mkdir(exist_ok=True)
        if not self.path.exists():
            self.path.write_text("[]\n")

    def _entries(self) -> List[Dict]:
        return json.loads(self.path.read_text())

    def save_entry(self, site: str, user: str, password: str):
        entries = self._entries()
        entries.append({"site": site, "user": user, "password": password})
        self.path.write_text(json.dumps(entries, indent=4))

    def entries_list(self):
        return self._entries()
