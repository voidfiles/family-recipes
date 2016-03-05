from recipes import Recipe, MeasurmentUnitTypes, TimeUnitTypes
from .people import alex_kessinger

recipe = Recipe(title='Pasta Carbonara', creator=[alex_kessinger], recorder=[alex_kessinger], portions=6)

recipe.set_description("""
When I was 19, I studied abroad^[study is a term used loosely here] but This was a recipe I learned while I lived in italy.
I made a smart move and chose to stay with an italian family. The woman was clearly doing this for the money, but she still
had to feed us twice a day. And, this pasta carbonara made a weekly appereance.

I have seen american chefs, of the TV variety, cook their pasta carbonara with the bacon, but that was not how I witnessed my
host make it. She mixed it all together in a bowl at the end, and the only thing that cooked the eggs was the hot pasta.
""")

recipe.add_requirements(
  ('A non-stick pan', ),
  ('A pot to boil water for pasta', ),
  ('A stove, or hot plate', ),
  ('A chefs knife', ),
  ('A cutting board', ),
)


recipe.add_ingredients(
  ('bacon', 1, MeasurmentUnitTypes.pound),
  ('parmesean cheese', 4, MeasurmentUnitTypes.ounce),
  ('pasta', 16, MeasurmentUnitTypes.ounce),
  ('eggs', 3),
  ('salt', 1, MeasurmentUnitTypes.pinch),
  ('pepper', 1, MeasurmentUnitTypes.pinch),
  ('chives, minced', 1, MeasurmentUnitTypes.bundle)
)

recipe.add_instructions(
  ('Cut bacon into half inch slices', ),
  ('Cook bacon in a pan until crispy, set aside', ),
  ('Cook pasta in boiling water', ),
  ('In a glass bowl^[It helps retain the heat] mix together the eggs, parmesean cheese, half the chives, salt, and pepper.', ),
  ('After draining the pasta, mix with the egg mixture, and stir continuously', 1, TimeUnitTypes.minute),
  ('Top with the remaining chives, and serve', )
)
