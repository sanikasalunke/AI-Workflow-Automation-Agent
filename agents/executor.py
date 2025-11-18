from core.tool_registry import TOOL_REGISTRY
from typing import List, Dict

class Executor:
    def __init__(self):
        pass

    def execute(self, steps: List[Dict]):
        results = []
        for step in steps:
            tool_name = step.get("tool")
            tool_input = step.get("input")
            tool_fn = TOOL_REGISTRY.get(tool_name)
            if tool_fn is None:
                results.append({"tool": tool_name, "error": "tool not found"})
                continue
            try:
                out = tool_fn(tool_input)
                results.append({"tool": tool_name, "result": out})
            except Exception as e:
                results.append({"tool": tool_name, "error": str(e)})
        return results
