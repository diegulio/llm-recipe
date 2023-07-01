# First Step
first_step_template = """ You are a good chef, I need you to bring me a \
    simple recipe to cook {food}"""

first_system_template_str = """
    You are a good chef, users need you to bring them recipes from food.
"""
first_human_template_str = "{food}"

# Second Step
custom_format_instructions = """
The output should be in a json format, formatted in the following schema:
{
  "food": List // List of ingredients
  [
    {
      "ingredient": string // Name of one ingredient
      "quantity": string  // Quantity of the ingredient 
      "optional": string  // Whether or not that ingredient is optional to cook the food. "Yes" if the ingredient is not indispensable to cook, "No" if is the ingredient is indispensable.
      "estimated_price": string  // The ingredient's estimated price in dolars
      "available": string // Random "Yes" or "No"
    }
  ]
}
"""

example_instructions = """
Follow the schema of this example:
{
  "Spaguetthi With Meat":
  [
    {
      "ingredient": "Spaguetti",
      "optional": "No",
      "quantity": "200g",
      "estimated_price": "5.00",
      "available": "No"
    },
    {
      "ingredient": "Meat",
      "optional": "No",
      "quantity": "1kg",
      "estimated_price": "10.00",
      "available": "Yes"
    },
    {
      "ingredient": "Pepper",
      "optional": "Yes",
      "quantity": "at ease",
      "estimated_price": "1.00",
      "available": "No"
    }

  ]
}
"""

second_step_template = """I need you to bring me the ingredients contained in the following recipe: \
recipe: {recipe}
{format_instructions}
{example_instructions}"""
