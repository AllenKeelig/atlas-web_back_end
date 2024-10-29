export default function appendToEachArrayValue(array, appendString) {
  for (const value of array.entries()) {
    array[idx] = appendString + value;
  }

  return array;
}
