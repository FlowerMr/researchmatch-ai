from typing import TypedDict

from langgraph.graph import StateGraph, END

from agent.cv_agent import analyze_cv
from agent.position_agent import analyze_position
from agent.professor_agent import analyze_professor
from agent.recommendation_agent import generate_recommendation

from agent.critic_agent import critique_application
from agent.report_agent import generate_report

from ml.match_engine import calculate_match
from ml.gap_analyzer import analyze_gap
from ml.professor_match import calculate_professor_match
from agent.storage_agent import save_report


# =========================
# STATE
# =========================

class WorkflowState(TypedDict):

    cv_path: str
    job_text: str
    professor_text: str

    cv_data: dict
    position_data: dict
    professor_data: dict

    match_score: float
    professor_match: float

    gap_analysis: dict

    recommendation: str

    critique: str

    report: dict


# =========================
# NODES
# =========================

def cv_node(state):

    state["cv_data"] = analyze_cv(
        state["cv_path"]
    )

    return state

def storage_node(state):

    save_report(
        state["report"]
    )

    return state

def position_node(state):

    state["position_data"] = analyze_position(
        state["job_text"]
    )

    return state


def professor_node(state):

    state["professor_data"] = {
        "Research Interests": [
            "Medical Imaging",
            "Vision Transformers",
            "Explainable AI",
            "Healthcare"
        ],
        "Recent Topics": [],
        "Keywords": []
    }

    return state


def match_node(state):

    state["match_score"] = calculate_match(
        state["cv_data"],
        state["position_data"]
    )

    return state


def professor_match_node(state):

    state["professor_match"] = (
        calculate_professor_match(
            state["cv_data"],
            state["professor_data"]
        )
    )

    return state


def gap_node(state):

    state["gap_analysis"] = analyze_gap(
        state["cv_data"],
        state["position_data"]
    )

    return state


def recommendation_node(state):

    state["recommendation"] = (
        generate_recommendation(
            state["gap_analysis"]
        )
    )

    return state


def critic_node(state):

    state["critique"] = (
        critique_application(
            {
                "match_score":
                    state["match_score"],
                "recommendation":
                    state["recommendation"]
            }
        )
    )

    return state


def report_node(state):

    state["report"] = generate_report(
        state["cv_data"],
        state["position_data"],
        state["professor_data"],
        state["match_score"],
        state["professor_match"],
        state["recommendation"],
        state["critique"]
    )

    return state


# =========================
# GRAPH
# =========================

builder = StateGraph(WorkflowState)

builder.add_node("cv", cv_node)
builder.add_node("position", position_node)
builder.add_node("professor", professor_node)

builder.add_node("match", match_node)
builder.add_node("professor_match", professor_match_node)

builder.add_node("gap", gap_node)

builder.add_node(
    "recommendation",
    recommendation_node
)

builder.add_node(
    "critic",
    critic_node
)

builder.add_node(
    "storage",
    storage_node
)
builder.add_edge(
    "report",
    "storage"
)

builder.add_edge(
    "storage",
    END
)

# =========================
# FLOW
# =========================

builder.set_entry_point("cv")

builder.add_edge(
    "cv",
    "position"
)

builder.add_edge(
    "position",
    "professor"
)

builder.add_edge(
    "professor",
    "match"
)

builder.add_edge(
    "match",
    "professor_match"
)

builder.add_edge(
    "professor_match",
    "gap"
)

builder.add_edge(
    "gap",
    "recommendation"
)

builder.add_edge(
    "recommendation",
    "critic"
)

builder.add_edge(
    "critic",
    "report"
)

builder.add_edge(
    "report",
    END
)

graph = builder.compile()