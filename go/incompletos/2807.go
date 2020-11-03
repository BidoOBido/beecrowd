package main

import (
  "fmt" 
)

func main() {
  var t int

  fmt.Scanln(&t)  
  if t > 2 {
    var v = make([]int,(t-1))
    v[t - 2] = 1
    v[t - 3] = 2
    for i := t-4; i >= 0; i-- {  
      v[i] = v[i+1]+v[i+2]
    }

    for i := 0; i < len(v)-1; i++{
      fmt.Printf("%d ", v[i])
    }

  }

  fmt.Printf("%d %d\n", 1, 1)
}

