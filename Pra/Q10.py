Car_detail = {"Name":"BMW","Model":"X1","Price":3950000}

    # a
Car_detail.update({"Location":"Noida"})
    # b
Car_detail["Price"] = "4000000"
    # c
print(Car_detail["Model"])
    # d
print(Car_detail.keys())
print(Car_detail.values())