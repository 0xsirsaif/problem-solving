def rename(problem_address: str) -> str:
    return problem_address.replace(" ", "_").lower()


print(rename("1800 Maximum Ascending Subarray Sum"))
