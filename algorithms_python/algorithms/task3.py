def SeatingStudents(arr):

  K = arr[0]
  occupied = arr[1:]

  rows = int(K/2)

  seats = []
  x = 0

  for i in range(rows):
    seats.append([])
    for j in range(2):
      if((x+1) in occupied):
        full_seat = True
      else:
        full_seat = False
      seats[i].append(str(full_seat))
      x+=1

  seating = 0
  for i in range(rows-1):
    if((seats[i][0] == str(False)) and (seats[i][1] == str(False))):
      seating+=1

    if((seats[i][0] == str(False)) and (seats[i+1][0] == str(False))):
      seating+=1

    if((seats[i][1] == str(False)) and (seats[i + 1][1] == str(False))):
      seating+=1

  if((seats[rows - 1][0] == str(False)) and (seats[rows - 1][1] == str(False))):
    seating+=1
  return seating


print(SeatingStudents([8,1,8]))
