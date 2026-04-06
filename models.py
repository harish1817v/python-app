"""
Data Models for Resume Screening System
Defines the core data structures used throughout the application
"""

from dataclasses import dataclass


@dataclass
class ScreeningResult:
    """Result of resume screening against a job description"""
    candidate_name: str
    job_title: str
    overall_score: float  # 0-100
    skill_match_score: float
    experience_match_score: float
    cultural_fit_score: float
    strengths: list[str]
    gaps: list[str]
    risks: list[str]
    recommendation: str
    explanation: str
