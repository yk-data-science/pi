from config import PI

dev_22_7 = 22 / 7
print(f'22 / 7 = {dev_22_7:.20f}')
print(f'PI = {PI:.20f}')

def find_decimal_places(value, precision=20):
    """
    Finds the number of decimal places in a given value up to a specified precision.
    """

    # Convert to string with specified precision
    decimal_str = f"{value:.{precision}f}"[2:]  # Skip "0."
    
    count = 0
    for ch in decimal_str:
        if ch == '0':
            count += 1
        else:
            break
    return count

diff = abs(PI - dev_22_7)
zeros = find_decimal_places(diff)

print(f'Difference: {diff:.30f}')
print(f'Leading zeros after decimal: {zeros}')