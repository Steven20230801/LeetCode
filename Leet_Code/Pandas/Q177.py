import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset="salary")
    if len(employee) < N:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    else:
        employee = employee.nlargest(N, "salary").tail(1)
        return pd.DataFrame({f"getNthHighestSalary({N})": [employee["salary"]]})


if __name__ == "__main__":
    data = [[1, 100], [2, 200], [3, 300]]
    employee = pd.DataFrame(data, columns=["Id", "salary"]).astype(
        {"Id": "Int64", "salary": "Int64"}
    )
    df = nth_highest_salary(employee, 2)
    df
