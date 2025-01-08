using Microsoft.Extensions.Logging.Internal;
using MongoDB.Bson;
using MongoDB.Driver;

internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
        string connnectionString = "mongodb://root:123456@127.0.0.1:27017/";
        var client = new MongoClient(connnectionString);
        var colletions = client.GetDatabase("DemoDB").GetCollection<BsonDocument>("Users");
        if (colletions!=null)
        {
            foreach (var item in colletions.Aggregate<BsonDocument>().ToList())
            {
                System.Console.WriteLine(item["username"]);
                System.Console.WriteLine(item["fullname"]);
            }
        }
    }
}