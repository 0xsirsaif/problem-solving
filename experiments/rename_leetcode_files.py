def rename(problem_address: str) -> str:
    return problem_address.replace(" ", "_").lower()


print(rename("14 Minimum Operations to Reduce X to Zero"))
