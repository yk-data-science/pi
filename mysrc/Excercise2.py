from config import PI

print(PI*7)
print(f'22 /7 = {22/7:.20f}') 

def find_best_devision(range_max=10):
    """
        Finds the best division of PI that is not a multiple of 7 and has the smallest reminder.
        The function iterates through numbers from 1 to range_max, calculating the division of PI by each number.
    """

    smallest_reminder = 0.9
    num_n, num_d = 1, 1

    for num in range(1, range_max + 1):
        n_tmp = PI * num

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

    print(f'PI * {num_d} = {PI * num_d:.20f}')
    print(f'smallest_reminder : {(smallest_reminder):.200f}')
    print(f'{num_n} / {num_d} = {(num_n/num_d):.20f}')

find_best_devision(10**7)
