import graphene
import tracks.schema
import users.schema
import graphql_jwt

class Query(users.schema.Query, tracks.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, tracks.schema.Mutation, graphene.ObjectType):
    # If credentials are correct, we will get a jwt token
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # Verify the web token that we got from token auth
    verify_token = graphql_jwt.Verify.Field()
    # Won't use this in the app
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)