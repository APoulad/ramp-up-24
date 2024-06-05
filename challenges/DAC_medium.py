def V_DAC(value):
    return round((value)*5/1023, 2)

print(V_DAC(1023))