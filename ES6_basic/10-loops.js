export default function appendToEachArrayValue(array, appendString) {
  const Array = [];

  let i = 0;
  for (const value of array) {
    Array[i] = appendString + value;
    i += 1;
  }

  return Array;
}
