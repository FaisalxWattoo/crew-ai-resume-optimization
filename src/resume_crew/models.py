from typing import List, Dict, Optional
from pydantic import BaseModel, Field, confloat

class SkillScore(BaseModel):
    skill_name: str = Field(..., description="Name of the skill being scored")
    required: bool = Field(..., description="Whether this skill is required or nice-to-have")
    match_level: float = Field(default=0.5, ge=0, le=1, description="How well the candidate's experience matches (0-1)")
    years_experience: Optional[float] = Field(default=None, description="Years of experience with this skill")
    context_score: float = Field(default=0.5, ge=0, le=1, description="How relevant the skill usage context is to the job requirements")

class JobMatchScore(BaseModel):
    overall_match: float = Field(default=50, ge=0, le=100, description="Overall match percentage (0-100)")
    technical_skills_match: float = Field(default=50, ge=0, le=100, description="Technical skills match percentage")
    soft_skills_match: float = Field(default=50, ge=0, le=100, description="Soft skills match percentage")
    experience_match: float = Field(default=50, ge=0, le=100, description="Experience level match percentage")
    education_match: float = Field(default=50, ge=0, le=100, description="Education requirements match percentage")
    industry_match: float = Field(default=50, ge=0, le=100, description="Industry experience match percentage")
    skill_details: List[SkillScore] = Field(default_factory=list, description="Detailed scoring for each skill")
    strengths: List[str] = Field(default_factory=list, description="List of areas where candidate exceeds requirements")
    gaps: List[str] = Field(default_factory=list, description="List of areas needing improvement")
    scoring_factors: Dict[str, float] = Field(default_factory=lambda: {"technical_skills": 0.35, "soft_skills": 0.20, "experience": 0.25, "education": 0.10, "industry": 0.10}, description="Weights used for different scoring components")

class JobRequirements(BaseModel):
    technical_skills: List[str] = Field(default_factory=list, description="List of required technical skills")
    soft_skills: List[str] = Field(default_factory=list, description="List of required soft skills")
    experience_requirements: List[str] = Field(default_factory=list, description="List of experience requirements")
    key_responsibilities: List[str] = Field(default_factory=list, description="List of key job responsibilities")
    education_requirements: List[str] = Field(default_factory=list, description="List of education requirements")
    nice_to_have: List[str] = Field(default_factory=list, description="List of preferred but not required skills")
    job_title: str = Field(default="", description="Official job title")
    department: Optional[str] = Field(default=None, description="Department or team within the company")
    reporting_structure: Optional[str] = Field(default=None, description="Who this role reports to and any direct reports")
    job_level: Optional[str] = Field(default=None, description="Level of the position (e.g., Entry, Senior, Lead)")
    location_requirements: Dict[str, str] = Field(default_factory=dict, description="Location details including remote/hybrid options")
    work_schedule: Optional[str] = Field(default=None, description="Expected work hours and schedule flexibility")
    travel_requirements: Optional[str] = Field(default=None, description="Expected travel frequency and scope")
    compensation: Dict[str, str] = Field(default_factory=dict, description="Salary range and compensation details if provided")
    benefits: List[str] = Field(default_factory=list, description="List of benefits and perks")
    tools_and_technologies: List[str] = Field(default_factory=list, description="Specific tools, software, or technologies used")
    industry_knowledge: List[str] = Field(default_factory=list, description="Required industry-specific knowledge")
    certifications_required: List[str] = Field(default_factory=list, description="Required certifications or licenses")
    security_clearance: Optional[str] = Field(default=None, description="Required security clearance level if any")
    team_size: Optional[str] = Field(default=None, description="Size of the immediate team")
    key_projects: List[str] = Field(default_factory=list, description="Major projects or initiatives mentioned")
    cross_functional_interactions: List[str] = Field(default_factory=list, description="Teams or departments this role interacts with")
    career_growth: List[str] = Field(default_factory=list, description="Career development and growth opportunities")
    training_provided: List[str] = Field(default_factory=list, description="Training or development programs offered")
    diversity_inclusion: Optional[str] = Field(default=None, description="D&I statements or requirements")
    company_values: List[str] = Field(default_factory=list, description="Company values mentioned in the job posting")
    job_url: str = Field(default="", description="URL of the job posting")
    posting_date: Optional[str] = Field(default=None, description="When the job was posted")
    application_deadline: Optional[str] = Field(default=None, description="Application deadline if specified")
    special_instructions: List[str] = Field(default_factory=list, description="Any special application instructions or requirements")
    match_score: JobMatchScore = Field(default_factory=JobMatchScore, description="Detailed scoring of how well the candidate matches the job requirements")
    score_explanation: List[str] = Field(default_factory=list, description="Detailed explanation of how scores were calculated")

