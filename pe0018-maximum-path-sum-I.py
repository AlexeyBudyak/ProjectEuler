nums=[[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

def copy_tr(arr_original):
    arr = []
    for i in range(len(arr_original)):
        arr_temp = []
        for j in range(len(arr_original[i])):
            arr_temp.append(arr_original[i][j])
        arr.append(arr_temp)
    return arr

def count_max(pir):
    if len(pir) == 1:
        return pir[0][0]
    pir1 = copy_tr(pir)[1:]
    pir2 = copy_tr(pir)[1:]
    for i in range(len(pir1)):
        pir1[i].pop(0)
        pir2[i].pop(-1)
    return pir[0][0] + max(count_max(pir1), count_max(pir2))

print(count_max(nums))



