using Microsoft.AspNetCore.Mvc;
using ResumeScanner.API.Models;
using ResumeScanner.API.Services;

namespace ResumeScanner.API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ResumeController : ControllerBase
    {
        private readonly ResumeService _resumeService;

        public ResumeController(ResumeService resumeService)
        {
            _resumeService = resumeService;
        }

        [HttpPost("upload")]
        public async Task<IActionResult> Upload([FromForm] ResumeRequest request)
        {
            if (request.ResumeFile == null || string.IsNullOrEmpty(request.JobDescription))
                return BadRequest("Invalid resume or job description.");

            var result = await _resumeService.ProcessResume(request);
            return Ok(result);
        }
    }
}
