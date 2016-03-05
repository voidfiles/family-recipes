from recipes import Recipe, MeasurmentUnitTypes
from .people import alex_kessinger

recipe = Recipe(title='Roast Chicken and Roast Vegetales', creator=[alex_kessinger], recorder=[alex_kessinger], portions=4)

recipe.set_description("""
I first tried this recipe based on an Alton Brown Recipe. I have made my own additions, and tweaks though.

The key here is that the chiken skin is not water permeable, so if you want the meat to be flavored,
you have to get under the skin. So, by creating a tasty mixture, and the getting it under the skin
you will be able to permeate the meat with flavor.

I like to roast the chiken with potatoes, and vegetables all at once. YMMV.
""")

recipe.add_requirements(
  ('A roast pan, and rack', ),
  ('An oven', ),
)


recipe.add_ingredients(
  ('Fryer Chiken', 1),
  ('Cloves of garlic', 2),
  ('Rosemary, minced', 1, MeasurmentUnitTypes.ounce),
  ('Stick of butter', 1),
  ('Lemon', 1),
  ('Salt', ),
  ('Pepper', ),
  ('Small potatoes, or cut potatoes to 1 1/2 inch', 10),
  ('Cleaned, but not peeled carrots', 6),
  ('Something to deglaze the roast pan', 8, MeasurmentUnitTypes.ounce),
)

recipe.add_instructions(
  ('Prepare vegtables, place at bottom of roasting pan', ),
  ('Coarsley salt the vegtables', ),
  ('Melt the butter in glass, 30 seconds in the microwave', ),
  ('Mince the garlic, mix with rosemary, a pinch of salt, and half the melted butter', ),
  ('Dry the chicken', ),
  ('Starting at the neck, work your fingers between the skin and the meat', ),
  ('Place bird breast side down on roasting rack', ),
  ('Get oven to 450', ),
  ('Insert roasting pan into oven, cook for 30 minutes or so', ),
  ('Rotate bird breast side up, cook for another 30 - 45 minutes', ),
  ('Remove bird from oven, juices should run clear', ),
  ('Rest bird', ),
  ('Get vegetables out with slotted spoon', ),
  ('You should be able to make a gravy here, or a jus. It never worked for me', )
)
