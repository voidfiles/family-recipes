import pytest

from datetime import datetime
from family_recipes.recipes.recipe import (Ingredient, MeasurmentUnitTypes, Entity, RequirementTypes,
                                           Requirement, Recipe, Instruction, TimeUnitTypes, Annotation)


class TestSlowjam(object):

    def test_entity(self):
        entity = Entity('Alexander', 'Kessinger', 'James', 'Alex Kessinger')

        assert entity == Entity.from_data(entity.to_data())

    def test_ingredient(self):
        ingredient = Ingredient('water', 1, MeasurmentUnitTypes.cup)

        assert ingredient == Ingredient.from_data(ingredient.to_data())

    def test_instruction(self):
        instruction = Instruction('bring water to boil')
        assert instruction == Instruction.from_data(instruction.to_data())

        instruction = Instruction('bring water to boil', 10, TimeUnitTypes.minute)
        assert instruction == Instruction.from_data(instruction.to_data())

    def test_annotation(self):
        annotation = Annotation('testing', ['test.testing', 'awesome.moreawesome'])

        assert annotation == Annotation.from_data(annotation.to_data())

    def test_requirement(self):
        description = 'testing'
        requirement0 = Requirement(description)
        assert requirement0.description == description

        requirement1 = Requirement(description, RequirementTypes.vessel)
        assert requirement1.kind == RequirementTypes.vessel

        requirement2 = Requirement(description, RequirementTypes.vessel)
        assert requirement1 == requirement2
        assert requirement0 != requirement1

        requirement3 = Requirement(description, RequirementTypes.vessel, 'test')

        test_data = {
            'description': description,
            'kind': int(RequirementTypes.vessel),
            'label': 'test',
        }

        assert requirement3.to_data() == test_data

        assert requirement3 == Requirement.from_data(test_data)

    def test_recipe(self):
        recipe = Recipe()

        recipe.add_creators('Alex', 'Kessinger')
        assert len(recipe.creators) == 1
        recipe.add_creators('Alex', 'Kessinger')
        assert len(recipe.creators) == 1

        recipe.add_recorders('Audrey', 'Kessinger')
        recipe.add_recorders('Alex', 'Kessinger')
        assert len(recipe.recorders) == 2

        dt = datetime.utcnow()
        recipe.set_created(dt)
        assert recipe.created == dt

        recipe.set_recorded(dt)
        assert recipe.recorded == dt

        recipe.add_requirements(
            ('stove', RequirementTypes.appliance),
            Requirement('non-stick pan', RequirementTypes.vessel),
            Requirement('non-stick pan', RequirementTypes.vessel),
        )

        assert len(recipe.requirements) == 2

        recipe.add_ingredients(
            ('egg', 1),
            ('salt', 1, MeasurmentUnitTypes.pinch)
        )

        assert len(recipe.ingredients) == 2

        recipe.add_instructions(
            ('Crack eggs into bowl', ),
            ('Beat eggs until thouroughly mixed', ),
            ('Heat pan to medium', ),
        )

        assert len(recipe.instructions) == 3

        recipe.add_annotations(
            ('Great breakfast meal', ['meal.breakfast']),
        )

        assert len(recipe.annotations) == 1
