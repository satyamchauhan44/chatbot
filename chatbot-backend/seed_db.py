import os
from main import SessionLocal, FAQ, engine, Base

# Re-create tables
Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Clear existing entries to prevent duplicates when re-running
db.query(FAQ).delete()

admission_faqs = [

    # ============================================================
    # --- AKTU / UPTAC COUNSELLING & RANKS ---
    # ============================================================

    FAQ(
        keyword="rank",
        question="What JEE Main/AKTU rank is needed for CSE at Galgotias?",
        answer="For B.Tech CSE at GCET through UPTAC counselling, the required rank varies every year depending on category, quota and counselling round. CSE is generally one of the most competitive branches at the college."
    ),

    FAQ(
        keyword="counselling",
        question="How does UPTAC counselling work for Galgotias College?",
        answer="Admissions are conducted through UPTAC counselling based on JEE Main scores. Candidates participate in registration, choice filling, seat allotment, seat acceptance and reporting. Candidates should select Galgotias College and their preferred branches during choice filling."
    ),

    FAQ(
        keyword="cutoff",
        question="What are the cutoffs for ECE, ME, and Electrical Engineering?",
        answer="Core branches such as ECE, Electrical and Mechanical Engineering generally have more relaxed closing ranks than CSE and its specializations. The exact cutoff changes every year according to category, quota and counselling round."
    ),

    FAQ(
        keyword="choice_filling",
        question="Which Galgotias College branches should I put first during UPTAC choice filling?",
        answer="Students should arrange choices according to their preferred branch and career goals. A typical preference may start with CSE, CSE AI/ML, CSE Data Science, IT, ECE, Electrical/EEE and Mechanical, but students should choose according to their own interests."
    ),

    FAQ(
        keyword="cutoff_trend",
        question="How can I compare Galgotias College cutoffs for the last two years?",
        answer="Compare the opening and closing ranks for the same branch, category, quota and counselling round. A fair comparison requires keeping these factors the same because cutoffs can change significantly between categories and rounds."
    ),

    FAQ(
        keyword="rank_prediction",
        question="I have a JEE Main rank of 2 lakh. Which branches can I get at Galgotias College?",
        answer="A JEE Main rank around 2 lakh may make several GCET branches possible depending on category, quota and counselling round. CSE and its specializations are generally more competitive, while ECE, Electrical and Mechanical may have more relaxed closing ranks."
    ),

    # ============================================================
    # --- BRANCH-WISE CUTOFFS: 2024 & 2025 ---
    # ============================================================

    FAQ(
        keyword="cse_cutoff",
        question="What was the CSE cutoff at Galgotias College in 2024 and 2025?",
        answer="For General/Open category admissions through UPTAC, the CSE closing rank was approximately 1.39 lakh in the 2024 last round for the relevant All India category. The 2025 cutoff varied by round, category and quota. Students should check the official UPTAC opening and closing rank data for the exact 2025 cutoff."
    ),

    FAQ(
        keyword="aiml_cutoff",
        question="What was the CSE AI/ML cutoff at Galgotias College in 2024 and 2025?",
        answer="For CSE Artificial Intelligence and Machine Learning, the 2024 General All India last-round closing rank was approximately 1.82 lakh. The 2025 cutoff varied according to counselling round, category and quota."
    ),

    FAQ(
        keyword="data_science_cutoff",
        question="What was the CSE Data Science cutoff at Galgotias College in 2024 and 2025?",
        answer="For CSE Data Science, the 2024 General All India last-round closing rank was approximately 2.25 lakh. The 2025 cutoff depended on the counselling round, category and quota."
    ),

    FAQ(
        keyword="it_cutoff",
        question="What was the Information Technology cutoff at Galgotias College in 2024 and 2025?",
        answer="For Information Technology, the 2024 General All India last-round closing rank was approximately 2.31 lakh. The 2025 cutoff varied depending on the counselling round, category and quota."
    ),

    FAQ(
        keyword="ece_cutoff",
        question="What was the ECE cutoff at Galgotias College in 2024 and 2025?",
        answer="For Electronics and Communication Engineering, the 2024 General All India last-round closing rank was approximately 3.63 lakh. The 2025 cutoff varied according to category, quota and counselling round."
    ),

    FAQ(
        keyword="eee_cutoff",
        question="What was the Electrical and Electronics Engineering cutoff at Galgotias College in 2024 and 2025?",
        answer="For Electrical and Electronics Engineering, the 2024 cutoff was considerably more relaxed than CSE and IT. The exact 2025 cutoff depended on category, quota and counselling round."
    ),

    FAQ(
        keyword="electrical_cutoff",
        question="What was the Electrical Engineering cutoff at Galgotias College in 2024 and 2025?",
        answer="Electrical Engineering generally has a more relaxed cutoff than CSE, AI/ML, Data Science, IT and ECE. The exact 2024 and 2025 closing ranks varied by category, quota and counselling round."
    ),

    FAQ(
        keyword="mechanical_cutoff",
        question="What was the Mechanical Engineering cutoff at Galgotias College in 2024 and 2025?",
        answer="For Mechanical Engineering, the 2024 General All India last-round closing rank was approximately 11.88 lakh. The 2025 cutoff varied according to category, quota and counselling round."
    ),

    FAQ(
        keyword="civil_cutoff",
        question="What was the Civil Engineering cutoff at Galgotias College in 2024 and 2025?",
        answer="Civil Engineering generally has a more relaxed cutoff compared with CSE and other popular branches. The exact 2024 and 2025 closing ranks varied depending on category, quota and counselling round."
    ),

    FAQ(
        keyword="branch_cutoff",
        question="Which branch has the highest cutoff at Galgotias College?",
        answer="CSE and popular computer science specializations generally have the highest competition. IT and ECE are also competitive, while Electrical, Mechanical and Civil generally have more relaxed closing ranks."
    ),

    # ============================================================
    # --- DIRECT & MANAGEMENT QUOTA ADMISSION ---
    # ============================================================

    FAQ(
        keyword="direct",
        question="Can I get direct admission without JEE Main or counselling?",
        answer="Admission rules for seats outside regular UPTAC counselling depend on the current institutional and regulatory rules. Students should verify the latest admission notification and eligibility requirements directly with the college before applying."
    ),

    FAQ(
        keyword="management",
        question="What is the process for management quota seats?",
        answer="Students interested in admission through institutional or management quota should contact the college admission office and verify the current eligibility, seat availability, fees and admission procedure."
    ),

    # ============================================================
    # --- COURSES & SPECIALIZATIONS ---
    # ============================================================

    FAQ(
        keyword="btech",
        question="What B.Tech branches are offered at GCET?",
        answer="GCET offers engineering programs including Computer Science and Engineering, CSE specializations such as Artificial Intelligence and Machine Learning and Data Science, Information Technology, Electronics and Communication Engineering, Electrical/Electronics-related programs and Mechanical Engineering."
    ),

    FAQ(
        keyword="intake",
        question="What is the seat intake capacity for B.Tech CSE?",
        answer="The approved intake can vary between academic sessions and branches. Students should check the latest official GCET/UPTAC seat matrix for the current year's exact intake."
    ),

    # ============================================================
    # --- FEE STRUCTURE & SCHOLARSHIPS ---
    # ============================================================

    FAQ(
        keyword="fee",
        question="What is the annual tuition fee for B.Tech?",
        answer="The annual B.Tech fee depends on the branch, academic session and applicable university or institutional charges. Students should check the latest official fee structure before admission because fees can change between academic years."
    ),

    FAQ(
        keyword="scholarship",
        question="Are UP Government or merit scholarships available?",
        answer="Eligible students may apply for government scholarship schemes according to the applicable rules. Fee waiver seats may also be available through UPTAC for eligible candidates. Students should check the latest UPTAC and government scholarship guidelines."
    ),

    # ============================================================
    # --- DOCUMENTS & LATERAL ENTRY ---
    # ============================================================

    FAQ(
        keyword="document",
        question="What documents are required during admission reporting?",
        answer="Commonly required documents include 10th and 12th marksheets and certificates, JEE Main scorecard, UPTAC allotment letter, transfer or migration certificate, category certificate if applicable, income certificate where required, Aadhaar or other identity proof and passport-size photographs. The exact list should be verified from the current admission instructions."
    ),

    FAQ(
        keyword="lateral",
        question="Is lateral entry admission available for Diploma/B.Sc students?",
        answer="B.Tech lateral entry may be available for eligible Diploma or B.Sc candidates through the applicable UPTAC admission process. Eligibility and seat availability depend on the current year's rules."
    ),

    # ============================================================
    # --- HOSTEL & FACILITIES ---
    # ============================================================

    FAQ(
        keyword="hostel",
        question="What are the hostel rules and charges?",
        answer="Hostel facilities are available for students subject to availability and the current hostel policy. Charges, room types, facilities, food and rules can change, so students should check the latest official hostel information before admission."
    ),

    FAQ(
        keyword="location",
        question="Where is Galgotias College located?",
        answer="Galgotias College of Engineering and Technology is located at Plot No. 1, Knowledge Park II, Greater Noida, Uttar Pradesh."
    ),

    # ============================================================
    # --- PLACEMENTS ---
    # ============================================================

    FAQ(
        keyword="placement",
        question="What are the average and highest placement packages at Galgotias College?",
        answer="According to published 2024-25 placement data for Galgotias College, 731 domestic placements were reported, along with 723 pre-placement offers and 150 companies offering jobs. The reported average salary was approximately ₹6.24 LPA and the highest salary was approximately ₹27 LPA. Placement outcomes vary by branch and student."
    ),

    FAQ(
        keyword="placement_statistics",
        question="What are the latest placement statistics of Galgotias College?",
        answer="Published 2024-25 data reports 731 domestic placements, 723 pre-placement offers and 150 companies offering jobs. The reported average salary was approximately ₹6.24 LPA and the highest salary was approximately ₹27 LPA."
    ),

    FAQ(
        keyword="highest_package",
        question="What is the highest placement package at Galgotias College?",
        answer="The published 2024-25 placement data for Galgotias College reports a highest salary of approximately ₹27 LPA."
    ),

    FAQ(
        keyword="average_package",
        question="What is the average placement package at Galgotias College?",
        answer="The published 2024-25 placement data reports an average salary of approximately ₹6.24 LPA."
    ),

    FAQ(
        keyword="placement_companies",
        question="Which companies recruit students from Galgotias College?",
        answer="Recruiters associated with the institution include companies such as TCS, Infosys, Wipro, Cognizant, Capgemini, HCL, Tech Mahindra and other technology and engineering companies. The companies visiting can change from year to year."
    ),

    FAQ(
        keyword="placement_branch",
        question="Which branch has the best placements at Galgotias College?",
        answer="CSE and computer-focused branches generally have the widest range of software and technology placement opportunities. However, individual placement outcomes depend on programming skills, internships, projects, communication skills and interview performance."
    ),

    # ============================================================
    # --- BRANCH-WISE PLACEMENTS ---
    # ============================================================

    FAQ(
        keyword="cse_placement",
        question="What are the placement opportunities for CSE students at Galgotias College?",
        answer="CSE students can pursue software development, web development, cloud, cybersecurity, data, consulting and other technology roles. Their opportunities include both service-based and product-oriented companies depending on the recruitment season."
    ),

    FAQ(
        keyword="aiml_placement",
        question="What are the placement opportunities for CSE AI/ML students?",
        answer="CSE AI/ML students can target software development, machine learning, artificial intelligence, data analytics and related technology roles. Strong programming, DSA, Python, machine learning projects and internships can improve placement opportunities."
    ),

    FAQ(
        keyword="ds_placement",
        question="What are the placement opportunities for CSE Data Science students?",
        answer="Data Science students can pursue software development, data analyst, data engineering, business intelligence and data science roles. Python, SQL, statistics, machine learning and practical projects are useful skills for these careers."
    ),

    FAQ(
        keyword="it_placement",
        question="What are the placement opportunities for IT students at Galgotias College?",
        answer="IT students can apply for software development, web development, cloud, cybersecurity, testing, database and IT services roles. Many recruiters hiring for software positions consider both IT and CSE students."
    ),

    FAQ(
        keyword="ece_placement",
        question="What are the placement opportunities for ECE students?",
        answer="ECE students can pursue both software and electronics careers. Opportunities may include software development, embedded systems, electronics, networking, IoT, VLSI and other technology roles."
    ),

    FAQ(
        keyword="eee_placement",
        question="What are the placement opportunities for Electrical and Electronics students?",
        answer="Electrical and Electronics students can explore software, automation, electronics, embedded systems, electrical systems and core engineering roles. Practical projects and relevant technical certifications can improve career opportunities."
    ),

    FAQ(
        keyword="mechanical_placement",
        question="What are the placement opportunities for Mechanical Engineering students?",
        answer="Mechanical students can pursue manufacturing, production, design, automobile, maintenance, operations and other engineering roles. Students who develop programming and analytical skills can also apply for software and analytics positions."
    ),

    FAQ(
        keyword="placement_eligibility",
        question="What skills should I develop for better placements at Galgotias College?",
        answer="For technology placements, students should focus on DSA, programming, communication, aptitude, projects, internships and Git/GitHub. AI/ML and Data Science students should additionally learn Python, SQL, statistics and machine learning."
    ),

    # ============================================================
    # --- ABOUT GALGOTIAS COLLEGE ---
    # ============================================================

    FAQ(
        keyword="about",
        question="Tell me about Galgotias College of Engineering and Technology.",
        answer="Galgotias College of Engineering and Technology (GCET) is an engineering institution located in Knowledge Park II, Greater Noida. The college was established in 2000 and is affiliated with Dr. A.P.J. Abdul Kalam Technical University (AKTU)."
    ),

    FAQ(
        keyword="history",
        question="When was Galgotias College established?",
        answer="Galgotias College of Engineering and Technology was established in 2000 and has more than two decades of experience in engineering education."
    ),

    FAQ(
        keyword="campus",
        question="How large is the Galgotias College campus?",
        answer="The official Galgotias College website describes the GCET campus as a 19-acre campus located in Knowledge Park II, Greater Noida."
    ),

    FAQ(
        keyword="affiliation",
        question="Which university is Galgotias College affiliated with?",
        answer="Galgotias College of Engineering and Technology is affiliated with Dr. A.P.J. Abdul Kalam Technical University (AKTU), Uttar Pradesh."
    ),

    FAQ(
        keyword="recognition",
        question="Is Galgotias College approved and recognized?",
        answer="GCET is an AICTE-approved institution and is affiliated with Dr. A.P.J. Abdul Kalam Technical University, Uttar Pradesh."
    ),

    # ============================================================
    # --- ACHIEVEMENTS & SUCCESS ---
    # ============================================================

    FAQ(
        keyword="achievements",
        question="What are some achievements of Galgotias College students?",
        answer="Galgotias students have achieved success in academics, innovation, sports, entrepreneurship and technical competitions. The college regularly highlights student achievements and innovations through its official platforms."
    ),

    FAQ(
        keyword="awards",
        question="How many awards has Galgotias College received?",
        answer="The official Galgotias College website highlights more than 300 awards among its institutional achievements."
    ),

    FAQ(
        keyword="student_success",
        question="What makes Galgotias College successful?",
        answer="Galgotias College focuses on academic education, practical learning, industry interaction, student innovation, extracurricular activities and placement opportunities. The institution also highlights student achievements and institutional successes."
    ),

    FAQ(
        keyword="student_achievements",
        question="What kind of achievements do Galgotias students have?",
        answer="Students have achieved recognition through academic performance, technical competitions, innovation, research, sports, entrepreneurship and other extracurricular activities."
    ),

    FAQ(
        keyword="innovation",
        question="Does Galgotias College support student innovation and entrepreneurship?",
        answer="Yes. The institution promotes student innovation, research and entrepreneurship activities and provides opportunities for students to participate in technical and innovation-oriented initiatives."
    ),

    FAQ(
        keyword="success",
        question="What are some notable successes of Galgotias students?",
        answer="Student successes include achievements in academics, technical competitions, innovation, sports and entrepreneurship. The college publishes information about student achievements through its official platforms."
    ),

    # ============================================================
    # --- GENERAL COLLEGE QUESTIONS ---
    # ============================================================

    FAQ(
        keyword="career",
        question="Is Galgotias College good for a career in technology?",
        answer="Galgotias College can provide opportunities for students interested in technology through computer science programs, coding activities, projects, internships, technical events and campus placements. The student's own skills and preparation play a major role in career outcomes."
    ),

    FAQ(
        keyword="cse_vs_it",
        question="Should I choose CSE or IT at Galgotias College?",
        answer="Both CSE and IT can lead to software and technology careers. CSE generally provides broader exposure to computer science fundamentals, while IT focuses more on information technology and applications. If both are available, students should consider their interests, curriculum and career goals."
    ),

    FAQ(
        keyword="cse_vs_aiml",
        question="Should I choose CSE or CSE AI/ML at Galgotias College?",
        answer="CSE provides a broader computer science foundation, while CSE AI/ML provides additional focus on artificial intelligence and machine learning. Students who want maximum flexibility may prefer core CSE, while students specifically interested in AI/ML may consider the specialization."
    ),

    FAQ(
        keyword="cse_vs_ds",
        question="Should I choose CSE or CSE Data Science at Galgotias College?",
        answer="Core CSE offers a broader computer science curriculum, while CSE Data Science focuses more on data analysis, statistics, machine learning and data-related applications. Both can lead to software careers."
    ),

    FAQ(
        keyword="scope",
        question="What is the scope of CSE at Galgotias College?",
        answer="CSE graduates can pursue careers in software development, web development, mobile applications, cloud computing, cybersecurity, artificial intelligence, data science, DevOps and other technology fields."
    ),

    FAQ(
        keyword="scope_ece",
        question="What is the scope of ECE after graduating from Galgotias College?",
        answer="ECE graduates can pursue careers in electronics, embedded systems, VLSI, telecommunications, IoT and other electronics fields. They can also pursue software careers by developing programming and DSA skills."
    ),

    FAQ(
        keyword="scope_mechanical",
        question="What is the scope of Mechanical Engineering at Galgotias College?",
        answer="Mechanical Engineering graduates can pursue careers in manufacturing, automobile, production, design, maintenance, operations and other engineering industries. Higher studies and technical certifications can also improve career opportunities."
    ),
]


# ============================================================
# --- INSERT DATA INTO DATABASE ---
# ============================================================

db.add_all(admission_faqs)
db.commit()
db.close()

print(
    f"Successfully loaded {len(admission_faqs)} admission FAQs "
    "into 'galgotias_admission.db'!"
)