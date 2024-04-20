import os
from dotenv import load_dotenv
load_dotenv()
print(f"[API KEY]\n{os.environ['OPENAI_API_KEY']}")
