import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

"""
Create a Gemini RoleModel which will give the settings for the response, in this case a parenting coach
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
response_11 = model.generate_content("Give me a 1 sentence tip how to teach my child how to make up with the person it hurt")
#response_12 = model.generate_content("")

print(response_1.text, response_2.text, response_3.text, response_4.text, response_5.text, response_6.text, response_7.text, response_8.text, response_9.text, response_10.text)



"""

# regular Gemini query, without giving Gemini a specific rolemodel
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("My child (toddler) is having trouble with hurting people. What is a gentle and effective parenting technique I can use that avoids punishment and fosters connection, give me a 1 sentence tip.")
# response_1 = model.generate_content("My child (toddler) is having trouble with hurting people. What is a gentle and effective parenting technique I can use that avoids punishment and fosters connection? 1 Sentence answer")
# response_2 = model.generate_content("My child (toddler) is having trouble with hurting people. What is a gentle and effective parenting technique I can use that avoids punishment and fosters connection? 1 Sentence answer")
# response_3 = model.generate_content("My child (toddler) is having trouble with hurting people. What is a gentle and effective parenting technique I can use that avoids punishment and fosters connection? 1 Sentence answer")
# response_4 = model.generate_content("My child (toddler) is having trouble with hurting people. What is a gentle and effective parenting technique I can use that avoids punishment and fosters connection? 1 Sentence answer")
# response_5 = model.generate_content("My child (toddler) is having trouble with hurting people. What is a gentle and effective parenting technique I can use that avoids punishment and fosters connection? 1 Sentence answer")
print(response.text)

"""

"""

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  system_instruction="You are a kind, empathic and creative parenting coach. Provide actionable tips for stressful parenting situations, emphasizing empathy. Your tips are need-oriented. You create a different response on every query. with every query, you rotate your answer between only 1 of the following aspects: 1 how to act as a parent in that situation, 2 what to say in this situation, 3 how to practise in a quiet moment avoiding it in a stressful situation, 4 emphasize with the parent after the parent got angry and might have yelled at the child, 5 how the child can make up what he did with the person he hurt")

response_1 = model.generate_content("Give me a 1 sentence tip what to do when my child hurts people")
print(response_1.text)
#Gently guide your child to understand the impact of their actions and encourage them to apologize sincerely, focusing on repairing the hurt they caused.
#Gently guide your child to understand the impact of their actions on others, and help them find ways to make amends.
#Gently guide your child to understand the impact of their actions on others and help them make amends.
#Gently guide your child to understand the impact of their actions and brainstorm ways to make amends.
#Gently guide your child to understand the impact of their actions on others and help them make amends.
#Gently guide your child to understand the impact of their actions and help them make amends.

#Gently guide your child to understand the impact of their actions on others, focusing on empathy and making amends.
#Gently guide your child to understand the impact of their actions and apologize sincerely to the person they hurt.

#Gently guide your child to understand the impact of their actions and help them find ways to make amends.
#Gently guide your child to understand the impact of their actions on others, encouraging them to apologize sincerely and offer help to make amends.

"""
