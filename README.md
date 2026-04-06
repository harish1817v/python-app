# Resume Screening System - File Structure Guide

## 📁 Project Organization

The application is now organized into separate modules for better clarity and maintainability:

```
python-app/
├── main.py                          # Entry point - Run this!
├── models.py                        # Data structures
├── sample_data.py                   # Sample job/resume data
├── screening_engine.py              # Core screening logic
├── reporting.py                     # Report generation
├── extensions.py                    # Production features (reference)
├── CASE_STUDY.md                    # Detailed case study documentation
├── PROJECT_SUMMARY.md               # Project overview
└── README.md                        # This file
```

---

## 🚀 Quick Start

### Run the Demo
```bash
python main.py
```

---

## 📚 File Descriptions

### 1. **main.py** - Main Entry Point
Entry point that orchestrates the screening process.

**What it does:**
- Initializes the screening engine
- Loads sample data
- Performs screening
- Displays results

**Run it:**
```bash
python main.py
```

---

### 2. **models.py** - Data Models
Defines the core data structure for screening results.

**Contains:**
- `ScreeningResult` - Dataclass with candidate evaluation results

**Use it when:**
- Creating new screening result objects
- Understanding the output structure

**Key fields:**
- `overall_score` - Final evaluation score (0-100)
- `strengths` - List of candidate strengths
- `gaps` - List of missing skills
- `recommendation` - Interview recommendation

---

### 3. **sample_data.py** - Sample Data
Pre-loaded job descriptions and resumes for demo.

**Contains:**
- `SAMPLE_JOB_DESCRIPTION` - Senior Python Developer position
- `SAMPLE_RESUME` - Test candidate resume (John Smith)

**Use it when:**
- Running the demo
- Testing with different JD/resume combinations

**Customize:**
Edit these constants to test different scenarios.

---

### 4. **screening_engine.py** - Core Logic
The heart of the system - performs intelligent resume evaluation.

**Main Class:**
`ResumeScreeningEngine`

**Key Methods:**
- `load_job_description()` - Load job requirements
- `load_resume()` - Load candidate resume
- `screen_resume()` - Execute full screening
- `_parse_job_requirements()` - Extract requirements
- `_parse_candidate_profile()` - Extract candidate info
- `_calculate_skill_match()` - Score technical alignment
- `_calculate_experience_match()` - Score experience relevance
- `_calculate_cultural_fit()` - Score cultural alignment

**How it works:**

```python
from screening_engine import ResumeScreeningEngine
from sample_data import SAMPLE_JOB_DESCRIPTION, SAMPLE_RESUME

engine = ResumeScreeningEngine()
engine.load_job_description(SAMPLE_JOB_DESCRIPTION)
engine.load_resume(SAMPLE_RESUME)
result = engine.screen_resume()  # Returns ScreeningResult
```

---

### 5. **reporting.py** - Report Generation
Formats and displays screening results.

**Functions:**
- `print_screening_report()` - Pretty-printed human-readable report
- `get_json_output()` - Convert result to JSON dict
- `print_json_output()` - Print as formatted JSON

**Output Formats:**

```python
# Option 1: Human-readable formatted report
print_screening_report(result)

# Option 2: Machine-readable JSON (for ATS integration)
json_data = get_json_output(result)
print_json_output(result)
```

---

### 6. **extensions.py** - Production Features
Reference implementation for advanced features.

**Contains Code Patterns For:**
- LLM Integration (GPT-4)
- Vector Database (Semantic Search)
- REST API (FastAPI)
- Fairness & Bias Detection
- ML Model (Hire Success Prediction)
- Analytics Dashboard

**Note:** This is reference documentation, not executed by main.py

---

## 🔄 Module Dependencies

```
main.py
├── screening_engine.py
│   └── models.py
├── sample_data.py
├── reporting.py
    └── models.py
```

---

## 📊 Scoring Algorithm

The system evaluates candidates using **3 weighted components**:

| Component | Weight | What It Measures |
|-----------|--------|------------------|
| **Skill Match** | 50% | Technical skills alignment |
| **Experience** | 30% | Career relevance & progression |
| **Cultural Fit** | 20% | Leadership, certs, community |

