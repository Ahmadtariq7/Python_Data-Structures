#   Set: Collection of elements which are unordered and no duplication
#   Set elements must be immutable

# Call set constructor and give it anything on which iteration is possible

x = set(['foo', 'bar', 'foo', 'baz', 'qux'])
print(x)

# for strings (iterable)
s = 'quux'
s = set(s)
print(s)

x = {'foo', 'bar', 'qux'}
print(x)

print('foo' in x)
print('temp' in x)

# Union of sets
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

print("The union of x1 and x2 is: ", x1 | x2)
print("The union of x1 and x2 is: ", x1.union(x2))  # alternative

print("The intersection is: ", x1.intersection(x2))
print("The difference is: ", x1.difference(x2))  # Stuff that is in x1, but not in x2
print("The disjoint is: ", x1.isdisjoint(x2))

a = {1, 2, 3, 4}
b = {5, 6, 7, 8}
print("A and B are disjoint: ", a.isdisjoint(b))

a = {1, 2}
b = {1, 2, 3, 4, 5}
c = {1, 2}

print("A is subset of B: ", a.issubset(b))
print("A is subset of C: ", a.issubset(c))
print("B is subset of C: ", b.issubset(c))

print("A is proper Subset of C: ", a < c)  # Proper Subset? = A is subset of C but is not equal..
print("A is subset of C: ", a <= c)  # Alternative of subset

a = {1, 2, 3}

# we can update values
a.update([5])
print(a)

# we can remove values
a.remove(1)
print(a)

print("::::::::::::::::   All and Any   ::::::::::::::::::::::\n")

a = 5
b = 4

# if a>2 and a<10 and b>0 and b<5:
#     print("All constrained Satisfied")

constraints = {a > 2, a < 10, b > 0, b < 5}
if all(constraints):
    print("All constrained Satisfied")
if any(constraints):
    print("At least one constrained Satisfied")

print(":::::: Quantifiers Example  :::::::\n")

X = {10, 20, 30, 40, 50}

print(all([x < 100 for x in X]))  # Same as "for all/each"
print(any([x < 50 for x in X]))  # Same as "there exist"


#  You can also have an arbitrary function computed in this scope
def is_div_by_20(n):
    return n % 20 == 0


print(all([is_div_by_20(x) for x in X]))
print(any([is_div_by_20(x) for x in X]))

print("::::::::::::::::   Counter   ::::::::::::::::::::::\n")

from collections import Counter

cnt = Counter()

for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1

print(cnt)
print(cnt['red'])  # we can count and get value..
print(cnt['orange'])  # zero output

print(cnt.most_common(2))  # tells common among list. gives ordered list of tuple and ordered on num we give..
print(cnt.most_common(2)[0][0])

sentence = """A wonderful serenity has taken possession of my entire soul,
              like these sweet mornings of spring which I enjoy with my whole heart.
              I am alone, and feel the charm of existence in this spot, which 
              was created for the bliss of souls like mine. I am so happy"""

for word in sentence.split():
    cnt[word] += 1

print(cnt.most_common())
