/*
export a function named uploadPhoto. It should accept
one argument fileName (string).
The function should return a Promise rejecting with an
Error and the string $fileName cannot be processed
*/

export default function uploadPhoto(fileName) {
  return Promise.reject(new Error(`${fileName} cannot be processed`));
}
