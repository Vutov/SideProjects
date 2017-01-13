namespace Server.Controllers
{
    using System.Web.Http;

    [RoutePrefix("")]
    public class HomeController: ApiController
    {
        [Route("")]
        public string Get()
        {
            return "Api working";
        }
    }
}
