import yaml

from family_recipes import pasta_carbonara, skirt_steak, roast_chicken


data = {
  'title': 'The Kessinger Family Cookbook',
  'authors': [
    'Alex Kessinger',
    'Rachel Kessinger',
    'Audrey Kessinger',
    'Jonah Kessinger',
  ],
  "classoption": "twocolumn",
}


def format_book_as_markdown():
    output = [u'']
    output += [u'---']
    output += [unicode(yaml.dump(data))]
    output += [u'---']
    output += [u'# Pasta']
    output += [unicode(pasta_carbonara.recipe), u'\\newpage']
    output += [u'# Meat']
    output += [unicode(skirt_steak.recipe), u'\\newpage']
    output += [unicode(roast_chicken.recipe), u'\\newpage']

    return u'\n'.join(output)


if __name__ == '__main__':
    print format_book_as_markdown()
