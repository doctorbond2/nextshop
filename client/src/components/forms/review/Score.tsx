'use client';
import React from 'react';
import {
  FormControl,
  FormControlLabel,
  FormLabel,
  RadioGroup,
  Radio,
} from '@mui/material';
type Props = {
  scoreName: string;
};

function Score({ scoreName }: Props) {
  const scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  return (
    <>
      <RadioGroup>
        {scores.map((score, index) => (
          <FormControlLabel
            key={index + '_score'}
            value={score}
            control={<Radio />}
            label={score}
            name={scoreName + '_score'}
            id={scoreName + '_score'}
          />
        ))}
      </RadioGroup>
    </>
  );
}

export default Score;
