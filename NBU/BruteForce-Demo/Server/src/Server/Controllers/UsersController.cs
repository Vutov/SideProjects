using Microsoft.AspNetCore.Mvc;

namespace Server.Controllers
{
    using Models;
    using Repository;

    [Route("api/[controller]")]
    public class UsersController : Controller
    {
        private readonly Repository _repository;

        public UsersController()
        {
            this._repository = new Repository();
        }

        [HttpPost]
        [Route("login")]
        public IActionResult Login(LoginBindingModel model)
        {
            if (model == null)
            {
                return this.BadRequest("Invalid user data!");
            }

            if (!this.ModelState.IsValid)
            {
                return this.BadRequest(this.ModelState);
            }

            //if (this._repository.IsLocked(model.Username))
            //{
            //    return this.Unauthorized();
            //}
            
            if (this._repository.IsUser(model.Username, model.Password))
            {
                return this.Ok(); // Return token, redirect etc
            }
            
            return this.BadRequest("Invalid Username or Password!");
        }

        [HttpGet]
        [Route("passwords")]
        public IActionResult GetHashedPasswords()
        {
            return this.Ok(this._repository.GetPasswords());
        }

    }
}
