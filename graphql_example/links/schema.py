from typing import Any
from graphql_example.links.models import Link
import graphene


class Query(graphene.ObjectType):
    links = graphene.List(Link)

    def resolve_links(self, info: str, **kwargs: Any):
        return
