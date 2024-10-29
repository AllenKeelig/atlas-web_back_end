export default function appendToEachArrayValue(array, appendString) {
    for (const [idx, value] of array) {
      value = array[idx];
      array[idx] = appendString + value;
    }
  
    return array;
  }