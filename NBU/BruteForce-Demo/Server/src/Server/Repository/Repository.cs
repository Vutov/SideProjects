namespace Server.Repository
{
    using System.Collections.Generic;
    using System.Linq;
    using DevOne.Security.Cryptography.BCrypt;

    public class Repository
    {
        private const int LockThreshold = 5;

        private static readonly Dictionary<string, string> UserData = new Dictionary<string, string>();
        private static readonly Dictionary<string, int> LoginAttempts = new Dictionary<string, int>();
        private readonly Passwords _passwords;

        public Repository()
        {
            this._passwords = new Passwords();
            if (UserData.Count == 0)
            {
                this.SeedPasswords();
            }
        }

        public List<string> GetPasswords()
        {
            return UserData.Values
                .Select(password => BCryptHelper.HashPassword(password, BCryptHelper.GenerateSalt()))
                .ToList();
        }

        public bool IsUser(string userName, string password)
        {
            if (UserData.ContainsKey(userName))
            {
                var usersPassword = UserData[userName];
                if (usersPassword == password)
                {
                    return true;
                }

                this.AddLoginAttempt(userName);
            }

            return false;
        }

        public bool IsLocked(string userName)
        {
            if (LoginAttempts.ContainsKey(userName) && LoginAttempts[userName] >= LockThreshold)
            {
                return true;
            }

            return false;
        }

        private void SeedPasswords()
        {
            UserData.Add("User1", this._passwords.Password1);
            UserData.Add("User2", this._passwords.Password2);
            UserData.Add("User3", this._passwords.Password3);
            UserData.Add("User4", this._passwords.Password4);
        }

        private void AddLoginAttempt(string userName)
        {
            if (LoginAttempts.ContainsKey(userName) == false)
            {
                LoginAttempts.Add(userName, 0);
            }

            LoginAttempts[userName]++;
        }
    }
}
