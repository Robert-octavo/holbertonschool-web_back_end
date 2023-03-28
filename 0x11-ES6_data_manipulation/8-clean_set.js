/*
- Create a function named cleanSet that returns a string of all the set
values that start with a specific string (startString).
- It accepts two arguments: a set (Set) and a startString (String).

- When a value starts with startString you only append the rest of the
string. The string contains all the values of the set separated by -.

Note:

- If startString is of type undefined, the function will return an empty string.
- If set contains undefined elements, the function will skip these elements.
*/

export default function cleanSet(set, startString) {
  if (startString === undefined || startString.length === 0) return '';
  return Array.from(set)
    .filter((value) => value !== undefined && value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-');
}

/* export default function cleanSet(set, startString) {
  const word = [];
  if (typeof set !== 'object'
  || typeof startString !== 'string'
  || startString.length === 0) {
    return '';
  }
  for (const iterator of set) {
    if (iterator && iterator.startsWith(startString)) {
      word.push(iterator.slice(startString.length));
    }
  }

  return word.join('-');
} */
