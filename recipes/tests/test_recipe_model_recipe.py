from django.core.exceptions import ValidationError

from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        return super().setUp()

    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = 'A' * 64

        self.assertRaises(ValidationError)
        self.recipe.full_clean()
        self.recipe.save()
        self.fail(self.recipe.title)
