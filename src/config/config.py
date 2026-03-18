import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for RAG system"""

    # API Key
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    # Model Configuration
    LLM_MODEL = "llama-3.3-70b-versatile"

    # Document Processing
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50

    # Default URLs
    DEFAULT_URLS = [
        "https://www.dogsis.com/",
        "https://www.companionanimalpsychology.com/p/all-about-dogs.html",
        "https://www.dogbreedslist.info/all-dog-breeds/",
        "https://thepetworld.org/dogs",
        "https://www.dogster.com/lifestyle/most-popular-dog-websites"
    ]

    @classmethod
    def get_llm(cls):
        """Initialize and return the LLM model"""

        return ChatGroq(
            model_name=cls.LLM_MODEL,
            groq_api_key=cls.GROQ_API_KEY
        )