import pandas as pd
from analyst_engine import run_tool, columns_profile, execute_plan

def demo():
    return pd.DataFrame({"Group": ["A", "B", "A", "B"], "Metric": [10,20,30,40], "Order Date": ["2024-01-01", "2024-01-02", "2024-02-01", "2024-02-02"]})

def test_profile():
    assert columns_profile(demo())["rows"] == 4

def test_grouping():
    r = run_tool(demo(), "grouped_analysis", {"category_col":"Group", "numeric_col":"Metric", "operation":"mean"})
    assert r["values"] == {"B":30, "A":20}

def test_plan():
    p = {"tasks":[{"selected_tool":"data_quality", "parameters":{}}, {"selected_tool":"summary_statistics", "parameters":{}}]}
    assert len(execute_plan(demo(), p)) == 2
