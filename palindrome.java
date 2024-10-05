class palindrome {
    public static void main(String[] args) {
      
      int num = 3553, r = 0, rem;
      
      
      int Num = num;
      
      
      while (num != 0) {
        rem = num % 10;
        r = r * 10 + rem;
        num /= 10;
      }
      
      
      if (Num == r) {
        System.out.println(Num + " is Palindrome.");
      }
      else {
        System.out.println(Num + " is not Palindrome.");
      }
    }
  }
