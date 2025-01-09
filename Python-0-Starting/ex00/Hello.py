ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# list : 추가 삭제 모두 가능
ft_list[1] = "World!"

# tuple : 추가 삭제 불가능
ft_tuple = ("Hello", "Korea!")

# set : 추가 삭제 모두 가능, 순서가 없어서 출력은 랜덤
ft_set.remove("tutu!")
ft_set.add("Seoul!")

# dict : 추가 제거 모두 가능, key값으로 value 값 수정
ft_dict["Hello"] = "42Seoul!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)