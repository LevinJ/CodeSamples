$global_variable = 10


class Variables
  @@no_of_variables = 0
  VARCONSTANT1 = 100
  VARCONSTANT2 = "this could be cool"
  def print_global
    puts "Global variable is #$global_variable"
  end
  def initialize(id)
    @id= id
    @@no_of_variables += 100
  end
  def print_instance
    puts "instance variable is #@id"
  end
  def print_calss_variable
    puts "class variable is #@@no_of_variables"
    puts @@no_of_variables
    puts @@no_of_variables + 2000
  end
  def print_constant
    puts "constant1: #{VARCONSTANT1}"
    puts "constant2: #{VARCONSTANT2}"
    puts "current file #{__FILE__}"
    puts "current line #{__LINE__}"
  end
end

$global_variable = $global_variable + 3
obj = Variables.new(5)
$global_variable = $global_variable + 3
obj.print_global()
obj.print_instance()
obj.print_calss_variable()
obj.print_constant()


ary = [  "fred", 10, 3.14, "This is a string", "last element", ]
ary.each do |i|
   puts i
end

hsh = colors = { "red" => 0xf00, "green" => 0x0f0, "blue" => 0x00f }
hsh.each do |key, value|
   print key, " is ", value, "\n"
end


(10..15).each do |n| 
   print n, ' ' 
end



