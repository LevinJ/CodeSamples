$global_variable = 10
class Class1
	def print_global
		puts "Global variable in Class1 is #$global_variable"
	end
end

class Class2
	def print_global
		puts "Global variable in Class2 is #$global_variable"
	end
end

class1obj = Class1.new
class1obj.print_global

class2obj = Class2.new
class2obj.print_global


class Example
	VAR1 = 100
	VAR2 = 200
	def show
		puts "Value of first constant is #{VAR1}"
		puts "Value of second constant is #{VAR2}"
	end
end

#Create Objects
obj = Example.new()
obj.show()

puts "Multiplication value :#{24*60*60}"

ary = [ "fred",10,3.14,"This is a string", "last element"]
ary.each do  |i|
puts i
end


hsh = colors={"red"=>0xf00, "green"=>0x0f0,"blue"=>0x00f}
colors.each do |key,value|
	print key, " is ",value, "\n"
end

(10..15).each do |n|
	print n, ' '
end

