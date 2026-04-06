"""
Report Generation Module
Formats and displays screening results in human-readable and machine formats
"""

import json
from datetime import datetime
from models import ScreeningResult


def print_screening_report(result: ScreeningResult) -> None:
    """Pretty print the screening results"""
    print("\n" + "="*80)
    print("RESUME SCREENING REPORT".center(80))
    print("="*80)
    
    print(f"\nCandidate: {result.candidate_name}")
    print(f"Position: {result.job_title}")
    print(f"Screening Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    print("\n" + "-"*80)
    print("SCORING BREAKDOWN")
    print("-"*80)
    print(f"Overall Score:           {result.overall_score}/100  {'█' * int(result.overall_score/5)}")
    print(f"Skill Match:             {result.skill_match_score}/100  {'█' * int(result.skill_match_score/5)}")
    print(f"Experience Match:        {result.experience_match_score}/100  {'█' * int(result.experience_match_score/5)}")
    print(f"Cultural Fit:            {result.cultural_fit_score}/100  {'█' * int(result.cultural_fit_score/5)}")
    
    print("\n" + "-"*80)
    print("STRENGTHS")
    print("-"*80)
    for i, strength in enumerate(result.strengths, 1):
        print(f"  {i}. {strength}")
    
    if result.gaps:
        print("\n" + "-"*80)
        print("SKILL GAPS")
        print("-"*80)
        for i, gap in enumerate(result.gaps, 1):
            print(f"  {i}. {gap}")
    
    if result.risks:
        print("\n" + "-"*80)
        print("RISK INDICATORS")
        print("-"*80)
        for i, risk in enumerate(result.risks, 1):
            print(f"  ⚠ {risk}")
    
    print("\n" + "-"*80)
    print("RECOMMENDATION")
    print("-"*80)
    print(f"  → {result.recommendation}")
    
    print(f"\nDETAILED ANALYSIS:")
    print(result.explanation)
    
    print("\n" + "="*80)


def get_json_output(result: ScreeningResult) -> dict:
    """Convert screening result to JSON-serializable dictionary"""
    return {
        'candidate_name': result.candidate_name,
        'job_title': result.job_title,
        'overall_score': result.overall_score,
        'scores': {
            'skill_match': result.skill_match_score,
            'experience_match': result.experience_match_score,
            'cultural_fit': result.cultural_fit_score
        },
        'strengths': result.strengths,
        'gaps': result.gaps,
        'risks': result.risks,
        'recommendation': result.recommendation
    }


def print_json_output(result: ScreeningResult) -> None:
    """Print screening result as formatted JSON"""
    result_dict = get_json_output(result)
    print("\nJSON OUTPUT (for system integration):")
    print("-"*80)
    print(json.dumps(result_dict, indent=2))
