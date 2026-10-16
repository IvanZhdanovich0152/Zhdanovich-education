namespace Lab2.Models;

public class WordEntry
{
    public string Word { get; set; } = string.Empty;
    
    public int Frequency { get; set; }

    public SortedSet<int> Lines { get; } = new();
    
    public override string ToString()
    {
        return $"{Word}.  {Frequency}: {string.Join(" ", Lines)}\n";
    }
}
