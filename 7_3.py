class Category:

    categories = []

    @classmethod
    def add(cls, category_name):
        if category_name in cls.categories:
            raise ValueError(f"Category '{category_name}' already exists")
        cls.categories.append(category_name)
        return cls.categories.index(category_name)

    @classmethod
    def get(cls, index):
        try:
            return cls.categories[index]
        except IndexError:
            raise IndexError("No such category")

    @classmethod
    def delete(cls, index):
        if index < len(cls.categories):
            del cls.categories[index]

    @classmethod
    def update(cls, index, new_category_name):
        if index == len(cls.categories):
            cls.categories.append(new_category_name)
        elif index < len(cls.categories):
            if new_category_name in cls.categories:
                raise ValueError(f"Category '{new_category_name}' already exists")
            cls.categories[index] = new_category_name