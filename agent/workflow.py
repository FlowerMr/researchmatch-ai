from typing import TypedDict

from langgraph.graph import StateGraph

from agent.cv_agent import analyze_cv
from agent.position_agent import analyze_position

from ml.match_engine import calculate_match
from ml.skill_gap_analyzer import analyze_skill_gap

from agent.recommendation_agent import generate_recommendation


class AgentState(TypedDict):

    cv_path: str

    job_text: str

    cv_data: dict

    position_data: dict

    match_score: float

    gap_analysis: dict

    recommendation: str
    
def cv_node(state):

    state["cv_data"] = analyze_cv(
        state["cv_path"]
    )

    return state
def position_node(state):

    state["position_data"] = analyze_position(
        state["job_text"]
    )

    return state
def match_node(state):

    score = calculate_match(
        state["cv_data"],
        state["position_data"]
    )

    state["match_score"] = score

    return state
def gap_node(state):

    state["gap_analysis"] = analyze_skill_gap(
        state["cv_data"],
        state["position_data"],
        state["match_score"]
    )

    return state
def recommendation_node(state):

    state["recommendation"] = (
        generate_recommendation(
            state["gap_analysis"]
        )
    )

    return state

graph = StateGraph(AgentState)

graph.add_node("cv", cv_node)

graph.add_node(
    "position",
    position_node
)

graph.add_node(
    "match",
    match_node
)

graph.add_node(
    "gap",
    gap_node
)

graph.add_node(
    "recommendation",
    recommendation_node
)
graph.add_edge("cv", "position")

graph.add_edge("position", "match")

graph.add_edge("match", "gap")

graph.add_edge(
    "gap",
    "recommendation"
)

from langgraph.graph import START, END

graph.add_edge(START, "cv")

graph.add_edge(
    "recommendation",
    END
)

app = graph.compile()