**Formula:**
```
Overall Score = (SkillScore × 0.50) + (ExperienceScore × 0.30) + (CulturalScore × 0.20)
```

**Recommendations:**
- **80-100**: STRONG RECOMMEND for Interview
- **65-80**: RECOMMEND for Phone Screen  
- **50-65**: POSSIBLE - Review with Caution
- **<50**: PASS - Does not meet requirements

---

## 🎯 Use Cases

### 1. Run Demo As-Is
```bash
python main.py
```
Uses sample job description and resume.

### 2. Test Different Resume
Edit `sample_data.py` - change `SAMPLE_RESUME`:
```python
# sample_data.py
SAMPLE_RESUME = """
Your new resume here...
"""
```

### 3. Test Different Job Description
Edit `sample_data.py` - change `SAMPLE_JOB_DESCRIPTION`:
```python
# sample_data.py
SAMPLE_JOB_DESCRIPTION = """
Your new job description here...
"""
```

### 4. Use in Your Code
```python
from screening_engine import ResumeScreeningEngine
from models import ScreeningResult

engine = ResumeScreeningEngine()
engine.load_job_description(your_jd)
engine.load_resume(your_resume)
result = engine.screen_resume()

print(f"Score: {result.overall_score}/100")
print(f"Recommendation: {result.recommendation}")
```

---

## 🔧 Customization

### Change Scoring Weights
Edit `screening_engine.py` - `screen_resume()` method:

```python
# Current weights
overall_score = (
    skill_score * 0.50 +      # 50% - Technical skills
    exp_score * 0.30 +        # 30% - Experience
    cultural_score * 0.20     # 20% - Cultural fit
)

# Example: Adjust for leadership role (more cultural fit)
overall_score = (
    skill_score * 0.40 +      # 40%
    exp_score * 0.30 +        # 30%
    cultural_score * 0.30     # 30% - increased
)
```

### Change Recommendation Thresholds
Edit `screening_engine.py` - `screen_resume()` method:

```python
# Current thresholds
if overall_score >= 80:
    recommendation = "STRONG RECOMMEND for Interview"
elif overall_score >= 65:
    recommendation = "RECOMMEND for Phone Screen"
elif overall_score >= 50:
    recommendation = "POSSIBLE - Review with Caution"
else:
    recommendation = "PASS - Does not meet requirements"

# Example: Make it stricter
if overall_score >= 85:  # Raised from 80
    recommendation = "STRONG RECOMMEND for Interview"
```

### Add Custom Parsing Logic
Edit `screening_engine.py` - `_parse_job_requirements()` and `_parse_candidate_profile()`:

In production, these would use LLM APIs for intelligent parsing. Currently they're hardcoded for demo purposes.

---

## 📈 Output Example

```
Candidate: John Smith
Position: Senior Python Developer
Overall Score: 90.0/100

STRONG RECOMMEND for Interview

Scoring Breakdown:
├─ Skill Match:        80/100 ████████░░
├─ Experience Match:   100/100 ██████████
└─ Cultural Fit:       100/100 ██████████

Strengths: (7 identified)
✓ 6 years experience exceeds requirement
✓ Proven leadership and mentoring experience
✓ Strong open source contribution record
...

Skill Gaps: (2 identified)
✗ CI/CD
✗ Unit testing

JSON Output: Ready for ATS integration
```

---

## 🚀 Next Steps

1. **Run demo**: `python main.py`
2. **Understand flow**: Read through main.py → screening_engine.py → models.py
3. **Customize data**: Edit sample_data.py with your scenarios
4. **Adjust weights**: Modify scoring in screening_engine.py
5. **Integrate LLM**: Reference extensions.py for GPT-4 integration
6. **Build API**: Use reporting.py + FastAPI for REST endpoints

---

## 📖 Additional Documentation

- **CASE_STUDY.md** - Complete business case and architecture
- **PROJECT_SUMMARY.md** - Overview and roadmap
- **extensions.py** - Production code patterns

---

## ✨ Key Features

✅ Modular, readable structure  
✅ Separated concerns (logic, data, reporting)  
✅ Easy to customize and extend  
✅ Production-ready architecture  
✅ Comprehensive documentation  

---

**Ready to get started? Run: `python main.py` 🚀**
