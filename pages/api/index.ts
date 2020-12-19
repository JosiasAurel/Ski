import {ApolloServer, gql} from "apollo-server-micro"

const typeDefs = gql`
    type User {
        name: String
        email: String
    }

    type Query {
        user: User
    }
`

const users = {
    name: "Mike Obrien",
    email: "mikeob@acme.com"
}
const resolvers = {
    Query: {
        user: () => users
    }
}

const server = new ApolloServer({typeDefs, resolvers})


export const config = {
  api: {
    bodyParser: false,
  },
}

export default server.createHandler({ path: '/api' })