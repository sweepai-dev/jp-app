using ObjCRuntime;
using UIKit;

namespace jp_app;

public class Program
{
    // This is the main entry point of the application.
    static void Main(string[] args)
    {
        Console.WriteLine("Hello world");
        // if you want to use a different Application Delegate class from "AppDelegate"
        // you can specify it here.
        UIApplication.Main(args, null, typeof(AppDelegate));
    }
}
