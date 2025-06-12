pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482

print(pi*7)

print(f'22 /7 = {22/7:.20f}') 

def find_best_devision(range_max=10):
    """
        Finds the best division of pi that is not a multiple of 7 and has the smallest reminder.
        The function iterates through numbers from 1 to range_max, calculating the division of pi by each number.
    """

    smallest_reminder = 0.9
    num_n, num_d = 1, 1

    for num in range(1, range_max + 1):
        n_tmp = pi * num

        if num / 7 == 0:
            # To avoid multiples of 7
            continue

        reminder_tmp = n_tmp - int(n_tmp) # Get the reminder of the division

        if reminder_tmp > (1-smallest_reminder):
            n_tmp = n_tmp + 1
            reminder_tmp = 1-(n_tmp - int(n_tmp))
            
        if reminder_tmp < smallest_reminder:
            smallest_reminder = reminder_tmp
            num_n = int(n_tmp)
            num_d = num

    print(f'pi * {num_d} = {pi * num_d:.20f}')
    print(f'smallest_reminder : {(smallest_reminder):.200f}')
    print(f'{num_n} / {num_d} = {(num_n/num_d):.20f}')

find_best_devision(10**7)
