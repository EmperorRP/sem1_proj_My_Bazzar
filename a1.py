

def show_menu():
    
    '''
	Description: Prints the menu as shown in the PDF
	Parameters: No paramters
	Returns: No return value
    '''
    
    print('''
=================================================
                   MY BAZAAR
=================================================
Hello! Welcome to my grocery store!
Following are the products available in the shop:

-------------------------------------------------
CODE | DESCRIPTION |   CATEGORY   | COST (Rs)
-------------------------------------------------
  0  | Tshirt      | Apparels     | 500
  1  | Trousers    | Apparels     | 600
  2  | Scarf       | Apparels     | 250
  3  | Smartphone  | Electronics  | 20,000
  4  | iPad        | Electronics  | 30,000
  5  | Laptop      | Electronics  | 50,000
  6  | Eggs        | Eatables     | 5
  7  | Chocolate   | Eatables     | 10
  8  | Juice       | Eatables     | 100
  9  | Milk        | Eatables     | 45
------------------------------------------------
''')



def get_regular_input():
    '''
	Description: Takes space separated item codes (only integers allowed). 
	Include appropriate print statements to match the output with the 
	screenshot provided in the PDF.
	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i. 
    '''
    print("Enter the item codes(space-separated):", end="")
    global itemCodes
    itemCodes=list(map(int, input().split()))
    quantities=[0,0,0,0,0,0,0,0,0,0]
    for i in itemCodes:
        if i<0:
            print("Invalid code: ", i)
            continue
        elif i==0:
            quantities[0]+=1
        elif i==1:
            quantities[1]+=1
        elif i==2:
            quantities[2]+=1
        elif i==3:
            quantities[3]+=1
        elif i==4:
            quantities[4]+=1
        elif i==5:
            quantities[5]+=1
        elif i==6:
            quantities[6]+=1
        elif i==7:
            quantities[7]+=1
        elif i==8:
            quantities[8]+=1
        elif i==9:
            quantities[9]+=1
    #print (quantities)
    return quantities
    
            


def get_bulk_input():
    
    '''
	Description: Takes inputs (only integers allowed) from a bulk buyer. 
	For details, refer PDF. Include appropriate print statements to match 
	the output with the screenshot provided in the PDF.
	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
    '''
    global itemCodes
    codes=[]
    global quantities
    quantities=[0,0,0,0,0,0,0,0,0,0]
    print("Enter the item codes(space-separated):", end="")
    flag1=0
    while flag1==0:
        x,y=map(int, input("Enter code and quantity(leave blank to stop)").split())
        if x==0:
            quantities[0]=y
            print("Added %i Tshirts" %(y))
        elif x==1:
            quantities[1]=y
            print("Added %i Trousers"  %(y))
        elif x==2:
            quantities[2]=y
            print("Added %i Scarf" %(y))
        elif x==3:
            quantities[3]=y
            print("Added %i Smartphones" %(y))
        elif x==4:
            quantities[4]=y
            print("Added %i iPad" %(y))
        elif x==5:
            quantities[5]=y
            print("Added %i Laptop" %(y))
        elif x==6:
            quantities[6]=y
            print("Added %i Eggs" %(y))
        elif x==7:
            quantities[7]=y
            print("Added %i Chocolate" %(y))
        elif x==8:
            quantities[8]=y
            print("Added %i Juice" %(y))
        elif x==9:
            quantities[9]=y
            print("Added %i Milk" %(y))
        elif x=="" and y=="":
            flag1=1
            print("Order complete")
        else:
            print("Invalid")

        return quantities
        


