# Hanoi Towers O(2^n)

# Example

With 3 disks


Tower 1

  ■■■
  
 ■■■■■
 
■■■■■■■

Tower 2

Tower 3

-------------------------
moving disk from Tower 1 to Tower 3

Tower 1

 ■■■■■
 
■■■■■■■

Tower 2

Tower 3

■■■

-------------------------
moving disk from Tower 1 to Tower 2

Tower 1

■■■■■■■

Tower 2

■■■■■

Tower 3

■■■

-------------------------
moving disk from Tower 3 to Tower 2

Tower 1

■■■■■■■

Tower 2

 ■■■
 
■■■■■

Tower 3

-------------------------
moving disk from Tower 1 to Tower 3
Tower 1

Tower 2

 ■■■
 
■■■■■

Tower 3

■■■■■■■

-------------------------
moving disk from Tower 2 to Tower 1

Tower 1

■■■

Tower 2

■■■■■

Tower 3

■■■■■■■

-------------------------
moving disk from Tower 2 to Tower 3

Tower 1

■■■

Tower 2

Tower 3

 ■■■■■
 
■■■■■■■

-------------------------
moving disk from Tower 1 to Tower 3

Tower 1

Tower 2

Tower 3

  ■■■
  
 ■■■■■
 
■■■■■■■


-------------------------
Time used

--- 3.468809127807617 seconds ---
