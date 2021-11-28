numero = gets.chomp.to_i
horas = gets.chomp.to_i
valor_horas = gets.chomp.to_f

puts "NUMBER = #{numero}"
puts "SALARY = U$ %.2f" % (horas * valor_horas).round(2)