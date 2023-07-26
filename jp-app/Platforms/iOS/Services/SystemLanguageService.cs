using Foundation;
using jp_app.Services;

namespace jp_app.Platforms.iOS.Services
{
    public class SystemLanguageService : ISystemLanguageService
    {
        public string GetSystemLanguage()
        {
            return NSLocale.PreferredLanguages[0];
        }
    }
}