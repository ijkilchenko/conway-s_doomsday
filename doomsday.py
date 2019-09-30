import datetime
import time
from datetime import timedelta
from random import randint

def get_random_date():
    start = datetime.datetime(1900, 1, 1)
    end = datetime.datetime.today()
    return start + timedelta(days=randint(0, int((end - start).days)))

num_to_month = {1: 'January', 2: 'February', 3: 'March',
                4: 'April', 5: 'May', 6: 'June',
                7: 'July', 8: 'August', 9: 'September',
                10: 'October', 11: 'November', 12: 'December'}

num_to_weekday = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                  4: 'Thursday', 5: 'Friday', 6: 'Saturday', 0: 'Sunday'}

if __name__ == '__main__':
    count = 0
    count_right = 0
    avg_time = 0
    while True:
        print()
        try:
            start = time.time()
            count += 1
            date = get_random_date()
            date_str = '%s %s %s' % (num_to_month[date.month], date.day, date.year)
            print('%s?' % date_str)
            guess_weekday = int(input())
            print('You guessed: %s' % num_to_weekday[guess_weekday])
            true_weekday = date.isoweekday() % 7
            if guess_weekday == true_weekday:
                print('Right!')
                count_right += 1
            else:
                print('Wrong!')
                print('%s is a %s. ' % (date_str, num_to_weekday[true_weekday]))
                doomsday = datetime.datetime(date.year, 3, 1) - timedelta(days=1)
                print('%s\'s doomsday was a %s.' % 
                    (date.year, num_to_weekday[doomsday.isoweekday()%7]))
            guess_time = time.time() - start
            avg_time = (avg_time*(count-1) + guess_time)/count
            print('Guessed %.2f%% correctly so far.' % (count_right/count*100))
            print('Average time to guess: %.2f seconds' % avg_time)

        except KeyboardInterrupt:
            break
