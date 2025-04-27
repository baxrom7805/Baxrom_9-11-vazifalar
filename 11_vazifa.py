#1-topshiriq

# son = int(input('Juft son kiriting >>>'))
# if son%2:
#     print('Bu son juft emas')
# else:
#     print('Rahmat')


# 2-topshiriq

# yosh = int(input('Yoshingiz nechchida? >>>'))
# if 4<=yosh<18:
#     print("Kirish bileti 10.000 so'm")
# elif 18<=yosh<60:
#     print("Kirish bileti 20.000 so'm")
# else:
#     print('Kirish tekin')


# 3-topshiriq

# son_1 = float(input("Birinchi sonni kiriting >>>"))
# son_2 = float(input("Ikkinchi sonni kiriting >>>"))
# if son_1 > son_2:
#     print(f"{son_1} > {son_2}")
# elif son_1 < son_2:
#     print(f"{son_1} < {son_2}")
# else:
#     print(f"{son_1} = {son_2}")


# 4-topshiriq

# mahsulotlar = ['shakar', 'un', 'tuz', 'guruch', "yog'", "mosh", "kartoshka", "sabzi", "piyoz", "sholg'om"]
# savat = []
# savat.append(input("Savatga 1-mahsulotni qo'shing >>>"))
# savat.append(input("Savatga 2-mahsulotni qo'shing >>>"))
# savat.append(input("Savatga 3-mahsulotni qo'shing >>>"))
# savat.append(input("Savatga 4-mahsulotni qo'shing >>>"))
# savat.append(input("Savatga 5-mahsulotni qo'shing >>>"))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")


# 5-topshiriq

# mahsulotlar = ['shakar', 'un', 'tuz', 'guruch', "yog'", "mosh", "kartoshka", "sabzi", "piyoz", "sholg'om"]
# savat = []
# bor_mahsulot = []
# yoq_mahsulot = []
# savat.append(input("Savatga 1-mahsulotni qo'shing >>>"))
# savat.append(input("Savatga 2-mahsulotni qo'shing >>>"))
# savat.append(input("Savatga 3-mahsulotni qo'shing >>>"))
# savat.append(input("Savatga 4-mahsulotni qo'shing >>>"))
# savat.append(input("Savatga 5-mahsulotni qo'shing >>>"))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulot.append(mahsulot)
#     else:
#         yoq_mahsulot.append(mahsulot)
# if yoq_mahsulot:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in yoq_mahsulot:
#     print(mahsulot)
# else:
#   print("Barcha mahsulotlar do'konimizda bor")


# 6-topshiriq

# foydalanuvchilar = ["admin", "user", "ali", "vali", "sobir"]
# foydalanuvchi = input("Yangi login kiriting>>>")
# if foydalanuvchi in foydalanuvchilar:
#     print("Login band, yangi login kiriting")
# else:
#     print(f"Xush kelibsiz {foydalanuvchi}!")


# 7-topshiriq

butun_son = float(input("Butun son kiriting>>>"))
boluvchi = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for k in boluvchi:
    if not(butun_son%k):
        print(f"{butun_son} soni {k} ga qoldiqsiz bo'linadi")



