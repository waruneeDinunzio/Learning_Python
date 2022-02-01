def add_time(start, duration, day_of_week=False):
  days_of_the_week_index = {"monday":0, "tuesday":1,"wednesday":2, "thursday":3, "friday":4, "saturday":5, "sunday":6}
  days_of_the_week_array = ["Monday", "Tuesday","Wednesday", "Thursday", "Friday","Saturday","Sunday"]

  start_time = start.partition(":")
  start_minute_tuple = start_time[2].partition(" ")
  minute_start = int(start_minute_tuple[0])
  hour_start = int(start_time[0])
  #print(hour_start,minute_start)

  durations = duration.partition(":")
  add_hours = int(durations[0])
  add_minutes = int(durations[2])
  #print(add_hours,add_minutes)

  am_pm = start_minute_tuple[2]
  #print(am_pm)
  am_pm_flip = {"AM":"PM","PM":"AM"}
  #print(am_pm_flip[am_pm])

  amount_of_days = int(add_hours/24)

  end_minutes = minute_start + add_minutes
  if (end_minutes >= 60):
    hour_start +=1
    end_minutes = end_minutes % 60
  amount_flips = int((hour_start +add_hours) /12)
  end_hours = (hour_start+add_hours) % 12
  #print(amount_flips)

  end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes)
  # if end_hours == 0, chang end_hours = 12
  end_hours = end_hours = 12 if end_hours == 0 else end_hours

  if(am_pm == "PM" and hour_start + (add_hours%12) >=12):
    amount_of_days += 1

  am_pm = am_pm_flip[am_pm] if amount_flips % 2 == 1 else am_pm
  
  returnTime = str(end_hours) + ":" + str(end_minutes) + " " + am_pm
  if(day_of_week):
    day_of_week = day_of_week.lower()
    index = int((days_of_the_week_index[day_of_week]) + amount_of_days)% 7
    new_day = days_of_the_week_array[index]
    returnTime += ", " + new_day

  if(amount_of_days == 1):
    return returnTime + " " + "(next day)"
  elif(amount_of_days > 1):
    return returnTime + " (" + str(amount_of_days) + " days later)"

  return returnTime
