print('-------------------------------------------------')
words = ['cat', 'window', 'lakjsdla']
for w in words:
    print(w, len(w))

print('-------------------------------------------------')
for w in words[:]:
    if len(w) > 3:
        words.insert(0, w)
print(words)

print('-------------------------------------------------')
for i in range(5, 15):
    print(i, end="# ")

print('-------------------------------------------------')
a = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(a)):
    print(i, a[i])

for i in range(10):
    print(i, end="# ")

print('-------------------------------------------------')
print(list(range(5)))