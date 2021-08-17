cc = int(input("engine capacity? "))
print("engine capacity is ",cc)
if cc <= 1000:
    print("road tax is ",20)
elif cc <= 1200:
    print("road tax is",55)
elif cc <= 1400:
    print("road tax is",70)
elif cc <= 1600:
    print("road tax is",90)
elif cc <= 1600:
    print("road tax is",90)
elif cc <= 1800:
    print("road tax is",200+(.4*(cc-1600)))
elif cc <= 2000:
    print("road tax is",280+(.5*(cc-1800)))
elif cc <= 2500:
    print("road tax is",380+(1*(cc-2000)))
elif cc <= 3000:
    print("road tax is",880+(2.5*(cc-2500)))
else:
    print("road tax is ",2130+(4.5*(cc-3000)))
    