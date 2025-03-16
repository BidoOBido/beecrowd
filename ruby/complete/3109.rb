def self.update(from, to)
  temp = $mesas[from - 1]
  $mesas[from - 1] = $mesas[to - 1]
  $mesas[to - 1] = temp
end

def self.query(goal, index)
  return 0 if $mesas[index - 1] == goal

  query(goal, $mesas[index - 1]) + 1
end

empregados = gets.chomp.to_i
eventos = gets.chomp.to_i

$mesas = (1..empregados).to_a

(1..eventos).each do
  args = gets.chomp.split(" ").map(&:to_i)
  evento = args.shift

  if evento == 1
    update(*args)
  else
    puts query(args[0], args[0])
  end
end
