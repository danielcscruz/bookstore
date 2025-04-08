import factory

from product.models import Product
from product.models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker("pyint")
    # category = factory.LazyAttribute(CategoryFactory)
    title = factory.Faker("pystr")

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:  # Se categorias forem passadas, adicionamos elas
            self.category.set(extracted)  # `.set()` para ManyToMany
        else:  # Se nenhuma for passada, criamos uma por padrão
            self.category.set([CategoryFactory()])

        # if extracted:
        #     for category in extracted:
        #         self.category.set(category)
        # else:
        #     self.category.set([CategoryFactory()])

    class Meta:
        model = Product
