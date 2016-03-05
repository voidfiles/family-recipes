import collections

from enum import IntEnum


class BuilderItem(object):
    @classmethod
    def builder(cls, *args, **kwargs):
        if args and isinstance(args[0], cls):
            return args[0]

        if args and args[0] is None:
            return None

        return cls(*args, **kwargs)

    def to_data(self, props):
        data = {}

        for prop in props:
            value = getattr(self, prop, None)
            if value:
                data[prop] = value

        return data

    def __eq__(self, other):
        return self.to_data() == other.to_data()

    @classmethod
    def from_data(cls, data):
        return cls(**data)


class Entity(BuilderItem):
    def __init__(self, first_name=None, last_name=None, middle_name=None, display_name=None, non_human=False,
                 unique_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.display_name = display_name or ' '.join(filter(None, [first_name, middle_name, last_name]))
        self.non_human = non_human
        self.unique_id = unique_id

    def __unicode__(self):
        return self.display_name

    def to_data(self):
        props = [
            'first_name',
            'last_name',
            'middle_name',
            'display_name',
            'non_human',
            'unique_id',
        ]

        return super(Entity, self).to_data(props)


class RequirementTypes(IntEnum):
    vessel = 1
    utensil = 2
    appliance = 3


class Requirement(BuilderItem):
    def __init__(self, description=None, kind=None, label=None):
        self.description = description
        self.kind = kind
        self.label = label

    def __unicode__(self):
        return self.description

    def to_data(self):
        props = [
            'description',
            'kind',
            'label',
        ]

        return super(Requirement, self).to_data(props)

    @classmethod
    def from_data(cls, data):
        if 'kind' in data:
            data['kind'] = RequirementTypes(data['kind'])

        return cls(**data)


class MeasurmentUnitTypes(IntEnum):
    cup = 1
    pinch = 2
    pound = 3
    ounce = 4
    bundle = 5


class Ingredient(BuilderItem):
    def __init__(self, description=None, amount=None, unit=None, unique_id=None):
        self.description = description
        self.amount = amount
        self.unit = unit
        self.unique_id = unique_id

    def __unicode__(self):
        output = u''

        if self.amount:
            output += u'%s ' % (self.amount, )

        if self.unit:
            output += u'%s ' % (self.unit.name, )

        if self.description:
            output += self.description

        return output

    def to_data(self):
        props = [
            'description',
            'amount',
            'unit',
            'unique_id',
        ]

        return super(Ingredient, self).to_data(props)

    @classmethod
    def from_data(cls, data):
        if 'unit' in data:
            data['unit'] = MeasurmentUnitTypes(data['unit'])

        return cls(**data)


class TimeUnitTypes(IntEnum):
    minute = 1


class Instruction(BuilderItem):
    def __init__(self, description=None, time=None, unit=None):
        self.description = description
        self.unit = unit
        self.time = time
        if self.time is not None:
            self.time = float(self.time)

    def __unicode__(self):
        output = u''
        if self.description:
            output += self.description + u' '

        if self.time and self.unit:
            output += u'for %s %s' % (self.time, self.unit.name)

        return output

    def to_data(self):
        props = [
            'description',
            'time',
            'unit'
        ]

        return super(Instruction, self).to_data(props)

    @classmethod
    def from_data(cls, data):
        if 'unit' in data:
            data['unit'] = TimeUnitTypes(data['unit'])

        return cls(**data)


class Annotation(BuilderItem):
    def __init__(self, description=None, tags=None):
        self.description = description
        self.tags = tags if tags else []

    def to_data(self):
        props = [
            'description',
            'tags',
        ]

        return super(Annotation, self).to_data(props)


def one_or_many(args, cls):
    if not args:
        return []

    first_arg = args[0]
    if isinstance(first_arg, cls):
        return args

    if isinstance(first_arg, basestring):
        return [cls.builder(*args)]

    if isinstance(first_arg, collections.Iterable):
        collection = []
        for arg in args:
            if isinstance(arg, cls):
                collection += [arg]
            else:
                collection += [cls.builder(*arg)]

        return collection

    return [cls.builder(*args)]


def add_stuff(prop, cls):

    def _add_stuff(self, *args):
        collection = getattr(self, prop, [])
        for arg in one_or_many(args, cls):
            if arg and arg not in collection:
                collection += [arg]

        setattr(self, prop, collection)

        return self

    return _add_stuff


def set_stuff(prop):

    def _add_stuff(self, arg):
        setattr(self, prop, arg)

        return self

    return _add_stuff


class Recipe(object):
    def __init__(self, title=None, description=None, creator=None, recorder=None, created=None, recorded=None, requirements=None,
                 ingredients=None, instructions=None, portions=None, annotations=None):

        self.title = None
        self.created = None
        self.recorded = None
        self.description = None
        self.portions = None

        self.set_title(title)
        self.set_created(created)
        self.set_recorded(recorded)

        self.add_creators(creator)
        self.add_recorders(recorder)
        self.add_requirements(requirements)
        self.add_ingredients(ingredients)
        self.add_instructions(instructions)

    add_creators = add_stuff('creators', Entity)
    add_recorders = add_stuff('recorders', Entity)
    add_requirements = add_stuff('requirements', Requirement)
    add_ingredients = add_stuff('ingredients', Ingredient)
    add_instructions = add_stuff('instructions', Instruction)
    add_annotations = add_stuff('annotations', Annotation)

    set_description = set_stuff('description')
    set_title = set_stuff('title')
    set_created = set_stuff('created')
    set_recorded = set_stuff('recorded')
    set_protions = set_stuff('portions')

    def __unicode__(self):
        output = []
        if self.title:
            output += [u'## %s' % (self.title), u'']

        if self.creators:
            output += [u'<span style="font-variant:small-caps;">',
                       u'Created by ', u', '.join(map(unicode, self.creators)),
                       u'</span>', u'']

        if self.recorders:
            output += [u'<span style="font-variant:small-caps;">',
                       u'Recorded by ', u', '.join(map(unicode, self.recorders)),
                       u'</span>', u'']

        if self.description:
            description = self.description
            description.strip()
            output += [self.description, u'']

        sections = (
            ('requirements', 'Requirements'),
            ('ingredients', 'Inredients'),
            ('instructions', 'Instructions'),
        )

        for prop, display in sections:
            value = getattr(self, prop, None)
            if value:
                output += [u"### %s" % (display), " "]
                output += map(lambda x: '* %s' % (unicode(x)), value)
                output += [u' ']

        return u'\n'.join(output)

    def to_data(self):
        props = [
            'title',
            'description',
            'created',
            'recorded',
            'creators',
            'recorders',
            'requirements',
            'ingredients',
            'instructions',
            'annotations'
        ]

        data = {}

        for prop in props:
            value = getattr(self, prop, None)
            if value:
                data[prop] = (x.to_data() for x in value)

        return data

    @classmethod
    def from_data(cls, data):
        return cls(**data)
