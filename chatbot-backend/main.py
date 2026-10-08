from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
import re
from difflib import SequenceMatcher


# ============================================================
# FASTAPI APP
# ============================================================

app = FastAPI()


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# DATABASE
# ============================================================

DATABASE_URL = "sqlite:///./galgotias_admission.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


class FAQ(Base):
    __tablename__ = "faqs"

    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String, index=True)
    question = Column(String)
    answer = Column(Text)


Base.metadata.create_all(bind=engine)


# ============================================================
# DATABASE SESSION
# ============================================================

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(text):
    """
    Convert user input into a clean comparable format.
    """

    text = text.lower()

    # Replace common symbols
    text = text.replace("&", " and ")
    text = text.replace("/", " ")
    text = text.replace("-", " ")

    # Remove punctuation
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


# ============================================================
# SYNONYMS / ABBREVIATIONS
# ============================================================

SYNONYMS = {

    # Computer branches
    "cse": ["computer science", "computer science engineering"],
    "cs": ["computer science"],
    "aiml": [
        "ai ml",
        "ai and ml",
        "artificial intelligence",
        "machine learning",
        "artificial intelligence and machine learning"
    ],
    "ai": ["artificial intelligence"],
    "ml": ["machine learning"],

    "ds": [
        "data science",
        "data sciences"
    ],

    "it": [
        "information technology"
    ],

    "ece": [
        "electronics communication",
        "electronics and communication",
        "electronics communication engineering"
    ],

    "eee": [
        "electrical electronics",
        "electrical and electronics"
    ],

    "me": [
        "mechanical",
        "mechanical engineering"
    ],

    # Admission
    "admission": [
        "admissions",
        "admit",
        "joining",
        "join"
    ],

    "counselling": [
        "counseling",
        "uptac",
        "counselling process",
        "counseling process"
    ],

    "cutoff": [
        "cut off",
        "closing rank",
        "closing ranks",
        "opening rank",
        "opening ranks",
        "rank required",
        "required rank"
    ],

    "rank": [
        "jee rank",
        "jee main rank",
        "closing rank",
        "opening rank"
    ],

    # Placement
    "placement": [
        "placements",
        "job",
        "jobs",
        "career",
        "package",
        "salary",
        "recruitment"
    ],

    "package": [
        "salary",
        "ctc",
        "lpa",
        "placement package"
    ],

    "highest": [
        "highest package",
        "highest salary",
        "maximum package"
    ],

    "average": [
        "average package",
        "average salary"
    ],

    # College information
    "about": [
        "about college",
        "about galgotias",
        "information about college",
        "college information"
    ],

    "history": [
        "established",
        "founded",
        "started",
        "year established"
    ],

    "campus": [
        "college campus",
        "campus size"
    ],

    "achievement": [
        "achievements",
        "success",
        "successes",
        "awards",
        "student achievements"
    ],

    # Fees
    "fee": [
        "fees",
        "tuition",
        "tuition fee",
        "college fees"
    ],

    "scholarship": [
        "scholarships",
        "financial aid",
        "fee waiver"
    ],

    # Hostel
    "hostel": [
        "hostels",
        "accommodation",
        "room",
        "hostel fee",
        "hostel fees"
    ],
}


# ============================================================
# STOP WORDS
# ============================================================

STOP_WORDS = {
    "a",
    "an",
    "the",
    "is",
    "are",
    "was",
    "were",
    "what",
    "which",
    "how",
    "where",
    "when",
    "why",
    "can",
    "could",
    "should",
    "would",
    "do",
    "does",
    "did",
    "i",
    "me",
    "my",
    "we",
    "you",
    "your",
    "at",
    "to",
    "for",
    "of",
    "in",
    "on",
    "with",
    "and",
    "or",
    "college",
    "galgotias",
    "tell",
    "about"
}


# ============================================================
# GET IMPORTANT WORDS
# ============================================================

