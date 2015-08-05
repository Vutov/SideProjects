namespace Sanitizer
{
    using System.Collections.Generic;
    using System.IO;
    using System.Text.RegularExpressions;

    /// <summary>
    /// HQC sanitizer, string friendly. Makes your refactoring work much easier.
    /// Keeps original comments and strings as they are, refactores whitespace.
    /// Best used with VS ctr + k, ctr + d. 
    /// Version 0.1a
    /// </summary>
    public class Sanitizer
    {
        public static void Main(string[] args)
        {
            var fuckedUpText = File.ReadAllText("../../../1.cs");
            var replacedComments = new HashSet<string>();

            // Regex
            const string StringRegex = "(\"[^\"]+\")";
            const string CommentsRegex = "(//.+)";
            const string StarCommentsRegex = @"(/\*[\s\S]+?\*/)";

            // Strings and Comments
            var stringsBefore = Regex.Matches(fuckedUpText, StringRegex);
            var commentsBefore = Regex.Matches(fuckedUpText, CommentsRegex);
            var starCommentsBefore = Regex.Matches(fuckedUpText, StarCommentsRegex);

            // WhiteSpace
            var goodLooking = Regex.Replace(fuckedUpText, "\\s+", " ");

            // Brackets
            goodLooking = Regex.Replace(goodLooking, "{", "\n{\n");
            goodLooking = Regex.Replace(goodLooking, "}", "\n}\n");

            // Commas
            goodLooking = Regex.Replace(goodLooking, "\\s?;", ";\n");

            // Method calls
            goodLooking = Regex.Replace(goodLooking, "\\s?\\.\\s?", ".");

            // Empty lines after '}' and ';' following '}'
            goodLooking = Regex.Replace(goodLooking, "}\\s+}", "}\n}");
            goodLooking = Regex.Replace(goodLooking, ";\\s+}", ";\n}");

            var stringsAfter = Regex.Matches(goodLooking, StringRegex);
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
                var commentWithNewLine = oldComment + "\n";
                if (!replacedComments.Contains(oldComment))
                {
                    goodLooking = goodLooking.Replace(oldComment, commentWithNewLine);
                }

                replacedComments.Add(oldComment);
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

            File.WriteAllText("../../../Result.cs", goodLooking);
        }
    }
}