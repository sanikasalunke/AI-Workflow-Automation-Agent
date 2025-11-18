"""
Simple CLI entry to run the agent with a text prompt or run a workflow YAML.
"""
import argparse
import json
from core.llm_loader import load_llm
from agents.planner import Planner
from agents.executor import Executor
from core.workflow_engine import run_workflow_from_yaml

def run_ad_hoc(prompt):
    llm = load_llm()
    planner = Planner(llm=llm)
    executor = Executor()
    plan = planner.plan(prompt)
    results = executor.execute(plan["steps"])
    print(json.dumps(results, indent=2, ensure_ascii=False))

def run_yaml(path):
    run_workflow_from_yaml(path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str, help="Ad-hoc natural language instruction")
    parser.add_argument("--workflow", type=str, help="Path to a workflow YAML")
    args = parser.parse_args()

    if args.prompt:
        run_ad_hoc(args.prompt)
    elif args.workflow:
        run_yaml(args.workflow)
    else:
        print("No args provided. Example: python main.py --prompt \"Summarize reports and email me\"")
