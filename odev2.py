__author__='ferhat cicek'
while True:
  print("bebek(1)")
  print("çocuk(2)")
  print("genç(3)")
  print("yaşlı(4)")
  print("----------")
  print
  secim = input("sizi tanımlayan kelimeyi seçin ...:")
  isim = input("İsminiz:")
  if secim=="1":
      print("bebek",isim)
      print
  elif secim=="2":
      print("çocuk",isim)
      print
  elif secim=="3":
      print("genç",isim)
      print
  elif secim=="4":
      print("yaşlı",isim)
      print
  else:
      print("geçersiz giriş.Program sonlandırılıyor ...")
      break