def print_order_details(quantities):
    '''
	Description: Prints the details of the order in a manner similar to the
	sample given in PDF.
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: No return value
    '''
    
    j=0

    
    for i in range(len(quantities)):
        if quantities[i]>0:
            if i==0:
                print("[%i] Tshirt * %i = Rs %i * %i = %i" %(j+1, quantities[i], 500, quantities[i], 500*quantities[i]))
                j+=1
            elif i==1:
                print("[%i] Trousers * %i = Rs %i * %i = %i" %(j+1, quantities[i], 600, quantities[i], 600*quantities[i]))
                j+=1
            elif i==2:
                print("[%i] Scarf * %i = Rs %i * %i = %i" %(j+1, quantities[i], 250, quantities[i], 250*quantities[i]))
                j+=1
            elif i==3:
                print("[%i] Smartphone * %i = Rs %i * %i = %i" %(j+1, quantities[i], 20000, quantities[i], 20000*quantities[i]))
                j+=1 
            elif i==4:
                print("[%i] iPad * %i = Rs %i * %i = %i" %(j+1, quantities[i], 30000, quantities[i], 30000*quantities[i]))
                j+=1
            elif i==5:
                print("[%i] Laptop * %i = Rs %i * %i = %i" %(j+1, quantities[i], 50000, quantities[i], 50000*quantities[i]))
                j+=1
            elif i==6:
                print("[%i] Eggs * %i = Rs %i * %i = %i" %(j+1, quantities[i], 5, quantities[i], 5*quantities[i]))
                j+=1
            elif i==7:
                print("[%i] Chocolate * %i = Rs %i * %i = %i" %(j+1, quantities[i], 10, quantities[i], 10*quantities[i]))
                j+=1
            elif i==8:
                print("[%i] Juice * %i = Rs %i * %i = %i" %(j+1, quantities[i], 100, quantities[i], 100*quantities[i]))
                j+=1
            elif i==9:
                print("[%i] Milk * %i = Rs %i * %i = %i" %(j+1, quantities[i], 45, quantities[i], 45*quantities[i]))
                j+=1
            else:
                print("Can't process this code")
                pass
        


    


def calculate_category_wise_cost(quantities):
    global apparels_cost
    global electronics_cost
    global eatables_cost

    apparels_cost=quantities[0]*500+quantities[1]*600+quantities[2]*250
    electronics_cost=quantities[3]*20000+quantities[4]*30000+quantities[5]*50000
    eatables_cost=quantities[6]*5+quantities[7]*10+quantities[8]*100+quantities[9]*45
    
    print ("Apparels = Rs ", int(apparels_cost))
    print ("Electronics = Rs ", int(electronics_cost))
    print ("Eatables = Rs ", int(eatables_cost))
    
    return (apparels_cost, electronics_cost, eatables_cost)
    '''
	Description: Calculates the category wise cost using the quantities
	provided. Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: A 3-tuple of integers in the following format: 
	(apparels_cost, electronics_cost, eatables_cost)
    '''

def get_discount(cost, discount_rate):
    
    '''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- discount_rate: Float: 0 <= discount_rate <= 1

	Returns: The discount on the cost provided.
    '''
    return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):    
    '''
	Description: Calculates the discounted category-wise price, if applicable. 
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables'
	
	Returns: A 3-tuple of integers in the following format: 
	(discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost). 
    '''
    global discounted_apparels_cost
    global discounted_electronics_cost
    global discounted_eatables_cost
    if apparels_cost>=2000:
        discount_rate = 0.1
    else:
        discount_rate = 0
    discounted_apparels_cost=apparels_cost - (get_discount(apparels_cost, discount_rate))
    

    if electronics_cost>=25000:
        discount_rate = 0.1
    else:
        discount_rate = 0
    discounted_electronics_cost=electronics_cost - (get_discount(electronics_cost, discount_rate))
    

    if eatables_cost>=2000:
        discount_rate = 0.1
    else:
        discount_rate = 0
    discounted_eatables_cost=eatables_cost - (get_discount(eatables_cost, discount_rate))
    
    
    return (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost)


