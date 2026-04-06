#!/usr/bin/env python3
"""
Quick Start & File Overview
Visual guide to the modular structure
"""

print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║          AI-POWERED RESUME SCREENING SYSTEM - MODULAR STRUCTURE             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝

📦 PROJECT FILES
═════════════════════════════════════════════════════════════════════════════

🚀 ENTRY POINT
  main.py                    → Run this: python main.py

🧠 CORE LOGIC
  screening_engine.py        → ResumeScreeningEngine class
  models.py                  → ScreeningResult dataclass

📊 DATA & OUTPUT
  sample_data.py            → Job descriptions & resumes
  reporting.py              → Format & display results

📚 DOCUMENTATION & EXAMPLES
  README.md                 → Full setup & customization guide
  FILE_STRUCTURE.md         → This file structure explained
  CASE_STUDY.md             → Business context & architecture
  PROJECT_SUMMARY.md        → Overview & roadmap
  extensions.py             → Production code patterns

🔨 LEGACY (Monolithic Version)
  app.py                    → Original (keep for reference)

═════════════════════════════════════════════════════════════════════════════

🎯 QUICK COMMANDS
═════════════════════════════════════════════════════════════════════════════

1. Run the demo:
   $ python main.py

2. View file structure:
   $ cat FILE_STRUCTURE.md

3. Read the full case study:
   $ cat CASE_STUDY.md

4. Check the project summary:
   $ cat PROJECT_SUMMARY.md

5. List all Python files:
   $ ls -la *.py

═════════════════════════════════════════════════════════════════════════════

📖 MODULE DESCRIPTIONS
═════════════════════════════════════════════════════════════════════════════

models.py (528 bytes)
  • ScreeningResult dataclass
  • Defines output structure
  • Import: from models import ScreeningResult

sample_data.py (2.2 KB)
  • SAMPLE_JOB_DESCRIPTION
  • SAMPLE_RESUME
  • Easy to customize for testing

screening_engine.py (8.0 KB)  
  • ResumeScreeningEngine class
  • Resume parsing
  • Job requirement extraction
  • Scoring algorithms:
    - Skill match calculation
    - Experience scoring
    - Cultural fit assessment
  • Recommendation generation

reporting.py (2.7 KB)
  • print_screening_report() - Pretty-printed output
  • get_json_output() - JSON serialization
  • print_json_output() - JSON display

main.py (1.2 KB)
  • Entry point
  • Orchestrates the workflow
  • Loads data, runs screening, displays results

═════════════════════════════════════════════════════════════════════════════

🔄 EXECUTION FLOW
═════════════════════════════════════════════════════════════════════════════

$ python main.py
    ↓
[main.py] Initialize & load modules
    ↓
[screening_engine.py] Create ResumeScreeningEngine instance
    ↓
[sample_data.py] Load sample job description & resume
    ↓
[screening_engine.py] Execute screen_resume()
    • Parse job requirements
    • Extract candidate profile
    • Calculate scores
    • Generate recommendation
    ↓
[models.py] Return ScreeningResult
    ↓
[reporting.py] Format and display results
    • Human-readable report
    • JSON output for integration
    ↓
Done! ✓

═════════════════════════════════════════════════════════════════════════════

💡 CUSTOMIZATION QUICK TIPS
═════════════════════════════════════════════════════════════════════════════

Change Resume/Job Description:
  → Edit sample_data.py
  → Modify SAMPLE_RESUME or SAMPLE_JOB_DESCRIPTION

Adjust Scoring Weights:
  → Edit screening_engine.py
  → Find screen_resume() method
  → Change: skill_score * 0.XX (adjust percentages)

Change Recommendation Thresholds:
  → Edit screening_engine.py
  → Find recommendation logic (if overall_score >= 80...)
  → Adjust threshold numbers

Add Custom Output Format:
  → Edit reporting.py
  → Add new function
  → Call from main.py

═════════════════════════════════════════════════════════════════════════════

📊 SCORING BREAKDOWN
═════════════════════════════════════════════════════════════════════════════

Overall Score Formula:
  (Skill Match × 0.50) + (Experience × 0.30) + (Cultural Fit × 0.20)

Recommendations:
  ✓ 80-100: STRONG RECOMMEND for Interview
  ➜ 65-80:  RECOMMEND for Phone Screen  
  ⚠ 50-65:  POSSIBLE - Review with Caution
  ✗ <50:    PASS - Does not meet requirements

═════════════════════════════════════════════════════════════════════════════

🚀 GETTING STARTED STEPS
═════════════════════════════════════════════════════════════════════════════

1. Run the demo first (2 minutes):
   $ python main.py

2. Review the structure (5 minutes):
   $ cat FILE_STRUCTURE.md

3. Understand the flow (10 minutes):
   Read: main.py → screening_engine.py → models.py

4. Customize test data (5 minutes):
   Edit: sample_data.py

5. Adjust scoring (10 minutes):
   Edit: screening_engine.py scoring methods

6. Build your own version (30+ minutes):
   Import modules and use in your code

═════════════════════════════════════════════════════════════════════════════

📚 DOCUMENTATION HIERARCHY
═════════════════════════════════════════════════════════════════════════════

FILE_STRUCTURE.md        ← Start here [This file]
        ↓
README.md                ← Setup & usage guide
        ↓
main.py                  ← Entry point to code
        ↓
screening_engine.py      ← Core algorithm
        ↓
CASE_STUDY.md            ← Why & what
        ↓
extensions.py            ← Advanced features
        ↓
PROJECT_SUMMARY.md       ← Big picture

═════════════════════════════════════════════════════════════════════════════

✨ KEY ADVANTAGES OF MODULAR STRUCTURE
═════════════════════════════════════════════════════════════════════════════

✓ Easy to understand - each file has one job
✓ Easy to modify - locate what you need quickly
✓ Easy to test - test modules independently
✓ Easy to extend - add without breaking existing code
✓ Easy to share - other developers understand structure
✓ Easy to maintain - clear dependencies between files
✓ Production-ready - proper separation of concerns

═════════════════════════════════════════════════════════════════════════════

🎓 LEARNING RESOURCES
═════════════════════════════════════════════════════════════════════════════

Business Understanding:
  → Read CASE_STUDY.md (15 minutes)
  → Understand the problem being solved

Architecture Understanding:
  → Read FILE_STRUCTURE.md (10 minutes)
  → Understand how pieces fit together

Code Understanding:
  → Run main.py (2 minutes)
  → Read main.py, then screening_engine.py (20 minutes)

Hands-On Learning:
  → Modify sample_data.py (10 minutes)
  → Try different scenarios
  
Advanced Learning:
  → Read extensions.py (20 minutes)
  → Reference code for production features

═════════════════════════════════════════════════════════════════════════════

🎉 YOU'RE ALL SET!
═════════════════════════════════════════════════════════════════════════════

Ready to run the demo?

    $ python main.py

Enjoy exploring the Resume Screening System! 🚀
""")
