from math import sqrt, floor

print(
    floor(
        sqrt(
            int(open("input.txt").readlines()[0].strip().split(":")[-1].replace(" ", "")) ** 2 -
            4 * int(open("input.txt").readlines()[1].strip().split(":")[-1].replace(" ", ""))
        )
    )
)