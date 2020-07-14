import React from 'react';
import { ApolloClient, HttpLink, InMemoryCache, ApolloProvider } from '@apollo/client';

import { Settings } from './Settings';

const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: new HttpLink({
    uri: '/graphql/batch',
  })
});

function App() {
  return (
    <ApolloProvider client={client}>
      <div>
        <h1>Settings</h1>
        <Settings />
      </div>
    </ApolloProvider>
  );
}

export default App;
