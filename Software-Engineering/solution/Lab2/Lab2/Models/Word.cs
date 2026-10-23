using System.Xml.Serialization;

namespace Lab2.Models;

public class Word : Token
{
    public static String consonants = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ";
    public static String vowels = "aeiouyаеёиуыэюя";
    
    public Word() { }
    public Word(string value) => Value = value;

    public override string Value
    {
        get => base.Value;

        set
        {
            if (value.All(char.IsLetter))
            {
                base.Value = value;
            }
        }
        
    } 
    
    [XmlIgnore]
    public int  Length => Value.Length;
    
    [XmlIgnore]
    public bool IsEmpty => string.IsNullOrWhiteSpace(Value);

    public bool StartsWithConsonant()
    {
        if (IsEmpty) return false;
        char c = char.ToLower(Value[0]);
        return consonants.Contains(c);
    }

    public bool StartsWithVowel()
    {
        if (IsEmpty) return false;
        char c = char.ToLower(Value[0]);
        return vowels.Contains(c);
    }
}