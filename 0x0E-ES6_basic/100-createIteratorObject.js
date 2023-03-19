export default function createIteratorObject(report) {
  let index = 0;
  const employees = [];
  for (const department of Object.values(report.allEmployees)) {
    for (const employee of department) {
      employees.push(employee);
    }
  }
  return {
    next() {
      const value = employees[index];
      const done = index >= employees.length;
      index += 1;
      return { value, done };
    },
  };
}