def get_words(text):
    text = normalize_text(text)

    words = text.split()

    return {
        word
        for word in words
        if word not in STOP_WORDS and len(word) > 1
    }


# ============================================================
# EXPAND USER QUERY
# ============================================================

def expand_query(text):
    """
    Adds known synonyms/abbreviations.

    Example:

    cse vs ds

    becomes related to:

    cse
    computer science
    ds
    data science
    """

    text = normalize_text(text)

    expanded = text

    words = text.split()

    for word in words:

        if word in SYNONYMS:

            for synonym in SYNONYMS[word]:
                expanded += " " + synonym

    return expanded


# ============================================================
# SIMILARITY FUNCTION
# ============================================================

def similarity(text1, text2):

    text1 = normalize_text(text1)
    text2 = normalize_text(text2)

    return SequenceMatcher(
        None,
        text1,
        text2
    ).ratio()


# ============================================================
# FAQ MATCHING
# ============================================================

def find_best_faq(user_msg, faqs):

    user_msg = normalize_text(user_msg)

    expanded_user_msg = expand_query(user_msg)

    user_words = get_words(expanded_user_msg)

    best_faq = None
    best_score = 0

    for faq in faqs:

        keyword = normalize_text(faq.keyword or "")
        question = normalize_text(faq.question or "")

        # ----------------------------------------------------
        # 1. Keyword score
        # ----------------------------------------------------

        keyword_words = set(keyword.replace("_", " ").split())

        keyword_matches = user_words.intersection(keyword_words)

        keyword_score = len(keyword_matches) * 0.20

        # ----------------------------------------------------
        # 2. Question word matching
        # ----------------------------------------------------

        question_words = get_words(question)

        common_words = user_words.intersection(question_words)

        if question_words:

            question_score = (
                len(common_words) / len(question_words)
            )

        else:

            question_score = 0

        # ----------------------------------------------------
        # 3. User words coverage
        # ----------------------------------------------------

        if user_words:

            coverage_score = (
                len(common_words) / len(user_words)
            )

        else:

            coverage_score = 0

        # ----------------------------------------------------
        # 4. Fuzzy similarity
        # ----------------------------------------------------

        fuzzy_score = similarity(
            expanded_user_msg,
            question
        )

        # ----------------------------------------------------
        # FINAL SCORE
        # ----------------------------------------------------

        score = (
            keyword_score
            + question_score * 0.35
            + coverage_score * 0.25
            + fuzzy_score * 0.40
        )

        # ----------------------------------------------------
        # Special handling for keyword phrases
        # ----------------------------------------------------

        keyword_phrase = keyword.replace("_", " ")

        if keyword_phrase and keyword_phrase in expanded_user_msg:

            score += 0.50

        # ----------------------------------------------------
        # Keep highest match
        # ----------------------------------------------------

        if score > best_score:

            best_score = score
            best_faq = faq

    # --------------------------------------------------------
    # Minimum confidence
    # --------------------------------------------------------

    if best_score >= 0.45:

        return best_faq

    return None


# ============================================================
# CHAT API
# ============================================================

@app.post("/chat")
def chat_response(
    data: dict,
    db: Session = Depends(get_db)
):

    user_msg = data.get("message", "").strip()

    if not user_msg:

        return {
            "reply": "Please ask me a question about Galgotias College."
        }

    # Get all FAQs
    faqs = db.query(FAQ).all()

    # Find best FAQ
    best_faq = find_best_faq(
        user_msg,
        faqs
    )

    # Return answer
    if best_faq:

        return {
            "reply": best_faq.answer
        }

    # No good match
    return {
        "reply": (
            "I couldn't find specific details for that query. "
            "You can ask me about admissions, UPTAC counselling, "
            "cutoffs, branches, fees, scholarships, hostel, "
            "placements or Galgotias College."
        )
    }


# ============================================================
# ROOT API
# ============================================================

@app.get("/")
def root():

    return {
        "message": "Galgotias College Admission Chatbot API is running!"
    }