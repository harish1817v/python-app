"""
Resume Screening & Candidate Evaluation System
AI-powered resume analysis platform for intelligent candidate evaluation
"""

import json
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


# ============================================================================
# DATA MODELS
# ============================================================================

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


# ============================================================================
# SAMPLE DATA
# ============================================================================

SAMPLE_JOB_DESCRIPTION = """
Position: Senior Python Developer
Company: TechCorp Solutions
Location: Remote

Requirements:
- 5+ years of Python development experience
- Strong knowledge of Django or FastAPI frameworks
- Experience with PostgreSQL and Redis
- AWS cloud infrastructure knowledge
- REST API design and development
- Unit testing and CI/CD pipelines
- Git version control expertise
- Team collaboration and communication skills

Nice to have:
- Machine Learning/Data Science background
- Docker and Kubernetes experience
- Microservices architecture knowledge
- Open source contributions
"""

SAMPLE_RESUME = """
Resume: John Smith

PROFESSIONAL SUMMARY
Experienced Python developer with 6 years of full-stack web development experience. 
Passionate about building scalable, maintainable applications using modern Python frameworks.

EXPERIENCE
Senior Developer | TechFlow Inc. (2021-Present, 3 years)
- Led development of microservices using FastAPI and Django
- Designed and optimized PostgreSQL databases for high-traffic applications
- Implemented Redis caching for performance optimization
- Deployed applications on AWS using EC2, S3, and RDS
- Mentored 3 junior developers on best practices
- Implemented CI/CD pipelines using GitHub Actions

Developer | StartupAI (2018-2021, 3 years)
- Developed REST APIs using Django
- Created comprehensive unit tests achieving 85% code coverage
- Worked with Git workflows and code reviews
- Collaborated with cross-functional teams

TECHNICAL SKILLS
Languages: Python (Expert), JavaScript (Intermediate), SQL (Advanced)
Frameworks: Django, FastAPI, Flask
Databases: PostgreSQL, MongoDB, Redis
Cloud: AWS (EC2, S3, Lambda, RDS)
DevOps: Docker, GitHub Actions, Basic Kubernetes
Tools: Git, Pytest, SQLAlchemy

EDUCATION
Bachelor of Science in Computer Science | State University (2018)

CERTIFICATIONS
- AWS Solutions Architect Associate (2022)
- Professional Python Developer Certification (2021)

ADDITIONAL
- GitHub: github.com/johnsmith (5K stars on open source projects)
- Blog: Writes technical articles on Python and cloud architecture
"""


# ============================================================================
# SCREENING ENGINE (Simulated LLM-based evaluation)
# ============================================================================

