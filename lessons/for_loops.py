xs: list[str] = ["w", "x", "y", "z"]
idx: int = 0
# while idx < len(xs):
# print(xs[idx])
# idx += 1
# for x in xs:
# print(x)

pets: list[str] = ["Louie", "Bo", "Bear"]
for pet in pets:
    print(f"Good boy, {pet}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(len(names)):
    print(f"{idx}: {names[idx]}")
