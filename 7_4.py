class Category:
    categories = []

    @classmethod
    def add(cls, name):
        for category in cls.categories:
            if category["name"] == name:
                raise ValueError("Category already exists")
        cls.categories.append({"name": name, "is_published": False})
        return len(cls.categories) - 1

    @classmethod
    def get(cls, index):
        return cls.categories[index]

    @classmethod
    def delete(cls, index):
        try:
            del cls.categories[index]
        except IndexError:
            pass

    @classmethod
    def update(cls, index, new_name):
        if index < 0 or index >= len(cls.categories):
            cls.add(new_name)
        else:
            for i, category in enumerate(cls.categories):
                if i != index and category["name"] == new_name:
                    raise ValueError("Category already exists")
            cls.categories[index]["name"] = new_name

    @classmethod
    def make_published(cls, index):
        try:
            cls.categories[index]["is_published"] = True
        except IndexError:
            raise IndexError("Index out of range")

    @classmethod
    def make_unpublished(cls, index):
        try:
            cls.categories[index]["is_published"] = False
        except IndexError:
            raise IndexError("Index out of range")