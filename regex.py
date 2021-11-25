import re
import pdfreader

x = 0
while(x<10):
    myPDF = pdfreader.pdf_array[x]
    x += 1

def find_clientName(pdf): # finds client name
    try:
        client_name = re.findall("ClientName:.{1,9}", pdf)
        return client_name[0].replace('ClientName:','')
    except:
        print("find_clientName: An exception occurred")

def find_subTotal(pdf): # finds sub total
    try: # try catch block
        subtotal = re.findall("SUBTOTAL.{1,9}", pdf)
        return int(re.search(r'\d+', subtotal[0]).group())
    except:
        print("find_subTotal: An exception occurred")
    
def find_discount(pdf): # finds discount
    try: # try catch block
        discount = re.findall("DISCOUNT.{1,9}", pdf)
        return (-int(re.search(r'\d+', discount[0]).group()))   
    except:
        print("find_discount: An exception occurred")

def find_tax(pdf): # finds tax
    try: # try catch block
        tax = re.findall("TAX.{1,9}", pdf)
        return int(re.search(r'\d+', tax[1]).group())
    except:
        print("find_tax: An exception occurred")

def find_taxRate(pdf): # finds tax rate
    try: # try catch block
        tax_rate = re.findall("TAX RATE.{1,9}", pdf)     
        return int(re.search(r'\d+', tax_rate[0]).group()) 
    except:
        print("find_taxRate: An exception occurred")
          
def find_invoiceTotal(pdf): # finds invoice total
    try: # try catch block
        invoice_total = re.findall("\$\d+", pdf)
        return int(re.search(r'\d+', invoice_total[-1]).group())  
    except:
        print("find_invoiceTotal: An exception occurred")

def find_zipCode(pdf): # finds zip code
    try:
        zip_code = re.findall("ZIPCode:.{1,6}", pdf)
        return int(re.search(r'\d+', zip_code[0]).group())   
    except:
        print("find_zipCode: An exception occurred")

def find_mail(pdf): # finds mail
    try:
        mail = re.findall("[a-z-0-9]*@gmail.com", pdf)
        return mail[0]
    except:
        print("find_mail: An exception occurred")

def find_domain(pdf): # finds domain
    try:
        domain = re.findall("[a-z-0-9]*.com", pdf)
        return domain[-1]
    except:
        print("find_domain: An exception occurred")

def find_phoneNumber(pdf): # finds phone number
    try:
        phone_number = re.findall("(\d[-\.\s]??\d{3}[-\.\s]??\d{4})", pdf)
        return phone_number[0]
    except:
        print("find_phoneNumber: An exception occurred")

def find_acountHolder(pdf): # finds account holder
    try:
        account_holder = re.findall("Accountholder:.{1,15}", pdf)
        return account_holder[0].replace('Accountholder:','')
    except:
        print("find_acountHolder: An exception occurred")

def find_companyName(pdf): # finds company name
    try:
        company_name = re.findall("[a-zA-Z]{1,39}",pdf)
        return company_name[0]
    except:
        print("find_companyName: An exception occurred")

def find_allValues(pdf):
    """
    print("client name: ",find_clientName(pdf))
    print("sub total: ",find_subTotal(pdf))
    print("discount: ", find_discount(pdf))
    print("tax: ", find_tax(pdf))   
    print("tax rate:", find_taxRate(pdf)) 
    print("invoice total: ", find_invoiceTotal(pdf)) 
    print("zip code: ", find_zipCode(pdf))
    print("mail: ", find_mail(pdf))
    print("domain: ", find_domain(pdf))
    print("phone number: ", find_phoneNumber(pdf))
    print("acount holder: ", find_acountHolder(pdf))
    print("company name:", find_companyName(pdf))
        """

# finds all company names
def find_allCompanyName():
    try:
        companyNames = []
        j = 0
        while(j<10):
            temp_pdf = pdfreader.pdf_array[j]
            companyNames.append(find_companyName(temp_pdf))
            j += 1
        return companyNames
    except:
        print("find_allCompanyName: Error")

# finds all clients names
def find_allClientName():
    try:
        clientNames = []
        j = 0
        while(j<10):
            temp_pdf = pdfreader.pdf_array[j]
            clientNames.append(find_clientName(temp_pdf))
            j += 1
        return clientNames
    except:
        print("find_allClientName: Error")

# finds all Sub Total
def find_allSubTotal():
    try:
        subTotals = []
        j = 0
        while(j<10):
            temp_pdf = pdfreader.pdf_array[j]
            subTotals.append(find_subTotal(temp_pdf))
            j += 1
        return subTotals
    except:
        print("find_allSubTotal: Error")

# finds all Discount 
def find_allDiscount():
    try:
        discounts = []
        j = 0
        while(j<10):
            temp_pdf = pdfreader.pdf_array[j]
            discounts.append(find_discount(temp_pdf))
            j += 1
        return discounts
    except:
        print("find_allDiscount: Error")

# finds all Taxs 
def find_allTax():
    try:
        taxs = []
        j = 0
        while(j<10):
            temp_pdf = pdfreader.pdf_array[j]
            taxs.append(find_tax(temp_pdf))
            j += 1
        return taxs
    except:
        print("find_allTax: Error")

# finds all Tax rates 
def find_allTaxRates():
    try:
        taxrates = []
        j = 0
        while(j<10):
            temp_pdf = pdfreader.pdf_array[j]
            taxrates.append(find_taxRate(temp_pdf))
            j += 1
        return taxrates
    except:
        print("find_allTaxRates: Error")

# find all invoice total
def find_allInvoiceTotal():
    try:
        invoceiTotals = []
        j = 0
        while(j<10):
            temp_pdf = pdfreader.pdf_array[j]
            invoceiTotals.append(find_invoiceTotal(temp_pdf))
            j += 1
        return invoceiTotals
    except:
        print("find_allInvoiceTotal: Error")

# find all zip codes
def find_allZipCode():
    try:
        zipCodes = []
        j = 0
        while(j<10):
            temp_pdf = pdfreader.pdf_array[j]
            zipCodes.append(find_zipCode(temp_pdf))
            j += 1
        return zipCodes
    except:
        print("find_allZipCode: Error")

# find all Domains
def find_allDomain():
    try:
        domains = []
        j = 0
        while(j<10):
            temp_pdf = pdfreader.pdf_array[j]
            domains.append(find_domain(temp_pdf))
            j += 1
        return domains
    except:
        print("find_allDomain: Error")

# find all mails
def find_allMail():
    try:
        mails = []
        j = 0
        while(j<10):
            temp_pdf = pdfreader.pdf_array[j]
            mails.append(find_mail(temp_pdf))
            j += 1
        return mails
    except:
        print("find_allMail: Error")

# find all phone numbers
def find_allPhoneNumbers():
    try:
        phoneNumbers = []
        j = 0
        while(j<10):
            temp_pdf = pdfreader.pdf_array[j]
            phoneNumbers.append(find_phoneNumber(temp_pdf))
            j += 1
        return phoneNumbers
    except:
        print("find_allPhoneNumbers: Error")

# find all account holders
def find_allAccountHolders():
    try:
        accountHolders = []
        j = 0
        while(j<10):
            temp_pdf = pdfreader.pdf_array[j]
            accountHolders.append(find_acountHolder(temp_pdf))
            j += 1
        return accountHolders
    except:
        print("find_allAccountHolders: Error")
