def prom(list1):
    list2 = []
    for avg in list1:
        if avg < 6:
            list2.append("reprobate")
        elif avg <= 6.4:
            list2.append("approved with 6")
        elif avg <= 7.4:
            list2.append("approved with 7")
        elif avg <= 8.4:
            list2.append("approved with 8")
        elif avg <= 9.4:
            list2.append("approved with 9")
        else:
            list2.append("approved with 10")
    return list2


list_students = [9, 5.4, 10, 3.2, 5.6, 8.7, 6.4, 8.4]
print(prom(list_students))