# Additional classes such as ResumeOptimization and CompanyResearch can also be defined following a similar pattern.


# from typing import List, Dict, Optional
# from pydantic import BaseModel, Field, confloat

# class SkillScore(BaseModel):
#     skill_name: str = Field(description="Name of the skill being scored")
#     required: bool = Field(description="Whether this skill is required or nice-to-have")
#     match_level: confloat(ge=0, le=1) = Field(description="How well the candidate's experience matches (0-1)")
#     years_experience: Optional[float] = Field(description="Years of experience with this skill", default=None)
#     context_score: confloat(ge=0, le=1) = Field(
#         description="How relevant the skill usage context is to the job requirements",
#         default=0.5
#     )

# class JobMatchScore(BaseModel):
#     overall_match: confloat(ge=0, le=100) = Field(
#         description="Overall match percentage (0-100)"
#     )
#     technical_skills_match: confloat(ge=0, le=100) = Field(
#         description="Technical skills match percentage"
#     )
#     soft_skills_match: confloat(ge=0, le=100) = Field(
#         description="Soft skills match percentage"
#     )
#     experience_match: confloat(ge=0, le=100) = Field(
#         description="Experience level match percentage"
#     )
#     education_match: confloat(ge=0, le=100) = Field(
#         description="Education requirements match percentage"
#     )
#     industry_match: confloat(ge=0, le=100) = Field(
#         description="Industry experience match percentage"
#     )
#     skill_details: List[SkillScore] = Field(
#         description="Detailed scoring for each skill",
#         default_factory=list
#     )
#     strengths: List[str] = Field(
#         description="List of areas where candidate exceeds requirements",
#         default_factory=list
#     )
#     gaps: List[str] = Field(
#         description="List of areas needing improvement",
#         default_factory=list
#     )
#     scoring_factors: Dict[str, float] = Field(
#         description="Weights used for different scoring components",
#         default_factory=lambda: {
#             "technical_skills": 0.35,
#             "soft_skills": 0.20,
#             "experience": 0.25,
#             "education": 0.10,
#             "industry": 0.10
#         }
#     )

