import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

"""
# regular Gemini query, without giving Gemini a specific rolemodel
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("My child (toddler) is having trouble with hurting people. What is a gentle and effective parenting technique I can use that avoids punishment and fosters connection?")
print(response.text)
"""


"""
Create a Gemini RoleModel which will give the settings for the answer, in this case a parenting coach
"""
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  system_instruction="You are a kind and creative parenting coach. Provide actionable tips for stressful parenting situations, emphasizing empathy. Your tips are need-oriented. You create a unique response on every query")

response_1 = model.generate_content("Give me a 1 sentence tip what to do when my child hurts people")
response_2 = model.generate_content("Give me a 1 sentence tip what to say when my child hurts people")
response_3 = model.generate_content("Give me a 1 sentence tip how to behave empathic when my child hurts people")
response_4 = model.generate_content("Give me a 1 sentence tip how to make up when I got mad at the child after it hurting people")
response_5 = model.generate_content("Give me a 1 sentence motivation line to make me feel better when I am stressed when my child hurts people")
response_6 = model.generate_content("Give me a 1 sentence tip how to behave when my child hurts people")
response_7 = model.generate_content("Give me a 1 sentence tip how to act when my child hurts people")
response_8 = model.generate_content("Give me a 1 sentence tip what way to stop my child, when my child hurts people")
response_9 = model.generate_content("Give me a 1 sentence tip how to prevent my child from hurting people")
response_10 = model.generate_content("Give me a 1 sentence example of how to practice with my child how to express their big feelings (like anger and frustration) with words and actions that are safe for themselves and others")
#response_11 = model.generate_content("")
#response_12 = model.generate_content("")

print(response_1.text, response_2.text, response_3.text, response_4.text, response_5.text, response_6.text, response_7.text, response_8.text, response_9.text, response_10.text)