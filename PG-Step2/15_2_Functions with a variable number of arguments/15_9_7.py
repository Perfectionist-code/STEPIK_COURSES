number_of_classes = int(input())
res = all(
    [
        any(
            [
                True if mark == "5" else False
                for name, mark in (input().split() for _ in range(int(input())))
            ]
        )
        for __ in range(number_of_classes)
    ]
)
print(("NO", "YES")[res])
