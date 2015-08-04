#while example
#$i = 0
#$num = 5
#
#while $i < $num  do
#   puts("Inside the loop i = #$i" )
#   $i +=1
#end


#$i = 0
#$num = 5
#begin
#   puts("Inside the loop i = #$i" )
#   $i +=1
#end while $i < $num


#for example

#for i in 0..5
#   puts "Value of local variable is #{i}"
#   if i == 2
#     break
#   end
#end

#for i in 0..5
#   if i == 2 then
#      next
#   end
#   puts "Value of local variable is #{i}"
#end

#$done = false
#for i in 0..5
#  puts "Value of local variable is #{i}"
#  if $done
#    next
#  end
#  if i == 2 then
#    $done = true;
#    redo
#  end
#end

#$done = false
#for i in 1..5
# 
#  puts "Value of local variable is #{i}"
#  if $done
#    next
#  end
#  $done = true
#  if i==2
#     retry
#   end
##  retry if i==2
#end


#for i in 1..5
#   retry if  i > 2
#   puts "Value of local variable is #{i}"
#end

20.times{|i| 
puts i
i = i+100
}