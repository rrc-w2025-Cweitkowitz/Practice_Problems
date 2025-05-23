
def factorialn(factor: int):
    counter = 1
    factor_intial = factor 
    
    for counter in range(1, factor):
        print(f"C{counter}")
        print(f"N!{factor}")
        factor_intial *= counter        
        counter += 1
        if counter == factor:
            return print(factor_intial)

factorialn(5)
