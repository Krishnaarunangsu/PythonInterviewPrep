x=220
y=int(220)
z=float(y/16)
list=str(z).split(".")
fraction_elem="."+list[1]
print(fraction_elem)
fraction_elem_int=float(fraction_elem)*16
print(int(fraction_elem_int))



decimal_hex_json={
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10:"A",
    11:"B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"

}
list_1=[]
hex_value_int=str(decimal_hex_json.get(int(list[0])))
print(hex_value_int)
list_1.append(hex_value_int)
hex_value_fraction=decimal_hex_json.get(fraction_elem_int)
print(hex_value_fraction)
hex_value_result=hex_value_int+hex_value_fraction
print(hex_value_result)
list_1.append(hex_value_fraction)
print(list_1)
hex_string=''.join(list_1)
print(hex_string)