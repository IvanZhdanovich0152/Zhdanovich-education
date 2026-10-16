using System.Xml.Serialization;

namespace Lab2.Models;

public class Sentence
{
    [XmlIgnore]
    public List<Token> Tokens { get; set; } = new();

    [XmlElement("word")]
    public List<Word> XmlWords
    {
        get => Tokens.OfType<Word>().ToList();
        set => Tokens = value.Cast<Token>().ToList();
    }
    
    [XmlIgnore] public string OriginalText { get; set; } = string.Empty;
    
    [XmlIgnore] public IEnumerable<Word> Words => Tokens.OfType<Word>();
    [XmlIgnore] public IEnumerable<Punctuation> Punctuations => Tokens.OfType<Punctuation>();

    [XmlIgnore]
    public char Terminator
    {
        get
        {
            var last = Tokens.OfType<Punctuation>()
                .LastOrDefault(p => p.IsSentenceTerminator);
            return last?.Value[0] ?? '.';
        }
    }

    [XmlIgnore]
    public bool IsInterrogative => Terminator == '?';

    [XmlIgnore]
    public int WordCount => Words.Count();

    [XmlIgnore]
    public int Length => OriginalText.Length;

    public override string ToString() => OriginalText;    
}