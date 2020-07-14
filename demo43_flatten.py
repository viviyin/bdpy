def list_by_order(var1, var2, var3):
    print(f"first={var1}, second={var2}, third={var3}")


list_by_order("apple", 'banana', 'citron')
list_by_order("apple", *['banana', 'citron'])
list_by_order(*['banana', 'citron'], "apple")
# list_by_order(*['banana', 'citron'])
s1 = {'Apple', 'Banana', 'Citron'}
list_by_order(*s1)
d1 = {'Apple': 100, 'Banana': 50, 'Citron': 40}
list_by_order(*d1)
