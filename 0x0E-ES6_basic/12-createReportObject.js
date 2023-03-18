export default function createReportObject(employeesList) {

  const newObject = {
    allEmployees: employeesList,
    getNumberOfDepartments: function (employees) {
      return Object.keys(employees).length;
    }
  };

  return newObject;
}