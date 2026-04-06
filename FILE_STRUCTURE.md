# File Structure Overview

## 📁 Directory Layout

```
python-app/
│
├── 📄 main.py                      [ENTRY POINT]
│   └─ Orchestrates the demo
│   └─ Imports: screening_engine, sample_data, reporting
│
├── 📄 screening_engine.py         [CORE LOGIC]
│   └─ ResumeScreeningEngine class
│   └─ All scoring algorithms
│   └─ Profile & requirement parsing
│   └─ Imports: models
│
├── 📄 models.py                   [DATA MODELS]
│   └─ ScreeningResult dataclass
│   └─ Type definitions
│
├── 📄 sample_data.py              [DEMO DATA]
│   └─ SAMPLE_JOB_DESCRIPTION
│   └─ SAMPLE_RESUME
│
├── 📄 reporting.py                [OUTPUT FORMATTING]
│   └─ print_screening_report()
│   └─ get_json_output()
│   └─ print_json_output()
│   └─ Imports: models
│
├── 📄 extensions.py               [REFERENCE PATTERNS]
│   └─ Production feature examples
│   └─ LLM integration code
│   └─ API design patterns
│   └─ Not executed by main
│
├── 📄 app.py                      [LEGACY - Original monolithic version]
│   └─ Kept for reference only
│   └─ All functionality now split into modules
│
├── 📄 CASE_STUDY.md              [DOCUMENTATION]
│   └─ Business context
│   └─ Solution architecture
│   └─ Use cases & outcomes
│
├── 📄 PROJECT_SUMMARY.md         [HIGH-LEVEL OVERVIEW]
│   └─ Quick reference
│   └─ Learning outcomes
│   └─ Next steps
│
└── 📄 README.md                  [THIS FILE]
    └─ File structure guide
    └─ How to run & customize
    └─ Usage examples
```

---

## 🔄 Module Dependencies & Flow

```
                    ┌─────────────────┐
                    │    main.py      │ ← START HERE
                    │  (Entry Point)  │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    │                 │
         ┌──────────▼───────────┐    │
         │  screening_engine.py │    │
         │ (Core Logic & Score) │    │
         └─────────┬────────────┘    │
                   │                 │
         ┌─────────▼────────┐        │
         │   models.py      │        │
         │(ScreeningResult) │        │
         └──────────────────┘        │
                                     │
                    ┌────────────────▼──────────┐
                    │    sample_data.py         │
                    │(Job & Resume Sample Data) │
                    └───────────────────────────┘
                                     │
                    ┌────────────────▼──────────┐
                    │    reporting.py           │
                    │  (Format & Display)       │
                    └───────────────────────────┘
```

---

## 📊 Class & Function Map

### models.py
```python
ScreeningResult                    # Dataclass
├── candidate_name: str
├── job_title: str
├── overall_score: float
├── skill_match_score: float
├── experience_match_score: float
├── cultural_fit_score: float
├── strengths: list[str]
├── gaps: list[str]
├── risks: list[str]
├── recommendation: str
└── explanation: str
```

### screening_engine.py
```python
ResumeScreeningEngine             # Main class
├── __init__()
├── load_job_description()
├── load_resume()
├── extract_candidate_name()
├── _parse_job_requirements()
├── _parse_candidate_profile()
├── _calculate_skill_match()
├── _calculate_experience_match()
├── _calculate_cultural_fit()
├── screen_resume()               # Main method
└── _generate_explanation()
```

### reporting.py
```python
Functions
├── print_screening_report()      # Pretty-print report
├── get_json_output()             # Convert to dict
└── print_json_output()           # Print as JSON
```

### sample_data.py
```python
Constants
├── SAMPLE_JOB_DESCRIPTION: str
└── SAMPLE_RESUME: str
```

---

## 🎯 Execution Flow

```
1. main.py starts
   ↓
2. Import modules:
   - ResumeScreeningEngine from screening_engine
   - Sample data from sample_data
   - Reporting functions from reporting
   ↓
3. Create engine instance
   ↓
4. Load job description
   ↓
5. Load resume
   ↓
6. Call screen_resume()
   - Extracts job requirements
   - Extracts candidate profile
   - Calculates skill score
   - Calculates experience score
   - Calculates cultural fit score
   - Combines scores (weighted average)
   - Generates recommendation
   - Creates ScreeningResult
   ↓
7. Display results
   - print_screening_report()    → Human-readable
   - print_json_output()         → Machine-readable
   ↓
8. Done!
```

---

## 🔧 Customization Locations

### To change sample data:
```
sample_data.py
├─ SAMPLE_JOB_DESCRIPTION
└─ SAMPLE_RESUME
```

### To change scoring algorithm:
```
screening_engine.py
├─ _calculate_skill_match()
├─ _calculate_experience_match()
├─ _calculate_cultural_fit()
└─ screen_resume()  [weights & thresholds]
```

### To change output format:
```
reporting.py
├─ print_screening_report()
├─ get_json_output()
└─ print_json_output()
```

### To add features:
```
All module files support extension
See extensions.py for production patterns
```

---

## 📋 Quick Reference

| Need | File | Function/Class |
|------|------|-----------------|
| Run demo | main.py | main() |
| Core logic | screening_engine.py | ResumeScreeningEngine |
| Data model | models.py | ScreeningResult |
| Sample data | sample_data.py | SAMPLE_* constants |
| Display results | reporting.py | print_* functions |
| Production code | extensions.py | Various classes |
| Business context | CASE_STUDY.md | Documentation |
| Project overview | PROJECT_SUMMARY.md | Documentation |
| File guide | README.md | This guide |

---

## ✨ Benefits of Modular Structure

✅ **Clarity**: Each file has one clear purpose  
✅ **Maintainability**: Easy to locate and modify features  
✅ **Testability**: Can unit test individual modules  
✅ **Reusability**: Import just what you need  
✅ **Scalability**: Add new modules without touching existing code  
✅ **Collaboration**: Team members can work on different modules  

---

## 🚀 Getting Started

1. **Understand structure**: Read this file
2. **Run demo**: `python main.py`
3. **Read code**: Start with main.py, then screening_engine.py
4. **Customize**: Edit sample_data.py for your scenarios
5. **Extend**: Reference extensions.py for advanced features

---

**Everything is organized and ready. Start with `python main.py`!** 🎉
