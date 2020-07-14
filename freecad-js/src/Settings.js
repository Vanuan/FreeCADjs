import React from 'react';
import { useQuery, gql } from '@apollo/client';

const SETTINGS = gql`
  query {
    settings {
      dump  {
        name
        value
      }
      system
      user
    }
  }
`;

export function Settings() {
  const { loading, error, data } = useQuery(SETTINGS);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  return data.settings.dump.map(({ name, value }) => (
    <div key={name}>
      <p>
        {name}: <input defaultValue={value} />
      </p>
    </div>
  ));
}

