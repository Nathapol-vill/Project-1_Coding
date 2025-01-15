def acceleration(v , u , t):
  a = (v - u) / t
  #a คือ ความเร่ง
  #v คือ ความเร็วปลาย
  #u คือ ความเร็วต้น
  #t คือ เวลา
  print ("your acceleration is " , ' %.2f '  %a , "m/s²")


acceleration(25 , 5 , 5)
