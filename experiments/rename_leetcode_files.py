def rename(problem_address: str, num) -> str:
    return F"{num}_" + problem_address.replace(" ", "_").lower()


print(rename("Remove Zero Sum Consecutive Nodes from Linked List", 1171))
