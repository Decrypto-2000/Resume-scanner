namespace ResumeScanner.API.Models
{
    public class ResumeRequest
    {
        public IFormFile? ResumeFile { get; set; }
        public string? JobDescription { get; set; }
    }
}
