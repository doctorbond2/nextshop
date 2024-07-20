'use client';
import React from 'react';
import {
  FormControl,
  FormControlLabel,
  FormLabel,
  RadioGroup,
  Radio,
} from '@mui/material';
type Props = {};

function Score({}: Props) {
  const scores = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];
  return (
    <>
      <RadioGroup>
        {scores.map((score, index) => (
          <FormControlLabel
            key={index + '-score'}
            value={score}
            control={<Radio />}
            label={score}
          />
        ))}
      </RadioGroup>
    </>
  );
}

export default Score;