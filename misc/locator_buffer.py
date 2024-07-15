from core.locator import Locator 

for i in range(1000):
    locations = Locator.locate("2024-JULY", ref_id="b:501708050")
    print(i)

print(locations)