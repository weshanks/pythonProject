from faker import Faker

fake = Faker(locale = 'zh-CN')
# print('年月日：', fake.date(pattern = '%Y-%m-%d'))
# # print('随机一篇文章:',fake.text())
# print('随机密码:',fake.password())
print('人物名字:',fake.first_name()) # 名字

print('女性名字:',fake.first_name_female())

print('男性名字:',fake.first_name_male())

print('罗马文名字:',fake.first_romanized_name())

print('姓:',fake.last_name())

print('男性的姓:',fake.last_name_male())

print('女性的姓:',fake.last_name_female())

print('罗马文的性:',fake.last_romanized_name())

print('人物全名:',fake.name())

print('女性全名:',fake.name_female())

print('男性全名:',fake.name_male())

print('简略个人信息：', fake.simple_profile())

print('详细个人信息：', fake.profile())

print('生成身份证号:',fake.ssn())

print('生成手机号:',fake.phone_number())

print('生成手机号段：',fake.phonenumber_prefix())

print('完整信用卡信息：',fake.credit_card_full())

print('信用卡号：',fake.credit_card_number())

print("邮箱:", fake.email())




