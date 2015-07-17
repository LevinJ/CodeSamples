#puts self

#class S  
#  puts 'Just started class S'  
#  puts self  
#  module M  
#    puts 'Nested module S::M'  
#    puts self  
#  end  
#  puts 'Back in the outer level of S'  
#  puts self  
#end


#
#class Item
#  def self.show
#    puts "Class method show invoked"
#  end  
#end
#
#Item.show

class Planet
  @@planets_count = 0
    
  def initialize(name)
    @name = name
    @@planets_count += 1
  end
  
  def self.planets_count
    @@planets_count
  end  
end

Planet.new("earth"); 

Planet.new("uranus")

p Planet.planets_count