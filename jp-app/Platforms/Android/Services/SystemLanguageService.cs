using Android.Content.Res;
using jp_app.Services;

namespace jp_app.Platforms.Android.Services
{
    public class SystemLanguageService : ISystemLanguageService
    {
        public string GetSystemLanguage()
        {
            return Resources.System.Configuration.Locale.Default.Iso3Language;
        }
    }
}