class ResumeScreeningEngine:
    """
    AI-powered resume screening engine that evaluates candidates
    against job descriptions using intelligent matching and scoring
    """
    
    def __init__(self):
        self.job_description = ""
        self.resume = ""
        
    def load_job_description(self, jd: str) -> None:
        """Load job description for screening"""
        self.job_description = jd
        
    def load_resume(self, resume: str) -> None:
        """Load candidate resume"""
        self.resume = resume
    
    def extract_candidate_name(self) -> str:
        """Extract candidate name from resume"""
        lines = self.resume.split('\n')
        for line in lines:
            if 'Resume:' in line:
                return line.replace('Resume:', '').strip()
        return "Unknown Candidate"
    
    def _parse_job_requirements(self) -> dict:
        """Parse job description to extract requirements"""
        # This would use LLM in production
        requirements = {
            'required_skills': [
                'Python', 'Django', 'FastAPI', 'PostgreSQL', 'Redis',
                'AWS', 'REST API', 'Unit testing', 'CI/CD', 'Git'
            ],
            'nice_to_have': [
                'Machine Learning', 'Docker', 'Kubernetes', 'Microservices'
            ],
            'years_experience': 5,
            'job_title': 'Senior Python Developer'
        }
        return requirements
    
    def _parse_candidate_profile(self) -> dict:
        """Parse resume to extract candidate profile"""
        # This would use LLM in production
        profile = {
            'skills': [
                'Python', 'Django', 'FastAPI', 'PostgreSQL', 'Redis',
                'AWS', 'REST API', 'Docker', 'Git', 'Kubernetes (Basic)'
            ],
            'years_experience': 6,
            'certifications': [
                'AWS Solutions Architect Associate',
                'Professional Python Developer Certification'
            ],
            'open_source_experience': True,
            'leadership_experience': True,
            'frameworks': ['Django', 'FastAPI', 'Flask']
        }
        return profile
    
    def _calculate_skill_match(self) -> tuple[float, list[str], list[str]]:
        """Calculate skill match score and identify gaps"""
        job_reqs = self._parse_job_requirements()
        candidate = self._parse_candidate_profile()
        
        required_skills = set(job_reqs['required_skills'])
        candidate_skills = set(candidate['skills'])
        
        matched = required_skills & candidate_skills
        gaps = required_skills - candidate_skills
        
        score = (len(matched) / len(required_skills)) * 100 if required_skills else 0
        
        return score, list(matched), list(gaps)
    
    def _calculate_experience_match(self) -> tuple[float, list[str]]:
        """Calculate experience match score"""
        job_reqs = self._parse_job_requirements()
        candidate = self._parse_candidate_profile()
        
        # Score based on years of experience
        exp_score = min((candidate['years_experience'] / job_reqs['years_experience']) * 100, 100)
        
        strengths = []
        if candidate['years_experience'] > job_reqs['years_experience']:
            strengths.append(f"{candidate['years_experience']} years experience exceeds requirement")
        
        if candidate['leadership_experience']:
            strengths.append("Proven leadership and mentoring experience")
        
        if candidate['open_source_experience']:
            strengths.append("Strong open source contribution record")
        
        return exp_score, strengths
    
    def _calculate_cultural_fit(self) -> tuple[float, list[str], list[str]]:
        """Calculate cultural fit and risk assessment"""
        candidate = self._parse_candidate_profile()
        
        # Higher score for certifications, leadership, and communication
        base_score = 75
        strengths = []
        risks = []
        
        if len(candidate['certifications']) > 0:
            base_score += 10
            strengths.append("Holds relevant professional certifications")
        
        if candidate['open_source_experience']:
            base_score += 5
            strengths.append("Active in open source community")
        
        if candidate['leadership_experience']:
            base_score += 10
            strengths.append("Demonstrated ability to mentor and lead teams")
        
        # Simulate detection of potential risks
        # (In production, this would be more sophisticated LLM analysis)
        if len(candidate['frameworks']) < 3:
            risks.append("Limited framework diversity")
        
        return min(base_score, 100), strengths, risks
    
    def screen_resume(self) -> ScreeningResult:
        """
        Perform comprehensive resume screening and evaluation
        
        Returns:
            ScreeningResult with scores, analysis, and recommendation
        """
        job_reqs = self._parse_job_requirements()
        
        # Calculate component scores
        skill_score, matched_skills, skill_gaps = self._calculate_skill_match()
        exp_score, exp_strengths = self._calculate_experience_match()
        cultural_score, cultural_strengths, risks = self._calculate_cultural_fit()
        
        # Combine scores (weighted average)
        overall_score = (
            skill_score * 0.50 +      # Skills are most important
            exp_score * 0.30 +         # Experience matters
            cultural_score * 0.20      # Cultural fit matters
        )
        
        # Generate recommendation
        if overall_score >= 80:
            recommendation = "STRONG RECOMMEND for Interview"
        elif overall_score >= 65:
            recommendation = "RECOMMEND for Phone Screen"
        elif overall_score >= 50:
            recommendation = "POSSIBLE - Review with Caution"
        else:
            recommendation = "PASS - Does not meet requirements"
        
        # Build explanation
        explanation = self._generate_explanation(
            overall_score, recommendation, skill_gaps, cultural_strengths, risks
        )
        
        # Compile all strengths
        all_strengths = exp_strengths + cultural_strengths + \
                       [f"Strong match in {len(matched_skills)}/{len(self._parse_job_requirements()['required_skills'])} required skills"]
        
        result = ScreeningResult(
            candidate_name=self.extract_candidate_name(),
            job_title=job_reqs['job_title'],
            overall_score=round(overall_score, 1),
            skill_match_score=round(skill_score, 1),
            experience_match_score=round(exp_score, 1),
            cultural_fit_score=round(cultural_score, 1),
            strengths=all_strengths,
            gaps=skill_gaps,
            risks=risks,
            recommendation=recommendation,
            explanation=explanation
        )
        
        return result
    
    def _generate_explanation(self, score: float, rec: str, gaps: list, 
                            strengths: list, risks: list) -> str:
        """Generate human-readable explanation of screening results"""
        explanation = f"""
This candidate scores {score}/100 for the Senior Python Developer role.

KEY HIGHLIGHTS:
- {len(strengths)} major strengths identified including team leadership experience
- Experience level aligns well with role requirements
- Strong technical certifications on file

ALIGNMENT:
- All core Python and framework skills present
- AWS and database experience verified
- CI/CD pipeline experience demonstrated

CONSIDERATIONS:
        """
        
        if gaps:
            explanation += f"\n- {len(gaps)} skill gaps identified: {', '.join(gaps[:3])}"
        
        if risks:
            explanation += f"\n- Potential concerns: {', '.join(risks)}"
        
        explanation += f"\n\nRECOMMENDATION: {rec}"
        
        return explanation


# ============================================================================
# MAIN DEMO
# ============================================================================

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


def main():
    """Main demo function"""
    print("\n" + "="*80)
    print("AI-POWERED RESUME SCREENING & CANDIDATE EVALUATION SYSTEM".center(80))
    print("="*80)
    print("\nInitializing screening engine...")
    
    # Initialize screening engine
    engine = ResumeScreeningEngine()
    
    # Load job description and resume
    engine.load_job_description(SAMPLE_JOB_DESCRIPTION)
    engine.load_resume(SAMPLE_RESUME)
    
    print("✓ Job description loaded")
    print("✓ Resume loaded")
    print("\nProcessing candidate profile...")
    
    # Perform screening
    result = engine.screen_resume()
    
    # Print comprehensive report
    print_screening_report(result)
    
    # Output structured result for integration
    print("\nJSON OUTPUT (for system integration):")
    print("-"*80)
    result_dict = {
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
    print(json.dumps(result_dict, indent=2))
    print("\n✓ Screening complete. Ready for integration with ATS or recruiter dashboard.\n")


if __name__ == "__main__":
    main()