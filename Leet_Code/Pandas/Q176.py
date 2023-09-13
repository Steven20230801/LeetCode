import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset="salary")
    employee = employee.sort_values(by="salary", ascending=False)
    if len(employee) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    else:
        return pd.DataFrame({"SecondHighestSalary": [employee.iloc[1]["salary"]]})


if __name__ == "__main__":
    employee = pd.DataFrame(
        {
            "Id": [1, 2, 3],
            "Name": ["Joe", "Henry", "Sam"],
            "Salary": [70000, 80000, 60000],
            "DepartmentId": [1, 2, 2],
        }
    )
    print(second_highest_salary(employee))
