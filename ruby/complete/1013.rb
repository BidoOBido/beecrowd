def self.maior(a, b)
  (a + b + (a - b).abs) / 2
end

A, B, C = gets.chomp.split.map(&:to_i)

maior = maior(maior(A, B), C)

puts format("%s eh o maior", maior)
