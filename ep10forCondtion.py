length=['hello','give','me','your','name']
for i in length:
    print(i,len(i))
    # print(len(i))
    
fees ={'Ankit':'paid','Rahul':'not paid','Ravi':'paid','Raj':'not paid'}

print("\nUnpaid students are:")
for fee, status in fees.copy().items():
    if status == 'not paid':
        print(fee)
        del fees[fee]
    # print(fee, status)
    # print(status)
print("\nPaid students are:")  
paid_fees = {}
for fee, status in fees.items():
    if status == 'paid':
        paid_fees[fee] = status
        print(fee, status)