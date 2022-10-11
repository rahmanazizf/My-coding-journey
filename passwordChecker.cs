using System;

namespace PasswordChecker
{
  class Program
  {
    public static void Main(string[] args)
    {
      int minLength = 8;
      string uppercase = "ABCDEFGHIJKLMNOPQRSTUVWZYZ";
      string lowercase = uppercase.ToLower();
      string digits = "0123456789";
      string specialChars = "?!#-_";

      Console.WriteLine("Please enter your password");
      string password = Console.ReadLine();

      int score = 0;

      if (password.Length >= minLength)
      {
        score ++;
      }
      if (Tools.Contains(password, uppercase))
      {
        score ++;
      }
      if (Tools.Contains(password, lowercase))
      {
        score ++;
      }
      if (Tools.Contains(password, digits))
      {
        score++;
      }
      if (Tools.Contains(password, specialChars))
      {
        score++;
      }
      Console.WriteLine(score);

      switch (score)
      {
        case 5:
        case 4:
        Console.WriteLine("Extremely strong");
        break;
        case 3:
        Console.WriteLine("Strong");
        break;
        case 2:
        Console.WriteLine("Medium");
        break;
        case 1:
        Console.WriteLine("Weak");
        break;
        default:
        Console.WriteLine("The Password does not meet any standards");
        break;

      }


    }
  }
}
