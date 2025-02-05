def ConvertTemperature(temperature:str):
    temperature = temperature.lower() + "|"
    if (any(sub in temperature for sub in ["f|","c|","r|","k|","fahrenheit|","celcius|","rankine|","kelvin|"])):

        temperatureNumber = float(''.join(i for i in temperature if i.isdigit() or i == '.' or i == '-'))
        
        if "f" in temperature:
            fahrenheit = temperatureNumber
        elif "r" in temperature:
            fahrenheit = temperatureNumber - 459.67
        elif "c" in temperature:
            fahrenheit = temperatureNumber * 9 / 5 + 32
        elif "k" in temperature:
            fahrenheit = (temperatureNumber - 273.15) * 9 / 5 + 32

        rankine     = fahrenheit + 459.67
        celcius     = (fahrenheit - 32) * (5/9)
        kelvin      = celcius + 273.15
        fahrenheit  = fahrenheit

        return rankine, celcius, kelvin, fahrenheit