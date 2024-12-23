import google.generativeai as genai
from dotenv import load_dotenv
import os
from random import choice

load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def get_ai_tip(problem_type: str):
    """
    Create a Gemini RoleModel which will give the settings for the response, in this case a parenting coach.
    Randomly picks a query from the list with different queries, which have the theme of the problem_type.
    return: new tip
    """
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      system_instruction="If the difficulty has nothing to do with some kind of problem or parenting, you answer: 'I can only answer parenting questions!'.You are a kind and creative parenting coach. Provide actionable tips for stressful parenting situations, emphasizing empathy. Your tips are need-oriented. You create a unique 1 sentence response on every query")

    list_with_diff_queries = [model.generate_content(f"Give me a tip what to do, when I have following difficulty with my child: {problem_type}"),
      model.generate_content(f"Give me a tip what to say, when I have following difficulty with my child: {problem_type}"),
      model.generate_content(f"Give me a tip how to behave empathic, when I have following difficulty with my child: {problem_type}"),
      model.generate_content(f"Give me a tip how to make up when I got mad at the child, when I have following difficulty with my child: {problem_type}"),
      model.generate_content(f"Give me a motivation line to make me feel better when I am stressed, when I have following difficulty with my child: {problem_type}"),
      model.generate_content(f"Give me a tip how to behave, when I have following difficulty with my child: {problem_type}"),
      model.generate_content(f"Give me a tip how to act, when I have following difficulty with my child: {problem_type}"),
      model.generate_content(f"Give me a tip what way to stop my child, when I have following difficulty with my child: {problem_type}"),
      model.generate_content(f"Give me a tip how to prevent my child from doing it, when I have following difficulty with my child: {problem_type}"),
      model.generate_content(f"Give me a example of how to practice words and actions in the heat of the moment, when I have following difficulty with my child: {problem_type}"),
      model.generate_content(f"Give me a tip how to teach my child how to make up with the person it hurt, when I have following difficulty with my child: {problem_type}"),
      model.generate_content(f"Give me an example of what to say to my child, when I have following difficulty with my child: {problem_type}")]

    # Randomly pick a query from the list
    new_tip = choice(list_with_diff_queries)
    return new_tip.text
