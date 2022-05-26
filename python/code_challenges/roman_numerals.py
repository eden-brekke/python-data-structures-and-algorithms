def roman_to_arabic(roman_num):
    roman_keys = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }
    total = 0
    i = 0

    while i < len(roman_num):  # so long as i is not the equal to or greater than the length of the roman numeral

      if i + 1 < len(roman_num) and roman_num[i:i + 2] in roman_keys:
          # If we have characters left in the roman numeral arg, aaand if the substring exists within our keys dict

          total += roman_keys[roman_num[i:i + 2]]
          # then add the value of the key to the total
          i += 2
          # increment i to the next pair! We do this in pairs because of how roman numerals work.

      else:

          total += roman_keys[roman_num[i]]

          i += 1

    return total
