export default function appendToEachArrayValue(array, appendString) {
  let idx = 0;
  for (const value of array) {
    idx += 1;
    array[idx] = appendString + value;
  }

  return array;
}
