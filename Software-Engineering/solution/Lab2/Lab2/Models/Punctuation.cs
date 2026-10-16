using System.Xml.Serialization;
namespace Lab2.Models;

public class Punctuation : Token
{
    public Punctuation() { }
    public Punctuation(string value)  => Value = value;

    [XmlIgnore] public bool IsSentenceTerminator => Value is "." or "!" or "?";
    [XmlIgnore] public bool IsComma => Value is "," or ";" or ":";
}