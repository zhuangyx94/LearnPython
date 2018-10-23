# coding:utf-8
# 字典就像一个地址簿，只要知道名字就能找到地址，键与值相关联


db = {
    'swaroop': 'swaroop@gmail.com',
    'Larry': 'larry@gmail.com',
    'Mastumoto': 'mastumoto@gmail.com',
    'Spammer': 'spammer@gmail.com'
}


print("Swaroop's adddress is", db['swaroop'])


del db['Spammer']


print(len(db))


for name, address in db.items():
    print 'Contact {} at {}'.format(name, address)



