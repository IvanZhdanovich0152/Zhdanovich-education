using Lab2.Models;
namespace Lab2.Services;

public static class WordEntryBuilder
{
    public static SortedDictionary<string, WordEntry> Build(Text text)
    {
        var result = new SortedDictionary<string, WordEntry>(StringComparer.OrdinalIgnoreCase);

        for (int i = 0; i < text.Sentences.Count; i++)
        {
            int lineNumber = i + 1;
            var sentence = text.Sentences[i];
            
            var seenInLine = new HashSet<string>(StringComparer.OrdinalIgnoreCase);

            foreach (var word in sentence.Words)
            {
                var key = word.Value.ToLowerInvariant();
                if (string.IsNullOrEmpty(key)) continue;

                if (!result.TryGetValue(key, out var entry))
                {
                    entry = new WordEntry { Word = key };
                    result[key] = entry;
                }

                entry.Frequency++;

                if (seenInLine.Add(key))
                    entry.Lines.Add(lineNumber);
            }
        }

        return result;
    }
    
    public static string Format(SortedDictionary<string, WordEntry> concordance) =>
        string.Join(" ", concordance.Values.Select(e => e.ToString()));
}