def solution(number):
    return sum([y for y in range(number) if y % 3 == 0 or y % 5 == 0 ])
    
  