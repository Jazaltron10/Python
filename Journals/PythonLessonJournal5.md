# The Jazaltron Learning Journal
## This is the Fifth LessonJournal in the Python series 
#### Here we'll basically be building a count down app 


+ user inputs are always interpreted as strings 
+ datetime.datetime 
+ the first is a module and the second is a definition inside the module 
+ The second is basically a container of functions and variables inside the first


###### Third Party Packages
+ Python comes only with a set of built-in modules
+ Many more modules out there, which are NOT part of the python installation
+ You need to install these third-party packages 
+ python modules live in a python repository called **pypi** 

###### Package vs Module 
+ Module is basically a single python file 
+ Package is a collection of Python modules 
+ a package always contains an __init__.py file 
+ this is to differentiate it from all the normal 
  folders that contain multiple python files
+ Packages is a good  way to define a structure and hierarchy for your modules 
  and kind of group them together
  
####### Library 
This is just basically a collection of python packages   
###### The Python Package Index(PyPI)
+ PuPI is a repo(storage) for third-party Python packages
+ People can Publish their packages to this repo
+ So it becomes available for everyone to use
+ A large community means, many people are creating useful modules and make them
  available for others
  
  
###### pip 
+ This is a package manager tool just like npm for js or maven/gradle for java
+ It is used to install packages from the Python Package Index, but also other indexes 
+ pip is included in the installation of python
+ you can install and uninstall packages like django using pip
            
            
             pip install Django
             pip uninstall Django
            
###### Automation with Python 
objectives
+ List each company with respective product count 
+ List products with inventory less than 10
+ List each company with respective total inventory value 
+ Write to Spreadsheet: Calculate and write inventory value for each product 
  into spreadsheet 
+ openpyxl should be installed using pip 

###### List each company with respective product count
+ For this exercise 
+ We need to go through each and ever row in each sheet 
+ We also need to execute the same logic for specific columns on each row
+ Thus we'll have to loop through the rows 
+ This loop will execute as many times as the number of products in the sheet 
+ That just simply means the number of rows in the sheet 

#####openpyxl
+ max_row - is the maximum row index containing data(1-based)
+ max_column - is the maximum column index containing data (1-based)
+ You can't just put a number in your for loop as the loop limit
+ This is is because the for loop is for iterating over a list and to achieve this 
+ we use a range() which takes in two parameters: start-point and end-point
+ The range creates a list to iterate through 
+ Thus a range of 75 will create a list of [0,1,2,3,4.......74]
+ The range is zero indexed by default unless you provide the start index
+ Also the second parameter in the range is exclusive
+ this means that for a range of 75 with start point of 2 
+ The range will execute from 2 to 74
+ to make it inclusive all you have to do is to add add 1 
+ product_list.cell()- takes in two values row_no. and col_no.
 

###### Sample Code 
          
          
          from openpyxl import Workbook
          wb = Workbook()

          # grab the active worksheet
          ws = wb.active

          # Data can be assigned directly to cells
          ws['A1'] = 42

          # Rows can also be appended
          ws.append([1, 2, 3])

          # Python types will automatically be converted
          import datetime
          ws['A2'] = datetime.datetime.now()

          # Save the file
          wb.save("sample.xlsx")



######## Code
    import openpyxl

    inv_file = openpyxl.load_workbook("FANG.xlsx")
    product_list =  inv_file["Sheet1"]


    # Name of company will be key and the product count will be the value
    products_per_supplier = {} # Exercise 1
    total_value_per_supplier = {}



    for product_row in range(2, product_list.max_row + 1):
        supplier_name = product_list.cell(product_row, 4).value
        inventory = product_list.cell(product_row, 2). value
        price = product_list.cell(product_row, 3).value
        currency = product_list.cell(product_row, 5).value

        # Calculation for number of products per supplier
        if supplier_name in products_per_supplier:
            current_num_products = products_per_supplier.get(supplier_name)
            products_per_supplier[supplier_name] = current_num_products + 1
        else:
            products_per_supplier[supplier_name] = 1

        # calculation of total value of inventory per supplier
        if supplier_name in total_value_per_supplier:
            # current_total_value = total_value_per_supplier[supplier_name]
            # final_value = current_total_value + inventory * price

            # total_value_per_supplier[supplier_name] = current_total_value + inventory * price
            total_value_per_supplier[supplier_name] += inventory * price
            # total_value_per_supplier[supplier_name] = final_value
            # print(f"${main_value}")
        else:
            total_value_per_supplier[supplier_name] = inventory * price
            # print(total_value_per_supplier)



    #print(f"The total amount of products per supplier -> {products_per_supplier}")
    print(f"The total value for each  supplier is : {total_value_per_supplier}")


###### Exercise 3 
Printing out all the products that have inventory less than 10
###### Exercise 4
Adding values to the spreadsheet 

###### Final Code 


    import openpyxl

    inv_file = openpyxl.load_workbook("FANG.xlsx")
    product_list =  inv_file["Sheet1"]


    # Name of company will be key and the product count will be the value
    products_per_supplier = {} # Exercise 1
    total_value_per_supplier = {}
    products_under_10_inv = {}


    for product_row in range(2, product_list.max_row + 1):
        supplier_name = product_list.cell(product_row, 4).value
        inventory = product_list.cell(product_row, 2).value
        price = product_list.cell(product_row, 3).value
        product_num = product_list.cell(product_row, 1).value
        inventory_price = product_list.cell(product_row, 5)

        # Calculation for number of products per supplier
        if supplier_name in products_per_supplier:
            # current_num_products = products_per_supplier.get(supplier_name)
            # products_per_supplier[supplier_name] = current_num_products + 1
            products_per_supplier[supplier_name] += 1
        else:
            products_per_supplier[supplier_name] = 1

        # calculation of total value of inventory per supplier
        if supplier_name in total_value_per_supplier:
            # current_total_value = total_value_per_supplier[supplier_name]
            # total_value_per_supplier[supplier_name] = current_total_value + inventory * price

            total_value_per_supplier[supplier_name] += inventory * price
        else:
            total_value_per_supplier[supplier_name] = inventory * price

        # Logic products with inventory less than 10
        if inventory < 10:
            products_under_10_inv[int(product_num)] = int(inventory)



        # Add value for total inventory price
        inventory_price.value = inventory * price




    print(f"The total amount of products per supplier -> {products_per_supplier}")
    print(f"The total value for each  supplier is : {total_value_per_supplier}")
    print(products_under_10_inv)
    inv_file .save("Inventory_with_total_value.xlsx")















