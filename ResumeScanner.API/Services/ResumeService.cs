using ResumeScanner.API.Models;

namespace ResumeScanner.API.Services
{
    public class ResumeService
    {
        private readonly IHttpClientFactory _httpClientFactory;

        public ResumeService(IHttpClientFactory httpClientFactory)
        {
            _httpClientFactory = httpClientFactory;
        }

        public async Task<ResumeResponse> ProcessResume(ResumeRequest request)
        {
            // Save resume temporarily
            var filePath = Path.GetTempFileName();
            using (var stream = System.IO.File.Create(filePath))
            {
                await request.ResumeFile.CopyToAsync(stream);
            }

            var client = _httpClientFactory.CreateClient();
            var form = new MultipartFormDataContent
            {
                { new StringContent(request.JobDescription), "job_description" },
                { new StreamContent(System.IO.File.OpenRead(filePath)), "resume", request.ResumeFile.FileName }
            };

            var response = await client.PostAsync("http://localhost:5001/analyze", form);
            if (!response.IsSuccessStatusCode)
                throw new Exception("Python service failed");

            var content = await response.Content.ReadAsStringAsync();
            return System.Text.Json.JsonSerializer.Deserialize<ResumeResponse>(content);
        }
    }
}