def get_tax(cost, tax):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- tax: 	Float: 0 <= tax <= 1

	Returns: The tax on the cost provided.
	'''
	return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    
    '''
	Description: Calculates the total cost including taxes.
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables' 
	
	Returns: A 2-tuple of integers in the following format: 
	(total_cost_including_tax, total_tax)
    '''
    total_cost_including_tax=0
    total_tax=0
    
    total_tax+=apparels_cost*0.10
    total_cost_including_tax+=apparels_cost+(apparels_cost*0.10)
    
    total_tax+=electronics_cost*0.15
    total_cost_including_tax+=electronics_cost+(electronics_cost*0.15)

    total_tax+=eatables_cost*0.05
    total_cost_including_tax+=eatables_cost+(eatables_cost*0.05)


    print("[APPAREL] Rs %i * Rs 0.10 = Rs %i" %(discounted_apparels_cost, get_tax(discounted_apparels_cost, 0.10)))
    print("[ELECTRONICS] Rs %i * Rs 0.15 = Rs %i" %(discounted_electronics_cost, get_tax(discounted_electronics_cost, 0.15)))
    print("[EATABLES] Rs %i * Rs 0.05 = Rs %i" %(discounted_eatables_cost, get_tax(discounted_eatables_cost, 0.05 )))
    print("\nTOTAL TAX = Rs ", int(total_tax))
    print("TOTAL COST = Rs ", int(total_cost_including_tax))
    
    global total_cost
    total_cost=total_cost_including_tax
    return (total_cost_including_tax, total_tax)


def apply_coupon_code(total_cost):
    
    '''
    Description: Takes the coupon code from the user as input (case-sensitive). 
    For details, refer the PDF. Include appropriate print statements to match 
    the output with the screenshot provided in the PDF.
    
    Parameters: The total cost (integer) on which the coupon is to be applied.
    
    Returns: A 2-tuple of integers:
    (total_cost_after_coupon_discount, total_coupon_discount)
    '''
    flag=0
    global total_coupon_discount
    total_coupon_discount=0
    global couponCode
    couponCode=input("Enter coupon code (else leave blank): ")
    while flag==0:
        if couponCode=="HELLE25":
            if total_cost>25000:
                total_coupon_discount=min(5000, total_cost*0.25)
                print("[HELLE25]min(10000, total_cost*0.50)= Rs",total_coupon_discount)
                flag=1
            else:
                total_coupon_discount=0
                print("\nCoupon not applied because amount lower than 25000")
                flag=1
        elif couponCode =="CHILL50":
            if total_cost>50000:
                total_coupon_discount=min(10000, total_cost*0.50)
                print("[CHILL50]min(10000, total_cost*0.50)= Rs",total_coupon_discount)
                flag=1
            else:
                total_coupon_discount=0
                print("\nCoupon not applied because amount lower than 50000")
                flag=1
        elif couponCode=="":
            print("No coupon code applied")
            flag=1
        else:
            print("Invalid coupon code, please try again")
            flag=1
            
    total_cost_after_coupon_discount=total_cost - total_coupon_discount
    print("\nTOTAL COUPON DISCOUNT",total_coupon_discount)
    print("TOTAL COST",total_cost_after_coupon_discount)
    return(total_cost_after_coupon_discount, total_coupon_discount)
        

        


def main():
    
    show_menu()
    x=input("Would you like to buy in bulk? (y or Y / n or N): ")
    if x=="n" or x == "N":
        quantities=get_regular_input()
    elif x=="y" or x == "Y":
        quantities=get_bulk_input()
    print('''-------------------------------------------------
ORDER DETAILS
-------------------------------------------------''')
    print_order_details(quantities)       
    print('''-------------------------------------------------
CATEGORY-WISE COST
-------------------------------------------------''')
    calculate_category_wise_cost(quantities)
    
    print('''-------------------------------------------------
DISCOUNTS
-------------------------------------------------''')
    if apparels_cost>=2000:
        discount_rate = 0.1
    else:
        discount_rate = 0
    print("[APPAREL] Rs %i - Rs %i = Rs %i" %(apparels_cost, get_discount(apparels_cost, discount_rate),calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost)[0]))
    if electronics_cost>=25000:
        discount_rate = 0.1
    else:
        discount_rate = 0
    print("[ELECTRONICS] Rs %i - Rs %i = Rs %i" %(electronics_cost,get_discount(electronics_cost, discount_rate),calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost)[1]))
    if eatables_cost>=2000:
        discount_rate = 0.1
    else:
        discount_rate = 0
    print("[EATABLES] Rs %i - Rs %i = Rs %i" %(eatables_cost, get_discount(eatables_cost, discount_rate), calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost)[2]))
    print('''-------------------------------------------------
TAX
-------------------------------------------------''')
    calculate_tax(discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost)
    
    print('''-------------------------------------------------
COUPON CODE
-------------------------------------------------''')
    
    apply_coupon_code(total_cost)
    print("\nThank you for visiting")


            

if __name__ == '__main__':
    main()
