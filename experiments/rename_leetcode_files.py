def rename(problem_address: str, num) -> str:
    return F"{num}_" + problem_address.replace(" ", "_").lower()


print(rename("Add Two Numbers", 2))
