using System.Text;
using System.Text.RegularExpressions;
using Lab2.Models;

namespace Lab2.Services;


public static class TextParser
{
    private static readonly Regex TokenRegex = new(
        @"[A-Za-zА-Яа-яЁё'-]+|[.,!?;:-]",
        RegexOptions.Compiled);
    
    private static readonly Regex SentenceRegex = new(
        @"[^.!?]+[.!?]+|[^.!?]+$",
        RegexOptions.Compiled);

    public static Text Parse(string raw)
    {
        var text = new Text();

        foreach (Match sm in SentenceRegex.Matches(raw))
        {
            var sentenceStr = sm.Value.Trim();
            if (string.IsNullOrWhiteSpace(sentenceStr)) continue;
            
            var sentence = new Sentence {OriginalText = sentenceStr};

            foreach (Match tm in TokenRegex.Matches(sentenceStr))
            {
                var token = tm.Value;
                if (Regex.IsMatch(token, @"^[.,!?;:-]$"))
                    sentence.Tokens.Add(new Punctuation(token));
                else 
                    sentence.Tokens.Add(new Word(token));   
            }
            text.Sentences.Add(sentence);
        }

        return text;
    }

    public static string Restore(Sentence sentence)
    {
        var sb = new StringBuilder();

        Token? prev = null;

        foreach (var t in sentence.Tokens)
        {
            if (prev is Word && t is Word)
                sb.Append(' ');
            
            if (t is Punctuation p)
            {
                if (p.IsSentenceTerminator || p.IsComma)
                {
                    if (sb.Length > 0 && sb[^1] == ' ') sb.Length--;
                }
                sb.Append(p.Value);
            }
            else
            {
                sb.Append(t.Value);
            }

            prev = t;
        }

        return sb.ToString();
    }
    
    public static string Restore(Text text) =>
        string.Join(" ", text.Sentences.Select(Restore));
    
    public static void RefreshOriginals(Text text)
    {
        foreach (var s in text.Sentences)
            s.OriginalText = Restore(s);
    }
}
    

