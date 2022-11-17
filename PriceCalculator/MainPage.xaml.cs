using System.Diagnostics;

namespace PriceCalculator
{
    public partial class MainPage : ContentPage
    {
        int count = 0;

        public MainPage()
        {
            InitializeComponent();
            this.Loaded += MainPage_Loaded;
        }

        private void MainPage_Loaded(object sender, EventArgs e)
        {
            double w = DeviceDisplay.Current.MainDisplayInfo.Width / 8;
            double h = DeviceDisplay.Current.MainDisplayInfo.Height / 2;

            Window.MinimumWidth = w;
            Window.MaximumWidth = w;
            Window.MinimumHeight = h;
            Window.MaximumHeight = h;

            Preferences.Set("height", h);
            Preferences.Set("width", w);
        }

        private void OnCounterClicked(object sender, EventArgs e)
        {
            count++;

            if (count == 1)
                CounterBtn.Text = $"Clicked {count} time";
            else
                CounterBtn.Text = $"Clicked {count} times";

            SemanticScreenReader.Announce(CounterBtn.Text);
        }
    }
}