from __future__ import absolute_import

from . import models
from dddp.api import API, Collection, Publication


class Presentation(Collection):
    model = models.Presentation


class Presentations(Publication):
    queries = [
        models.Presentation.objects.all(),
    ]


API.register([
    Presentation,
    Presentations,
]);
