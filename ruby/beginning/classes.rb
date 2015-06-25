class Customer
  @@no_of_customers =0
  def initialize(id,name,addr)
    @cust_id = id
    @cust_name = name
    @addr = addr
    @@no_of_customers +=1
  end
  def hello
    puts "Hello Ruby!"
  end
  def display_details
    puts "Customer id #@cust_id"
    puts "Customer name #@cust_name"
    puts "Customer address #@cust_addr"
  end
  def total_no_of_customers
    puts "Total number of customers: #@@no_of_customers"
  end
end

cust1 = Customer.new("1","John","addr1")
cust2 = Customer.new("2","name","addr")

cust1.hello()
cust1.display_details()
cust2.display_details()
cust1.total_no_of_customers()
cust2.total_no_of_customers()

# a case study about class and objects