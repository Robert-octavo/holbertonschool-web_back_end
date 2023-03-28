/*
Create a function getStudentIdsSum that returns the sum of all the student ids.
It should accept a list of students (from getListStudents) as a parameter.
You must use the reduce function on the array.
*/
export default function getStudentIdsSum(getListStudents) {
  return getListStudents.reduce((sum, student) => sum + student.id, 0);
}
