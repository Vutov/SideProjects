namespace _01.CowsAndBulls
{
    using System;
    using System.IO;
    using System.Text;

    public class CowsAndBulls
    {
        public static Random rng = new Random();
        public static StringBuilder log = new StringBuilder();
        public static string path = @"../../log.txt";

        public static void Main(string[] args)
        {

            var randomNum = GenerateNumber();
            var gameOver = false;
            while (!gameOver)
            {
                var userNumber = ReadNumber();
                var isValidNumer = IsValidInput(userNumber);
                if (isValidNumer)
                {
                    gameOver = CheckCowsAndBuls(randomNum, userNumber);
                    if (gameOver)
                    {
                        //randomNum = GenerateNumber();
                        Output("Game Over!");
                    }
                }

                File.AppendAllText(path, string.Join(Environment.NewLine, log));
            }
        }

        private static void Output(string message)
        {
            Console.WriteLine(message);
            log.AppendLine(message);
        }

        private static int ReadNumber()
        {
            var isValid = false;
            int number = -1;
            while (!isValid)
            {
                var input = Console.ReadLine();
                isValid = int.TryParse(input, out number);
                if (!isValid)
                {
                    var message = string.Format("Try Again! Invalid: {0}", input);
                    Output(message);
                }
            }

            return number;
        }

        private static bool CheckCowsAndBuls(int randomNum, int userNum)
        {
            var message = string.Empty;

            if (randomNum == userNum)
            {
                message = string.Format("Congratulations you guessed the number {0}", randomNum);
                Output(message);

                return true;
            }

            var stringRngNum = randomNum.ToString();
            var stringUserNum = userNum.ToString();
            int cows = 0;
            int bulls = 0;

            for (int i = 0; i < stringRngNum.Length; i++)
            {
                if (stringRngNum[i] == stringUserNum[i])
                {
                    bulls++;
                }
                else
                {
                    for (int j = 0; j < stringUserNum.Length; j++)
                    {
                        if (stringRngNum[i] == stringUserNum[j])
                        {
                            cows++;
                        }
                    }
                }
            }

            message = string.Format("Bulls: {0}, Cows: {1}", bulls, cows);
            Output(message);

            return false;
        }

        private static bool IsValidInput(int number)
        {
            var isValid = false;
            var message = string.Empty;

            if (IsValidNumber(number))
            {
                message = string.Format("Valid: {0}", number);
                Output(message);

                return true;
            }

            message = string.Format("Try Again! Invalid: {0}", number);
            Output(message);

            return false;
        }

        private static int GenerateNumber()
        {
            var num = rng.Next(1000, 10000);
            while (!IsValidNum(num))
            {
                num = rng.Next(1000, 10000);
            }

            var message = "Random Number Generated: " + num;
            //Output(message);

            return num;
        }

        private static bool IsValidNumber(int number)
        {
            if (number.ToString().Length == 4)
            {
                return IsValidNum(number);
            }

            return false;
        }

        private static bool IsValidNum(int num)
        {
            var stringNum = num.ToString();
            for (int i = 0; i < stringNum.Length - 1; i++)
            {
                for (int j = i + 1; j < stringNum.Length; j++)
                {
                    if (stringNum[i] == stringNum[j])
                    {
                        return false;
                    }
                }
            }

            return true;
        }
    }
}