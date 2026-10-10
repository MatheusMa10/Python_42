import alchemy

print("=== Alembic 1 ===")
print("Acessing the alchemy module using 'import alchemy'")
print(f"Testing create_air:  Air element created")

print("Now show that not all functions can be reached")
print("this will raise an exception!")
print("Testing the hidden create_earth:", end=" ")
print(f"{alchemy.create_earth()}")