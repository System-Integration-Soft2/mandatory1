import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.schema.query import Query
from app.schema.mutation import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI(title="GraphQL API", version="0.1.0")
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
def root():
    return {"message": "GraphQL API"}
