namespace Sanitizer
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;
    using System.Text.RegularExpressions;

    /// <summary>
    /// HQC sanitizer, string friendly. Makes your refactoring work much easier.
    /// Keeps original comments and strings as they are, refactores whitespace.
    /// Best used with VS ctr + k, ctr + d. 
    /// Version 0.15b
    /// </summary>
    public class Sanitizer
    {
        public static void Main(string[] args)
        {
            var fuckedUpText = File.ReadAllText("../../../1.cs");
            var replacedComments = new HashSet<string>();

            // Regex
            const string StringRegex = "(\"[^\"]+\")";
            const string CommentsRegex = @"^(?:[ ]+?)?(\/\/[^\/]+?)$";
            const string StarCommentsRegex = @"(/\*[\s\S]+?\*/)";
            const string PropertiesRegex = @"\s+{[\s]+?(get;)\s+?([\s\S]+?set;)\s+?}";
            const string ParentisisInMethodOpeningRegex = @"(\]|=>)\s+{\s+";
            const string ParentisisInMethodClosingRegex = @"\s+}\s+,";

            // Strings and Comments
            var stringsBefore = Regex.Matches(fuckedUpText, StringRegex);
            var commentsBefore = Regex.Matches(fuckedUpText, CommentsRegex, RegexOptions.Multiline);
            var starCommentsBefore = Regex.Matches(fuckedUpText, StarCommentsRegex);

            // WhiteSpace
            var goodLooking = Regex.Replace(fuckedUpText, "\\s+", " ");

            // Brackets
            goodLooking = Regex.Replace(goodLooking, "{", "\n{\n");
            goodLooking = Regex.Replace(goodLooking, "}", "\n}\n\n");

            // Commas
            goodLooking = Regex.Replace(goodLooking, "\\s?;", ";\n");

            // Method calls
            goodLooking = Regex.Replace(goodLooking, "\\s?\\.\\s?", ".");

            // Empty lines after '}', ';' following '}', ')' following '}'
            goodLooking = Regex.Replace(goodLooking, "}\\s+}", "}\n}");
            goodLooking = Regex.Replace(goodLooking, "}\\s+}\\s+}", "}\n}\n}");
            goodLooking = Regex.Replace(goodLooking, "}\\s+}\\s+}\\s+}", "}\n}\n}\n}");
            goodLooking = Regex.Replace(goodLooking, "}\\s+}\\s+}\\s+}\\s+}", "}\n}\n}\n}\n}");
            goodLooking = Regex.Replace(goodLooking, ";\\s+}", ";\n}");
            goodLooking = Regex.Replace(goodLooking, "\\s*}\\s+\\)", "})");

            // Single line auto-properties
            goodLooking = Regex.Replace(goodLooking, PropertiesRegex, " { $1 $2}");

            // '}' in method call
            goodLooking = Regex.Replace(goodLooking, ParentisisInMethodOpeningRegex, "$1 {");
            goodLooking = Regex.Replace(goodLooking, ParentisisInMethodClosingRegex, "},");

            // if-else construction
            goodLooking = Regex.Replace(goodLooking, "}\\s+else", "}\nelse");

            var stringsAfter = Regex.Matches(goodLooking, StringRegex);
            if (stringsBefore.Count != stringsAfter.Count)
            {
                var before = (from Match b in stringsBefore
                              select b.Groups[1].Value)
                    .ToList();
                var after = (from Match a in stringsAfter
                             select a.Groups[1].Value)
                    .ToList();
                var diff = before.Except(after);
                var differencesString = string.Join(", ", diff);
                var message = string.Format("Possible string mismatch: {0}", differencesString);
                throw new InvalidOperationException(message);
            }

            for (int i = 0; i < stringsBefore.Count; i++)
            {
                var before = stringsBefore[i].Groups[1].Value;
                var after = stringsAfter[i].Groups[1].Value;
                if (!string.IsNullOrEmpty(before))
                {
                    goodLooking = goodLooking.Replace(after, before);
                }
            }

            foreach (Match comment in commentsBefore)
            {
                var oldComment = comment.Groups[1].Value.Trim();
                if (!replacedComments.Contains(oldComment))
                {
                    if (!goodLooking.Contains(oldComment))
                    {
                        Console.Error.WriteLine("Missing comment: \"{0}\"", oldComment);
                    }

                    var commentWithNewLine = "\n" + oldComment + "\n";
                    goodLooking = goodLooking.Replace(oldComment, commentWithNewLine);
                    replacedComments.Add(oldComment);
                }
            }

            var starCommentsAfter = Regex.Matches(goodLooking, StarCommentsRegex);
            for (int i = 0; i < starCommentsBefore.Count; i++)
            {
                var before = starCommentsBefore[i].Groups[1].Value + "\n";
                var after = starCommentsAfter[i].Groups[1].Value;
                if (!string.IsNullOrEmpty(before))
                {
                    goodLooking = goodLooking.Replace(after, before);
                }
            }

            File.WriteAllText("../../../Result.cs", goodLooking.Trim());
        }
    }
}