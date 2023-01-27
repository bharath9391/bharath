class order:
    items=[]
    def __init__(self,id):
        self.id=id


    def add_item(self,item):
        self.items.append(item)


id1=order("bharath")
id2=order("chandu")
id1.add_item('books')
id2.add_item('phone')


print(id1.items,id2.items)
print(order.items)

print(help())


        
