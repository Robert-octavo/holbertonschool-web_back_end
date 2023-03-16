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
            let value = employees[index];
            let done = index >= employees.length;
            index++;
            return { value, done };
        }
    };
}