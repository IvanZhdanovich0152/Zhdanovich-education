using System.Xml.Serialization;

namespace Lab2.Models;

[XmlRoot("text")]
public class Text
{
    [XmlElement("sentence")]
    public List<Sentence> Sentences { get; set; } = new();

    public override string ToString() =>
        string.Join(" ", Sentences.Select(s => s.OriginalText));
}