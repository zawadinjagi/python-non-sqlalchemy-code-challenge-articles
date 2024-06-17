class Article:
    # A class-level attribute which stores all instances of Article
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        self._magazine._articles.remove(self)
        value._articles.append(self)
        self._magazine = value

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author")
        self._author._articles.remove(self)
        value._articles.append(self)
        self._author = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

    def remove_article(self, article):
        self._articles.remove(article)


# Class-level attribute which will store all instances of Magazine
class Magazine:
    _magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string with 2 to 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []
        Magazine._magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string with 2 to 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        from collections import Counter
        author_count = Counter(article.author for article in self._articles)
        contributing_authors = [author for author, count in author_count.items() if count > 2]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        if not cls._magazines:
            return None
        return max(cls._magazines, key=lambda magazine: len(magazine.articles()))


# Test method to check immutability of title
def test_title_is_immutable_str():
    """title is an immutable string"""
    author = Author("Carry Bradshaw")
    magazine = Magazine("Vogue", "Fashion")
    article_1 = Article(author,magazine, "How to wear a tutu with style")

    try:
        article_1.title = 500
    except AttributeError:
        print("Test passed: Title is immutable")
    else:
        raise AssertionError("Expected an AttributeError because title should be immutable")


# Running the test

def test_name_is_immutable_string():
    """author name is of type str and cannot change"""
    author_1 = Author("Carry Bradshaw")
    author_2 = Author("Nathaniel Hawthorne")

    assert isinstance(author_1.name, str)
    assert isinstance(author_2.name, str)

    try:
        author_1.name = "ActuallyTopher"
    except AttributeError:
        print("Test passed: Author name is immutable")
    else:
        raise AssertionError("Expected an AttributeError because author name should be immutable")
    def test_name_is_mutable_string():
        """magazine name is of type str and can change"""
    magazine_1 = Magazine("Vogue", "Fashion")
    magazine_2 = Magazine("AD", "Architecture")

    assert isinstance(magazine_1.name, str)
    assert isinstance(magazine_2.name, str)

    magazine_1.name = "New Yorker"
    assert magazine_1.name == "New Yorker"

    try:
        magazine_2.name = 2
    except ValueError:
        print("Test passed: Magazine name must be a valid string")
    else:
        raise AssertionError("Expected a ValueError because magazine name should be a valid string")

# Test method to check length of magazine name
def test_name_len():
    """magazine name is between 2 and 16 characters, inclusive"""
    magazine_1 = Magazine("Vogue", "Fashion")
    magazine_2 = Magazine("AD", "Architecture")

    assert 2 <= len(magazine_1.name) <= 16
    assert 2 <= len(magazine_2.name) <= 16

    try:
        magazine_1.name = "New Yorker Plus X"
    except ValueError:
        print("Test passed: Magazine name must be between 2 and 16 characters")
    else:
        raise AssertionError("Expected a ValueError because magazine name should be between 2 and 16 characters")

# Test method to check mutability of magazine category
def test_category_is_mutable_string():
    """magazine category is of type str and can change"""
    magazine_1 = Magazine("Vogue", "Fashion")
    magazine_2 = Magazine("AD", "Architecture")

    assert isinstance(magazine_1.category, str)
    assert isinstance(magazine_2.category, str)

    magazine_1.category = "Life Style"
    assert magazine_1.category == "Life Style"

    try:
        magazine_2.category = 2
    except ValueError:
        print("Test passed: Magazine category must be a valid string")
    else:
        raise AssertionError("Expected a ValueError because magazine category should be a valid string")

# Test method to check length of magazine category
def test_category_len():
    """magazine category has length greater than 0"""
    magazine_1 = Magazine("Vogue", "Fashion")

    assert magazine_1.category != ""

    try:
        magazine_1.category = ""
    except ValueError:
        print("Test passed: Magazine category must have length greater than 0")
    else:
        raise AssertionError("Expected a ValueError because magazine category should have length greater than 0")
