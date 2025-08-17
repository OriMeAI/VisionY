import React, { useEffect, useState } from 'react';

interface IncrementingNumberProps {
  start: number;
  end: number;
  duration: number;
}

const IncrementingNumber: React.FC<IncrementingNumberProps> = ({ start, end, duration }) => {
  const [number, setNumber] = useState(start);

  useEffect(() => {
    const increment = (end - start) / (duration / 1000 * 60);
    let currentNumber = start;

    const interval = setInterval(() => {
      currentNumber += increment;
      if (currentNumber >= end) {
        currentNumber = end;
        clearInterval(interval);
      }
      setNumber(Math.floor(currentNumber));
    }, 1000 / 60);

    return () => clearInterval(interval);
  }, [start, end, duration]);

  return <span>{number.toLocaleString()}</span>;
};

export default IncrementingNumber;