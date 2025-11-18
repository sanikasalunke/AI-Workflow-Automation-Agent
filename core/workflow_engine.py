import yaml
from agents.executor import Executor
from agents.planner import Planner
from core.llm_loader import load_llm

def run_workflow_from_yaml(path: str):
    with open(path, "r", encoding="utf-8") as f:
        wf = yaml.safe_load(f)
    steps = wf.get("steps", [])
    # Resolve templates (naive) - small helper for substituting summary placeholders
    # For POC we pass steps directly to Executor
    executor = Executor()
    results = executor.execute(steps)
    print("Workflow results:")
    for r in results:
        print(r)
    return results

def run_ad_hoc_with_planner(prompt: str):
    llm = load_llm()
    planner = Planner(llm=llm)
    plan = planner.plan(prompt)
    executor = Executor()
    return executor.execute(plan["steps"])
