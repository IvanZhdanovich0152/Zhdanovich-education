using System.Xml.Serialization;

namespace Lab2.Models;

[XmlInclude(typeof(Word))]
[XmlInclude(typeof(Punctuation))]

public abstract class Token
{
    [XmlText]
    public string Value { get; set; } = string.Empty;

    public override string ToString() => Value;
}