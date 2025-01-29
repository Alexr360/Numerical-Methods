temperature = input("What is the temperature you would like to convert?\n").lower()

if "f" in temperature or "fahrenheit" in temperature:
    fahrenheit = str(round(float(temperature.replace("f",""))                         , 3))
elif "r" in temperature or "rankine" in temperature:
    fahrenheit = str(round(float(temperature.replace("r","")) - 459.67                , 3))
elif "c" in temperature or "celcius" in temperature:
    fahrenheit = str(round(float(temperature.replace("c","")) * (9/5) + 32            , 3))
elif "k" in temperature or "kelvin" in temperature:
    fahrenheit = str(round((float(temperature.replace("k","")) - 273.15) * (9/5) + 32 , 3))

rankine = str(round(float(fahrenheit) + 459.67          , 3))
celcius = str(round((float(fahrenheit) - 32) * (5/9)    , 3))
kelvin  = str(round((float(celcius) + 273.15)           , 3))

print("Converted Units:\n Fahrenheit: " + fahrenheit + "\n Rankine  " + rankine + "\n Celcius  " + celcius + "\n Kelvin  " + kelvin + "")