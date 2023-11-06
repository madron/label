import factory
from .. import models


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Brand

    name = factory.Sequence(lambda n: 'brand-{}'.format(n))


class LabelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Label

    name = factory.Sequence(lambda n: 'label-{}'.format(n))
    brand = factory.SubFactory(BrandFactory)
