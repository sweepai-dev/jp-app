using System.Globalization;
using jp_app.Services;
using Microsoft.Maui.Controls;

namespace jp_app
{
    public partial class App : Application
    {
        private readonly ISystemLanguageService _systemLanguageService;

        public App(ISystemLanguageService systemLanguageService)
        {
            _systemLanguageService = systemLanguageService;

            InitializeComponent();

            MainPage = new AppShell();
        }

        protected override void OnStart()
        {
            var systemLanguage = _systemLanguageService.GetSystemLanguage();
            CultureInfo.CurrentCulture = new CultureInfo(systemLanguage);

            base.OnStart();
        }
    }
}
