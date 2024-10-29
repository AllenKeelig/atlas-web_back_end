export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,

    getNumberOfDepartments: (dpt) => Object.keys(employeesList).length,
    }
}
