import React from 'react';
import { clientInstance as a } from '@/classes/axiosInstance';
import api from '@/classes/api';
import endpoints from '@/classes/endpoints';
import { Button } from '@mui/material';
type Props = {
  data: any[];
};
import { AxiosResponse } from 'axios';

const getData = async (): Promise<AxiosResponse<any[]>> => {
  const res = await api.get(endpoints.getAllGames);

  if (res.status !== 200) {
    throw new Error('Error fetching data');
  }
  return res;
};

async function Games({}: Props) {
  try {
    const res: any = await getData();
    return (
      <>
        {res.data.map((game: any, index: number) => (
          <>
            <div key={index}></div>

            <h2 style={{ color: 'white' }}>{game.title}</h2>
          </>
        ))}
      </>
    );
  } catch (error) {
    console.error(error);
    return (
      <>
        <h3 style={{ color: 'white' }}>Error fetching data</h3>
      </>
    );
  }
}
export default Games;
