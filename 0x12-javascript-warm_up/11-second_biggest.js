#!/usr/bin/node
function findSecondLargest (numbers) {
  if (numbers.length <= 1) {
    return 0;
  }

  // Convert arg to int and remove duplicates
  const uniqueNumbers = [...new Set(numbers.map(Number))];

  // descending sort
  const sortedNumbers = uniqueNumbers.sort((a, b) => b - a);

  // Return the second largest number, or 0 if NaN
  return sortedNumbers[1] || 0;
}

const args = process.argv.slice(2);
const numbers = args.map(Number);

// Print the second largest integer
console.log(findSecondLargest(numbers));
