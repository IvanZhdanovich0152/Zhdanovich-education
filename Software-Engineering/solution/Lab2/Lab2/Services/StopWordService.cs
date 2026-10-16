namespace Lab2.Services;

public class StopWordService
{
    private readonly HashSet<string> _stopWords;

    public StopWordService(params string[] files)
    {
        _stopWords = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
        foreach (var file in files)
        {
            if (!File.Exists(file)) continue;
            foreach (var line in File.ReadAllLines(file))
            {
                var w = line.Trim();
                if (!string.IsNullOrEmpty(w))
                    _stopWords.Add(w);
            }
        }
    }

    public bool IsStopWord(string word) => _stopWords.Contains(word);

}