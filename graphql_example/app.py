from starlette.graphql import GraphQLApp
import graphene
from fastapi import FastAPI

from graphql_example.types.query import Query


if __name__ == "__main__":
    app = FastAPI()
    app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))
