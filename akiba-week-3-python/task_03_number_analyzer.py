def is_prime(number):
    if number<1:
        return f"NOT PRIME (Number can't be bellow 1)"
    for i in range(2, number):
        if number%i==0:
            return f"NOT PRIME"

    return f"PRIME"



def get_divisors(number):
    
    if number == 0 or number < 0:
        return "divisors are undefined for zero"
    
    divisors=[]

    for i in range(1,number + 1):
        if number % i == 0:              
            divisors.append(i)
    
    return divisors


def sum_of_digits(number):
    
    if number < 0:
        number = -number

    total = 0
    while number > 0:

        digit = number % 10    
        total += digit        
        number = number // 10 

    return total


        
def reverse_number(number):
      
      num_reversed=0
      while number > 0:
          last_digit=number % 10       

      
          num_reversed=num_reversed *10 +last_digit     

    
          number=number // 10     

      return num_reversed                     

     

def analyze_number(number):
    if number % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    return {
         "number": number,
        "even or odd": parity,
        "prime": is_prime(number),
    
        f"The sum of digits of {number} is": sum_of_digits(number),
        f"The divisors of {number} are": get_divisors(number),
        f"The reversed number of {number} is": reverse_number(number)
    }


