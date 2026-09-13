using System.Drawing;
using System.Drawing.Imaging;
using System.Text;
using System.Text.RegularExpressions;

namespace Lab1
{
    public class Program
    {
        static readonly Dictionary<string, Color> ColorMap = new(StringComparer.OrdinalIgnoreCase)
        {
            { "красн", Color.Red },
            { "ал", Color.Crimson },
            { "багр", Color.DarkRed },
            { "зелен", Color.Green },
            { "изумруд", Color.MediumSeaGreen }, 
            { "малахит", Color.MediumSeaGreen },
            { "син", Color.Blue },
            { "голуб", Color.LightBlue },
            { "лазур", Color.LightSkyBlue },
            { "ультрамарин", Color.Blue },
            { "желт", Color.Yellow },
            { "золот", Color.Gold },
            { "лимон", Color.LemonChiffon },
            { "бел", Color.White }, 
            { "черн", Color.Black },
            { "сер", Color.Gray }, 
            { "фиолетов", Color.Purple }, 
            { "лилов", Color.Purple },
            { "оранжев", Color.Orange }, 
            { "коричнев", Color.Brown }, 
            { "розов", Color.Pink },
            { "бирюз", Color.Turquoise }
        };

        public static void Main()
        {
            string inputPath = "Podarok.txt"; 
            string outputPath = "Output.png";
            
            try
            {
                if (!File.Exists(inputPath))
                {
                    Console.WriteLine($"Файл не найден: {inputPath}");
                    return;
                }

                string text = File.ReadAllText(inputPath, Encoding.UTF8);
                var colors = ExtractColors(text);

                if (colors.Count == 0)
                {
                    Console.WriteLine("В тексте не найдено слов, обозначающих цвета.");
                    return;
                }

                VisualizeColorsGrid(colors, outputPath);
                // PrintStatistics(colors);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Ошибка выполнения: {ex.Message}");
            }
        }

        static List<Color> ExtractColors(string text)
        {
            var detectedColors = new List<Color>();
            var words = Regex.Matches(text.ToLower(), @"\b[\p{IsCyrillic}a-z]+\b");

            foreach (Match match in words)
            {
                string word = match.Value;
                var foundColor = ColorMap.FirstOrDefault(kvp => word.StartsWith(kvp.Key));
                
                if (foundColor.Key != null)
                {
                    detectedColors.Add(foundColor.Value);
                }
            }
            return detectedColors;
        }

        static void VisualizeColorsGrid(List<Color> colors, string outputPath)
        {
            const int squareSize = 30; 
            
            int cols = (int)Math.Ceiling(Math.Sqrt(colors.Count));
            int rows = (int)Math.Ceiling((double)colors.Count / cols);

            int imgWidth = cols * squareSize;
            int imgHeight = rows * squareSize;

            using (Bitmap bmp = new Bitmap(imgWidth, imgHeight))
            using (Graphics g = Graphics.FromImage(bmp))
            {
                g.Clear(Color.White);

                for (int i = 0; i < colors.Count; i++)
                {
                    int x = (i % cols) * squareSize;
                    int y = (i / cols) * squareSize;

                    using (SolidBrush brush = new SolidBrush(colors[i]))
                    {
                        g.FillRectangle(brush, x, y, squareSize, squareSize);
                    }
                }

                bmp.Save(outputPath, ImageFormat.Png);
                Console.WriteLine($"Визуализация сохранена в {outputPath}");
            }
        }

        // static void PrintStatistics(List<Color> colors)
        // {
        //     Console.WriteLine("\nЧастота упоминания цветов:");
        //     var stats = colors.GroupBy(c => c.Name)
        //                       .Select(g => new { Color = g.Key, Count = g.Count() })
        //                       .OrderByDescending(x => x.Count);
        //
        //     foreach (var stat in stats)
        //     {
        //         Console.WriteLine($"- {stat.Color}: {stat.Count}");
        //     }
        // }
    }
}