# class JobRequirements(BaseModel):
#     technical_skills: List[str] = Field(
#         description="List of required technical skills",
#         default_factory=list
#     )
#     soft_skills: List[str] = Field(
#         description="List of required soft skills",
#         default_factory=list
#     )
#     experience_requirements: List[str] = Field(
#         description="List of experience requirements",
#         default_factory=list
#     )
#     key_responsibilities: List[str] = Field(
#         description="List of key job responsibilities",
#         default_factory=list
#     )
#     education_requirements: List[str] = Field(
#         description="List of education requirements",
#         default_factory=list
#     )
#     nice_to_have: List[str] = Field(
#         description="List of preferred but not required skills",
#         default_factory=list
#     )
#     job_title: str = Field(
#         description="Official job title",
#         default=""
#     )
#     department: Optional[str] = Field(
#         description="Department or team within the company",
#         default=None
#     )
#     reporting_structure: Optional[str] = Field(
#         description="Who this role reports to and any direct reports",
#         default=None
#     )
#     job_level: Optional[str] = Field(
#         description="Level of the position (e.g., Entry, Senior, Lead)",
#         default=None
#     )
#     location_requirements: Dict[str, str] = Field(
#         description="Location details including remote/hybrid options",
#         default_factory=dict
#     )
#     work_schedule: Optional[str] = Field(
#         description="Expected work hours and schedule flexibility",
#         default=None
#     )
#     travel_requirements: Optional[str] = Field(
#         description="Expected travel frequency and scope",
#         default=None
#     )
#     compensation: Dict[str, str] = Field(
#         description="Salary range and compensation details if provided",
#         default_factory=dict
#     )
#     benefits: List[str] = Field(
#         description="List of benefits and perks",
#         default_factory=list
#     )
#     tools_and_technologies: List[str] = Field(
#         description="Specific tools, software, or technologies used",
#         default_factory=list
#     )
#     industry_knowledge: List[str] = Field(
#         description="Required industry-specific knowledge",
#         default_factory=list
#     )
#     certifications_required: List[str] = Field(
#         description="Required certifications or licenses",
#         default_factory=list
#     )
#     security_clearance: Optional[str] = Field(
#         description="Required security clearance level if any",
#         default=None
#     )
#     team_size: Optional[str] = Field(
#         description="Size of the immediate team",
#         default=None
#     )
#     key_projects: List[str] = Field(
#         description="Major projects or initiatives mentioned",
#         default_factory=list
#     )
#     cross_functional_interactions: List[str] = Field(
#         description="Teams or departments this role interacts with",
#         default_factory=list
#     )
#     career_growth: List[str] = Field(
#         description="Career development and growth opportunities",
#         default_factory=list
#     )
#     training_provided: List[str] = Field(
#         description="Training or development programs offered",
#         default_factory=list
#     )
#     diversity_inclusion: Optional[str] = Field(
#         description="D&I statements or requirements",
#         default=None
#     )
#     company_values: List[str] = Field(
#         description="Company values mentioned in the job posting",
#         default_factory=list
#     )
#     job_url: str = Field(
#         description="URL of the job posting",
#         default=""
#     )
#     posting_date: Optional[str] = Field(
#         description="When the job was posted",
#         default=None
#     )
#     application_deadline: Optional[str] = Field(
#         description="Application deadline if specified",
#         default=None
#     )
#     special_instructions: List[str] = Field(
#         description="Any special application instructions or requirements",
#         default_factory=list
#     )
#     match_score: JobMatchScore = Field(
#         description="Detailed scoring of how well the candidate matches the job requirements",
#         default_factory=JobMatchScore
#     )
#     score_explanation: List[str] = Field(
#         description="Detailed explanation of how scores were calculated",
#         default_factory=list
#     )

class ResumeOptimization(BaseModel):
    content_suggestions: List[Dict[str, str]] = Field(
        description="List of content optimization suggestions with 'before' and 'after' examples"
    )
    skills_to_highlight: List[str] = Field(
        description="List of skills that should be emphasized based on job requirements"
    )
    achievements_to_add: List[str] = Field(
        description="List of achievements that should be added or modified"
    )
    keywords_for_ats: List[str] = Field(
        description="List of important keywords for ATS optimization"
    )
    formatting_suggestions: List[str] = Field(
        description="List of formatting improvements"
    )

class CompanyResearch(BaseModel):
    recent_developments: List[str] = Field(
        description="List of recent company news and developments"
    )
    culture_and_values: List[str] = Field(
        description="Key points about company culture and values"
    )
    market_position: Dict[str, List[str]] = Field(
        description="Information about market position, including competitors and industry standing"
    )
    growth_trajectory: List[str] = Field(
        description="Information about company's growth and future plans"
    )
    interview_questions: List[str] = Field(
        description="Strategic questions to ask during the interview"
    )
