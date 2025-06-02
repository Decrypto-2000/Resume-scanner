namespace ResumeScanner.API.Models
{
    public class ResumeResponse
    {
        public double MatchScore { get; set; }
        public string[] ExtractedSkills { get; set; }
    }
}
