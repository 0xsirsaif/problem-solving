def rename(problem_address: str, num) -> str:
    return F"{num}_" + problem_address.replace(" ", "_").lower()


print(rename("Check If Two String Arrays are Equivalent", 8))
