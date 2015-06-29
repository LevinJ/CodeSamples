class Box
  BOX_COMPANY = "TATA INc"
  BOX_WEIGHT = 10
  #constructor method
  def initialize(w,h)
    @width,@height=w,h
  end
  #instance method
  def getArea
    @width * @height
  end
end

#define a subclass
class BigBox < Box
  #add a new instance method
  def printArea
    @area = @width * @height
    puts "Big box area is : #@area"
  end
  def getArea
    @area = @width * @height
    puts "Big box area is : #@area"
  end
end

#create an object
box = BigBox.new(10,20)
#box.printArea()
box.getArea()

puts Box::BOX_COMPANY

puts "Box weight is : #{Box::BOX_WEIGHT}"


#class Classinformation
#  #print calss information
#  puts "Type of self = #{self.type}"
#  puts "Name of self = #{self.name}"
#end
