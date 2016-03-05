from recipes import Recipe, MeasurmentUnitTypes
from .people import alex_kessinger

recipe = Recipe(title='Skirt Steak', creator=[alex_kessinger], recorder=[alex_kessinger], portions=4)

recipe.set_description("""
Around the time that Audrey was born, I started to get interested in grilling. I had spend a fair amount of time cooking,
but I got the urge to grill. Skirt Steak was one of my early success. Most of all because it's simple.

I have head skirt steak prepared via other methods, but grilling, on hardwood charcoal is objectivley better. The smoke
adds an imense amount of flavor to the fatty meat, and that is the seasoning, more then the salt, or the oil.

Skirt steak has unfortunatley been discovered, and so it is expensive. The Berkeley Bowl is selling it for 15.99 a pound.
If you want almost the same experience with a cheaper cut of meat get a butcher steak, or I have heard it refered to as a
hanger steak. It has a serious tendon right down the middle, but just eat around it.

Putting rosemary sticks on the coals, and rubbing the meat with rosemary is a nice addition.
""")

recipe.add_requirements(
  ('A grill, get it hot', ),
  ('Tongs, because the grill will be hot', ),
)


recipe.add_ingredients(
  ('Skirt Steak', 1),
  ('Toasted Seasame Oil', 2, MeasurmentUnitTypes.ounce),
  ('Salt, enough to cover the steak', ),
  ('Pepper, enough to cover the steak', ),
)

recipe.add_instructions(
  ('Cut the strip into managable pieces', ),
  ('Salt, and pepper both sides', ),
  ('Use the oil sparingly, but cover the surface', ),
  ('Place meat on hot grill, cook to rare, the outside should be almost charred', ),
  ('Let the meat rest, then cut into strips', ),
)
