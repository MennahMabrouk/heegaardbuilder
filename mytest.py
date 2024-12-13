import regina
from heegaardbuilder import HeegaardBuilder
from regina import Triangulation3

sig = "eHbecadjk"
tri = Triangulation3(sig)

weights = (0, 2, 2, 4, 5, 1, 2, 3, 0)

hb = HeegaardBuilder()
hb.setBouquet(tri, weights)

try:
    handlebody_filled = hb.fillHandlebody()
    if handlebody_filled:
        print("Handlebody filled successfully.")
    else:
        print("Handlebody filling failed.")
except Exception as e:
    print(f"Error during handlebody fill: {str(e)}")

if tri.isClosed():
    print("Triangulation is closed.")
else:
    print("Triangulation is not closed.")

print("\n--- Debugging HeegaardBuilder Attributes ---")
print("HeegaardBuilder state:", hb)
print("Triangulation state:", tri)

try:
    hb.resolveAllPetals()
    print("All petals resolved.")
except Exception as e:
    print(f"Error during petal resolution: {str(e)}")

if tri.isClosed():
    print("Triangulation is still closed after petal resolution.")
else:
    print("Triangulation is not closed after petal resolution.")

try:
    hb.resolveGreedily()
    hb.fillHandlebody()
    print("Greedy resolution successful.")
    print("Triangulation size:", tri.size())
except Exception as e:
    print(f"Error during greedy resolution: {str(e)}")

print("\n--- Inspecting Internal State ---")
try:
    print("Internal state (check attributes or methods):", hb.__dict__)
except Exception as e:
    print(f"Error accessing internal state: {str(e)}")
