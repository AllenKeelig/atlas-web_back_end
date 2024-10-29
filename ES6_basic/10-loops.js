export default function appendToEachArrayValue(array, appendString) {
    for (const value of array) {
      array[idx] = appendString + value;
      idx++
    }
  
    return array;
  }