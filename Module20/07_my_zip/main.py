def new_zip(obj_a, obj_b):
    obj_a, obj_b = list(obj_a), list(obj_b)
    return ((obj_a[i], obj_b[i]) for i in range(min(len(obj_a), len(obj_b))))


object_a = 'abcd'
object_b = [10, 20, 30, 40]

print(new_zip(object_a, object_b))
for j in new_zip(object_a, object_b):
    print(j)
