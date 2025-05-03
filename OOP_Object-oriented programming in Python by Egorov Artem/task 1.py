class Pizza:
    ingredients_dict = {'margherita': ['mozzarella', 'tomatoes'],
                   'peperoni': ['mozzarella', 'peperoni', 'tomatoes'],
                   'barbecue': ['mozzarella', 'red onion', 'sauce bbq', 'chicken']
                  }

    def __init__(self, ingredients=[]):
        self.ingredients = list(ingredients)

    @classmethod
    def barbecue(cls):
        return cls(cls.ingredients_dict['barbecue'])

    @classmethod
    def peperoni(cls):
        return cls(cls.ingredients_dict['peperoni'])

    @classmethod
    def margherita(cls):
        return cls(cls.ingredients_dict['margherita'])

# bbq = Pizza.barbecue()
# peperoni = Pizza.peperoni()
# margherita = Pizza.margherita()
# print(sorted(bbq.ingredients))
# print(sorted(peperoni.ingredients))
# print(sorted(margherita.ingredients))

# margherita_1 = Pizza.margherita()
# margherita_2 = Pizza.margherita()
# print(sorted(margherita_1.ingredients))
# margherita_2.ingredients.append('ham')
# print(sorted(margherita_2.ingredients))
# print(sorted(margherita_1.ingredients))

# pizza = Pizza()
#
# bbq = pizza.barbecue()
# peperoni = pizza.peperoni()
# print(sorted(bbq.ingredients))
# print(sorted(peperoni.ingredients))