import hash_table

h=hash_table.HashTable()
h[54]="cat"
h[26]="dog"
h[93]="lion"
h[17]="tiger"
h[77]="bird"
h[31]="cow"
h[44]="goat"
h[55]="pig"
h[20]="chicken"
print(h.slots)
print(h.data)
print(h[20])
print(h[17])
h[20]='duck'
print(h[20])
print(h.data)
print(h[99])
