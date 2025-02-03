xkph = 60
ykph = 90

dist = int(input())

hours_taken = dist / (ykph-xkph)

minutes_taken = 60 * hours_taken

print(f"{minutes_taken:.0f} minutos")
