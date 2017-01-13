namespace Server.Controllers
{
    using System.Web.Http;
    using Models;
    using Repository;

    [RoutePrefix("api/users")]
    public class UsersController : ApiController
    {
        private readonly Repository _repository;

        public UsersController()
        {
            this._repository = new Repository();
        }

        [HttpPost]
        [Route("login")]
        public IHttpActionResult Login(LoginBindingModel model)
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
        public IHttpActionResult GetHashedPasswords()
        {
            return this.Ok(this._repository.GetPasswords());
        }

    }
}
