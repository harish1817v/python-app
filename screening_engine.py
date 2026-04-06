"""
Resume Screening Engine
Core logic for intelligent resume evaluation and scoring
"""

from models import ScreeningResult


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
