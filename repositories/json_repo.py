from __future__ import annotations

import json
from pathlib import Path
from typing import List

from models import App, LLM, Evaluator, AppEvaluator, RawPrompt


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def _read_json_array(path: Path) -> list:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


class JsonRepository:
    def __init__(
        self,
        apps: List[App],
        llms: List[LLM],
        evaluators: List[Evaluator],
        app_evaluators: List[AppEvaluator],
        raw_prompts: List[RawPrompt],
    ) -> None:
        self._apps = apps
        self._llms = llms
        self._evaluators = evaluators
        self._app_evaluators = app_evaluators
        self._raw_prompts = raw_prompts

    @staticmethod
    def load(data_dir: Path = DATA_DIR) -> JsonRepository:
        apps = [App(**item) for item in _read_json_array(data_dir / "apps.json")]
        llms = [LLM(**item) for item in _read_json_array(data_dir / "llms.json")]
        evaluators = [Evaluator(**item) for item in _read_json_array(data_dir / "evaluators.json")]
        app_evaluators = [AppEvaluator(**item) for item in _read_json_array(data_dir / "app_evaluators.json")]
        raw_prompts = [RawPrompt(**item) for item in _read_json_array(data_dir / "raw_prompts.json")]
        return JsonRepository(apps, llms, evaluators, app_evaluators, raw_prompts)

    # Exposed getters (like an in-memory DB)
    def list_apps(self) -> List[App]:
        return list(self._apps)

    def list_llms(self) -> List[LLM]:
        return list(self._llms)

    def list_evaluators(self) -> List[Evaluator]:
        return list(self._evaluators)

    def list_app_evaluators(self) -> List[AppEvaluator]:
        return list(self._app_evaluators)

    def list_raw_prompts(self) -> List[RawPrompt]:
        return list(self._raw_prompts)


# Single module-level repository instance (acts like in-memory cache)
REPO = JsonRepository.load()
