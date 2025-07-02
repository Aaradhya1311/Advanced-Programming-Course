person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

def smallest_average_result(per1, per2, per3):
    Avg_l = []
    per1_Avg = (per1["result1"] + per1["result2"] + per1["result3"])/3  
    per2_Avg = (per2["result1"] + per2["result2"] + per2["result3"]) /3
    per3_Avg = (per3["result1"] + per3["result2"] + per3["result3"]) /3
    Avg_l.append(per1_Avg)
    Avg_l.append(per2_Avg)
    Avg_l.append(per3_Avg)
    Avg_l.sort()

    if Avg_l[0] == per1_Avg:
        return per1
    elif Avg_l[0] == per2_Avg:
        return per2
    else:
        return per3

print(smallest_average_result(person1, person2, person3))