import streamlit as st
from core.llm_loader import load_llm
from agents.planner import Planner
from agents.executor import Executor

st.title("AI Workflow Automation Agent (POC)")

inp = st.text_area("Instruction", value="Summarize README.md and save to out.txt")
if st.button("Run"):
    llm = load_llm()
    planner = Planner(llm=llm)
    executor = Executor()
    with st.spinner("Planning..."):
        plan = planner.plan(inp)
    st.write("Plan:", plan)
    with st.spinner("Executing..."):
        results = executor.execute(plan["steps"])
    st.write("Results:", results)
