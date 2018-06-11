class Pizza:
    def __init__(self,ingredients):
        self.ingredients=ingredients

    def __str__(self):
        return self.ingredients

    @classmethod
    def margherita(cls):
        return cls(['mozarella','tomotoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozarella','tomatoes','ham'])

print(Pizza.margherita())
print(Pizza.prosciutto())