from agent.position_agent import analyze_position


job_text = """
PhD Position in Explainable AI and Medical Imaging

Requirements:

- Python
- Deep Learning
- PyTorch
- Computer Vision
- Medical Image Analysis

Preferred:

- Publications
- Explainable AI
- TensorFlow

Research Area:

Explainable Deep Learning for Healthcare
"""

result = analyze_position(job_text)

print(result)