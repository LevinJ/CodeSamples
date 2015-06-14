#I am a comment, Just ignore me
puts "hello, ruby!"
BEGIN{
  puts "Initializing Ruby Program"
}
END{
puts "Terminating ruby program"
}
class Customer
   @@no_of_customers=0
   def initialize(id,name,addr)
	@cust_id = id
	@cust_name=name
	@cust_addr=addr
   end
end
cust1 = Customer.new("1","John","Windows Apartment,ludhiya")
cust2 = Customer.new("2","paul","new empire road,khandala")


class Sample
	def hello
		puts "hello ruby from the sample class"
	end
end

#Now using above class to create objects
object = Sample.new
object.hello
