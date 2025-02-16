import streamlit as st
import os
import json
from PyPDF2 import PdfReader
from resume_crew.crew import ResumeCrew  # Importing your existing CrewAI logic

def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

def run_optimization(job_url, company_name, resume_text):
    inputs = {
        'job_url': job_url,
        'company_name': company_name,
        'resume_text': resume_text
    }
    
    ResumeCrew().crew().kickoff(inputs=inputs)
    
    return {
        "job_analysis": json.load(open("output/job_analysis.json")) if os.path.exists("output/job_analysis.json") else {},
        "resume_optimization": json.load(open("output/resume_optimization.json")) if os.path.exists("output/resume_optimization.json") else {},
        "company_research": json.load(open("output/company_research.json")) if os.path.exists("output/company_research.json") else {},
        "optimized_resume": open("output/optimized_resume.md").read() if os.path.exists("output/optimized_resume.md") else "No optimized resume generated.",
        "final_report": open("output/final_report.md").read() if os.path.exists("output/final_report.md") else "No final report generated."
    }

# Streamlit UI
st.set_page_config(page_title="Resume Optimizer", layout="wide")
st.title("📄 Resume Optimization with AI")

# File Upload & Input Fields
uploaded_file = st.file_uploader("📂 Upload Your Resume (PDF)", type=["pdf"])
job_url = st.text_input("🔗 Job Posting URL")
company_name = st.text_input("🏢 Company Name")

if uploaded_file and job_url and company_name:
    st.success("✅ All inputs received! Click below to optimize your resume.")
    
    if st.button("🚀 Optimize Resume"):
        resume_text = extract_text_from_pdf(uploaded_file)
        st.info("🔄 Running Resume Optimization... This may take a few moments.")
        
        try:
            results = run_optimization(job_url, company_name, resume_text)
        except Exception as e:
            st.error(f"❌ Error running optimization: {str(e)}")
            st.stop()
        
        # Display Results
        st.subheader("📊 Job Analysis")
        st.json(results.get("job_analysis", {}))
        
        st.subheader("📝 Resume Optimization Suggestions")
        st.json(results.get("resume_optimization", {}))
        
        st.subheader("🏢 Company Insights")
        st.json(results.get("company_research", {}))
        
        st.subheader("📌 Optimized Resume")
        optimized_resume = results.get("optimized_resume", "No optimized resume generated.")
        st.text_area("", optimized_resume, height=300)
        
        st.download_button(
            label="📥 Download Optimized Resume",
            data=optimized_resume,
            file_name="optimized_resume.md",
            mime="text/markdown"
        )
        
        st.subheader("📑 Final Report")
        final_report = results.get("final_report", "No final report generated.")
        st.text_area("", final_report, height=300)
        
        st.download_button(
            label="📥 Download Final Report",
            data=final_report,
            file_name="final_report.md",
            mime="text/markdown"
        )
