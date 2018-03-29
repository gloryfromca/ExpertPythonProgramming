"""
for pylint check
"""
OPTIONS = {}
A = OPTIONS.setdefault("s", 1 << len(OPTIONS))
B = OPTIONS.setdefault("a", 1 << len(OPTIONS))
C = OPTIONS.setdefault("c", 1 << len(OPTIONS))
print("s:", A, "a:", B, "c:", C)
A_SET = A | B
print("A_SET: ", A_SET)
print("OPTIONS: ", OPTIONS)
print(bool(A & A_SET))
