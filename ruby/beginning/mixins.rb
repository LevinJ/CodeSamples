module A
   def a1
     puts "a1 from A"
   end
   def a2
   end
end
module B
   def b1
     puts "b1 from B"
   end
   def b2
   end
end

class Sample
include A
include B
   def s1
   end
end

samp=Sample.new
samp.a1
samp.a2
samp.b1
samp.b2
samp.s1