def calc_diferenca(valor_a, valor_b, valor_c, valor_d)
    return (valor_a * valor_b) - (valor_c * valor_d)
end

puts "DIFERENCA = #{calc_diferenca(gets.chomp.to_i, gets.chomp.to_i, gets.chomp.to_i, gets.chomp.to_i)}"