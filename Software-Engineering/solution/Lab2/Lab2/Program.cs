using Lab2.Services;

namespace Lab2;

internal class Program
{
    private static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;

        var raw = File.ReadAllText("Data/input.txt");
        var text = TextParser.Parse(raw);
        var processor = new TextProcessor(text);
        var stopWords = new StopWordService(
            "Data/stopwords_en.txt",
            "Data/stopwords_ru.txt");


        while (true)
        {
            Console.WriteLine("\n1 - сортировка по кол-ву слов");
            Console.WriteLine("2 - сортировка по длине");
            Console.WriteLine("3 - слова длины N в вопросах");
            Console.WriteLine("4 - удалить слова длины N на согласную");
            Console.WriteLine("5 - замена в предложении");
            Console.WriteLine("6 - удалить стоп-слова");
            Console.WriteLine("7 - экспорт в XML");
            Console.WriteLine("8 - показать токены предложения");
            Console.WriteLine("9 - Подсчет вхождения слов в предложения");
            Console.WriteLine("0 - выход");
            Console.Write("> ");

            var choice = Console.ReadLine();
            switch (choice)
            {
                case "1":
                    foreach (var s in processor.SortByWordCount())
                        Console.WriteLine(s);
                    break;

                case "2":
                    foreach (var s in processor.SortByLength())
                        Console.WriteLine(s);
                    break;

                case "3":
                    Console.Write("Длина слова: ");
                    int len3 = int.Parse(Console.ReadLine()!);
                    foreach (var w in processor.FindWordsInQuestions(len3))
                        Console.WriteLine(w);
                    break;

                case "4":
                    Console.Write("Длина слова: ");
                    int len4 = int.Parse(Console.ReadLine()!);
                    processor.RemoveConsonantWords(len4);
                    Console.WriteLine(TextParser.Restore(text));
                    break;

                case "5":
                    Console.Write("Индекс предложения: ");
                    int idx = int.Parse(Console.ReadLine()!);
                    Console.Write("Длина слова: ");
                    int len5 = int.Parse(Console.ReadLine()!);
                    Console.Write("Замена: ");
                    string repl = Console.ReadLine()!;
                    processor.ReplaceInSentence(idx, len5, repl);
                    Console.WriteLine(TextParser.Restore(text));
                    break;

                case "6":
                    processor.RemoveStopWords(stopWords);
                    Console.WriteLine(TextParser.Restore(text));
                    break;

                case "7":
                    XmlExporter.Export(text, "Data/output.xml");
                    Console.WriteLine("Сохранено в Data/output.xml");
                    break;

                case "8":
                    Console.Write("Индекс предложения: ");
                    int di = int.Parse(Console.ReadLine()!);
                    Console.WriteLine(TextProcessor.DumpTokens(text.Sentences[di]));
                    break;
                case "9":
                    var wordEntry = WordEntryBuilder.Build(text);
                    Console.WriteLine(WordEntryBuilder.Format(wordEntry));
                    break;

                case "0":
                    return;
            }
        }
    }
}