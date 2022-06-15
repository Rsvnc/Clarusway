#Get two dates from the user in the format "30.10.2020" and find the "number of days" between these dates.
 # Rules:
 # * "import" cannot be used.
 # * "def" can be used.
 # * Each month will be evaluated in its own number of days. (Jan:31, Feb:28, Mar: 31, ...)
 # * The result is 1 day tolerance. (Due to February, the result may be "1 day less/more".)
  
 str_date1 = input('Date-1 (DD.MM.YYYY): ')
 str_date2 = input('Date-2 (DD.MM.YYYY): ')
 def date_to_int(date):
  months = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
  day, month, year = date.split('.')
  sum_day = int(day)
  sum_day += sum(months[:int(month)])
  return (int(year), sum_day)

date1 = date_to_int(str_date1)
date2 = date_to_int(str_date2)

total_day = int((date1[0]-date2[0])*365.25)
total_day += (date1[1]-date2[1])




