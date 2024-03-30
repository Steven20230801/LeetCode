import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if len(employee.salary.unique()) < N or N < 0: # 若沒有N個不同的薪資或N為不合理輸入，則回傳None
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    else:
        employee = employee.drop_duplicates(subset="salary") # 移除重複的薪資
        employee = employee.nlargest(N, "salary", keep="first") # 找出N個最高的薪資
        employee = employee.tail(1) # 取出最後一個薪資
        return pd.DataFrame({f"getNthHighestSalary({N})": employee["salary"]})


if __name__ == "__main__":
    data = [[1, 100], [2, 200], [3, 300]]

    data = [[1, 100]]
    employee = pd.DataFrame(data, columns=["Id", "salary"]).astype(
        {"Id": "Int64", "salary": "Int64"}
    )
    df = nth_highest_salary(employee, 1)
    df
