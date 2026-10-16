using Lab2.Models;

namespace Lab2.Services;

public class TextProcessor
{
    private readonly Text _text;

    public TextProcessor(Text text) => _text = text;

    public IEnumerable<Sentence> SortByWordCount() =>
        _text.Sentences.OrderBy(s => s.WordCount);

    public IEnumerable<Sentence> SortByLength() =>
        _text.Sentences.OrderBy(s => s.Length);

    public IEnumerable<string> FindWordsInQuestions(int length) =>
        _text.Sentences
            .Where(s => s.IsInterrogative)
            .SelectMany(s => s.Words)
            .Where(w => w.Length == length)
            .Select(w => w.Value.ToLowerInvariant())
            .Distinct();

    public void RemoveConsonantWords(int length)
    {
        foreach (var s in _text.Sentences)
        {
            s.Tokens = s.Tokens
                .Where(t => !(t is Word w
                              && w.Length == length
                              && w.StartsWithConsonant()))
                .ToList();
        }
        TextParser.RefreshOriginals(_text);
    }

    public void ReplaceInSentence(int sentenceIndex, int wordLength, string replacement)
    {
        if (sentenceIndex < 0 || sentenceIndex >= _text.Sentences.Count)
            throw new ArgumentOutOfRangeException(nameof(sentenceIndex));

        var s = _text.Sentences[sentenceIndex];
        foreach (var w in s.Words.Where(w => w.Length == wordLength))
            w.Value = replacement;

        s.OriginalText = TextParser.Restore(s);
    }

    public void RemoveStopWords(StopWordService stopWordService)
    {
        foreach (var s in _text.Sentences)
        {
            s.Tokens = s.Tokens
                .Where(t => !(t is Word w && stopWordService.IsStopWord(w.Value)))
                .ToList();
        }
        TextParser.RefreshOriginals(_text);
    }

    public static string DumpTokens(Sentence s) =>
        string.Join(" | ", s.Tokens.Select(t =>
            $"{t.GetType().Name}({t.Value})"));

}