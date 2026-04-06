"""
Resume Screening & Candidate Evaluation System
Main entry point for the demo application
"""

from screening_engine import ResumeScreeningEngine
from sample_data import SAMPLE_JOB_DESCRIPTION, SAMPLE_RESUME
from reporting import print_screening_report, print_json_output


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
    print_json_output(result)
    
    print("\n✓ Screening complete. Ready for integration with ATS or recruiter dashboard.\n")


if __name__ == "__main__":
    main()
