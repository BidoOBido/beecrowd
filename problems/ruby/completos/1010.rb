produto_1 = gets.chomp.split(" ")
produto_2 = gets.chomp.split(" ")

puts "VALOR A PAGAR: R$ %.2f" % ((produto_1[1].to_i * produto_1[2].to_f) + (produto_2[1].to_i * produto_2[2].to_f)).round(2)