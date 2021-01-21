def rename(problem_address: str) -> str:
    return problem_address.replace(" ", "_").lower()


print(rename("70 Climbing Stairs"))
