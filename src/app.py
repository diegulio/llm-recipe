import json
import os

import gradio as gr
import openai
import pandas as pd
from dotenv import find_dotenv, load_dotenv
from langchain.chat_models import ChatOpenAI

from src.chains import chain, ingredients_chain, recipe_chain
from src.templates import (custom_format_instructions, example_instructions,
                           first_step_template, second_step_template,
                           first_human_template_str, first_system_template_str)

# load KEY
try:
    _ = load_dotenv(find_dotenv())  # read local .env file
    openai.api_key = os.environ["OPENAI_API_KEY"]
except:
    print(
        "No .env file found, please create it in order to set OPENAI_API_KEY environment variable"
    )

# Create Chain
# LLM Definition
llm = ChatOpenAI(temperature=0)
recipe_chain = recipe_chain(llm=llm, system_template=first_system_template_str, human_template=first_human_template_str)
ingredients_chain = ingredients_chain(llm=llm, template=second_step_template)
overall_chain = chain(recipe_chain=recipe_chain, ingredient_chain=ingredients_chain)


def get_ingredients(food):
    result = overall_chain(
        {
            "food": food,
            "format_instructions": custom_format_instructions,
            "example_instructions": example_instructions,
        }
    )

    recipe = result["recipe"]
    ingredients = result["ingredients"]
    dict_ingredients = json.loads(ingredients)
    key_food = list(dict_ingredients.keys())[0]
    output_df = pd.DataFrame(data=dict_ingredients[key_food])

    return recipe, output_df


# Create Interface
iface = gr.Interface(
    fn=get_ingredients,
    inputs="text",
    outputs=["text", "dataframe"],
    title="Recipe & Ingredients",
    description="This app will bring you a food's recipe and the list of ingredients needed to cook it.",
    examples=[["Lasagna"]],
)

