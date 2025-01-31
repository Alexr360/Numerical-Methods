temperature = input("What is the temperature you would like to convert?\n").lower() + "|"

if (any(sub in temperature for sub in ["f|","c|","r|","k|","fahrenheit|","celcius|","rankine|","kelvin|"])):

    temperatureNumber = float(''.join(i for i in temperature if i.isdigit() or i == '.'))
    
    if "f" in temperature:
        fahrenheit = temperatureNumber
    elif "r" in temperature:
        fahrenheit = temperatureNumber - 459.67
    elif "c" in temperature:
        fahrenheit = temperatureNumber * 9 / 5 + 32
    elif "k" in temperature:
        fahrenheit = (temperatureNumber - 273.15) * 9 / 5 + 32

    rankine     = round(fahrenheit + 459.67         , 3)
    celcius     = round((fahrenheit - 32) * (5/9)   , 3)
    kelvin      = round(celcius + 273.15            , 3)
    fahrenheit  = round(fahrenheit                  , 3)

    print(f"Converted Units:\n Fahrenheit: {fahrenheit}\n Rankine  {rankine}\n Celcius  {celcius}\n Kelvin  {kelvin}")
    
else:
    print("Invalid Input Please Try Again.")