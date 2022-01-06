gets.chomp
fixo =  gets.chomp.to_f
vendas = gets.chomp.to_f

puts "TOTAL = R$ %.2f" % (fixo + (vendas * 0.15))