export default function appendToEachArrayValue(array, appendString) {
  for (const value of array) {
    array = appendString + value;
  }

  return array;
}
