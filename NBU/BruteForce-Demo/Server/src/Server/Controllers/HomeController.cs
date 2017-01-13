namespace Server.Controllers
{
    using Microsoft.AspNetCore.Mvc;

    [Route("api/[controller]")]
    public class HomeController: Controller
    {
        public string Get()
        {
            return "Api working";
        }
    }
}
