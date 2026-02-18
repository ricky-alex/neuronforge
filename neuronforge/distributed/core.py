"""Core implementation for distributed."""

from __future__ import annotations
from typing import Any, Dict, Optional


class DistributedManager:
    """Manages multi-gpu training."""

    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self._initialized = False

    def initialize(self) -> None:
        self._initialized = True

    def process(self, data: Any) -> Any:
        if not self._initialized:
            self.initialize()
        return data

    def __repr__(self) -> str:
        return f"DistributedManager(initialized={self._initialized})"
