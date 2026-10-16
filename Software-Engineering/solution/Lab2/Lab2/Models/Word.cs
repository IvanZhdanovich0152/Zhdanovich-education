using System.Xml.Serialization;

namespace Lab2.Models;

public class Word : Token
{
    public Word() { }
    public Word(string value) => Value = value; 
    
    [XmlIgnore]
    public int  Length => Value.Length;
    
    [XmlIgnore]
    public bool IsEmpty => string.IsNullOrWhiteSpace(Value);

    public bool StartsWithConsonant()
    {
        if (IsEmpty) return false;
        char c = char.ToLower(Value[0]);
        const string consonants = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ";
        return consonants.Contains(c);
    }

    public bool StartsWithVowel()
    {
        if (IsEmpty) return false;
        char c = char.ToLower(Value[0]);
        const string vowels = "aeiouyаеёиуыэюя";
        return vowels.Contains(c);
    }
}