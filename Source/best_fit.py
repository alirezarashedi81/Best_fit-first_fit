
def get_int(prompt, min_value=None, max_value=None):
    while True:
        raw = input(prompt)
        if not raw.lstrip('-').isdigit():
            print("Please enter a valid integer.")
            continue
        value = int(raw)
        if min_value is not None and value < min_value:
            print(f"Please enter a value greater than or equal to {min_value}.")
            continue
        if max_value is not None and value > max_value:
            print(f"Please enter a value less than or equal to {max_value}.")
            continue
        return value
    
# best fit
darkhast = []
hofreh   = []

n_requests = get_int("count darkhast: ", min_value=1, max_value=10)

for i in range(n_requests):
    darkhast.append(get_int(f"darkhast{i+1}: ", min_value=1))

n_blocks = get_int("count hofreh: ", min_value=1, max_value=10)
for i in range(n_blocks):
    hofreh.append(get_int(f"hofreh{i+1}: ", min_value=1))

for i in darkhast:
    best = -1

    for j in range(len(hofreh)):
        if hofreh[j] >= i:
            if best == -1 or hofreh[j] < hofreh[best]:
                best = j

    if best == -1:
        print(f"{i} -> ekhtesas nadarad")
    else:
        print(f"{i} -> allocated in block {hofreh[best]} (index {best})")
        hofreh[best] -= i
        print(f"    remaining block: {hofreh[best]}")

print("\nfinal hofreh:", hofreh)
